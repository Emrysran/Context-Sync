import click
import os
from datetime import datetime
from collectors import git, filesystem, terminal, privacy, env
import config as cfg_handler
import pyperclip

@click.group()
def cli():
    """Context-Sync: Capture and sync your development context."""
    pass

@cli.command()
def init():
    """Initialize a .ctx.json configuration file in current directory."""
    if cfg_handler.save_default_config():
        click.echo(click.style("Created .ctx.json with default settings.", fg='green', bold=True))
    else:
        click.echo(click.style("Config .ctx.json already exists.", fg='cyan'))

@cli.command()
@click.option('--output', '-o', default=None, help='Output file name')
@click.option('--clip', '-c', is_flag=True, help='Copy generated context to clipboard')
@click.option('--file', '-f', multiple=True, help='Include specific file contents in the context')
def sync(output, clip, file):
    """Capture current context and save to a markdown file."""
    config = cfg_handler.load_config()
    output_path = output or config.get("output_file", "context_state.md")
    
    click.echo(f"Capturing context for project: {os.path.basename(os.getcwd())}...")
    
    context_sections = []
    
    # 1. Header
    header = f"# Development Context Snapshot - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    header += f"Project: `{os.path.basename(os.getcwd())}`\n"
    context_sections.append(header)

    # 2. Env Context
    click.echo("  -> Collecting Environment info...")
    env_info = env.collect()
    context_sections.append(f"## Environment Info\n{env_info}")
    
    # 3. Git Context
    click.echo("  -> Collecting Git info...")
    git_info = git.collect()
    context_sections.append(f"## Git Context\n{git_info}")
    
    # 4. Filesystem Context
    click.echo("  -> Scanning filesystem...")
    fs_info = filesystem.collect(config)
    context_sections.append(f"## Filesystem Context\n{fs_info}")

    # 5. Targeted Files
    if file:
        click.echo(f"  -> Including {len(file)} targeted files...")
        file_sections = ["## Targeted Files Content"]
        for fpath in file:
            if os.path.exists(fpath) and os.path.isfile(fpath):
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        file_sections.append(f"### File: `{fpath}`\n```\n{content}\n```")
                except Exception as e:
                    file_sections.append(f"### File: `{fpath}`\nError reading file: {e}")
            else:
                file_sections.append(f"### File: `{fpath}`\n*(File not found or not a file)*")
        context_sections.append("\n".join(file_sections))
    
    # 6. Terminal Context
    click.echo("  -> Retrieving terminal history...")
    term_info = terminal.collect(config)
    context_sections.append(f"## Terminal Context\n{term_info}")
    
    # 7. AI Guidance Prompt
    ai_prompt = config.get("ai_guidance_prompt", "")
    if ai_prompt:
        context_sections.append(f"## AI 指引 (AI Guidance)\n> {ai_prompt}\n")
    
    # Final aggregation and sanitization
    full_content = "\n---\n".join(context_sections)
    if config.get("sanitize_secrets", True):
        click.echo("  -> Scrubbing sensitive data...")
        full_content = privacy.sanitize(full_content)
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    # Clipboard support
    if clip:
        pyperclip.copy(full_content)
        click.echo(click.style("📋 Content copied to clipboard!", fg='blue'))
        
    click.echo(click.style(f"Successfully synced to {output_path}", fg='green', bold=True))

@cli.command()
def clean():
    """Remove generated context files."""
    config = cfg_handler.load_config()
    output_path = config.get("output_file", "context_state.md")
    
    if os.path.exists(output_path):
        os.remove(output_path)
        click.echo(click.style(f"Removed {output_path}", fg='yellow'))
    else:
        click.echo("No context file found to clean.")

if __name__ == '__main__':
    cli()
