import click
import os
from datetime import datetime
from collectors import git, filesystem, terminal

@click.group()
def cli():
    """Context-Sync: Capture and sync your development context."""
    pass

@cli.command()
@click.option('--output', '-o', default='context_state.md', help='Output file name')
def sync(output):
    """Capture current context and save to a markdown file."""
    click.echo(f"Capturing context for project: {os.path.basename(os.getcwd())}...")
    
    context_sections = []
    
    # 1. Header
    header = f"# Development Context Snapshot - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    header += f"Project: `{os.path.basename(os.getcwd())}`\n"
    context_sections.append(header)
    
    # 2. Git Context
    click.echo("  -> Collecting Git info...")
    git_info = git.collect()
    context_sections.append(f"## Git Context\n{git_info}")
    
    # 3. Filesystem Context
    click.echo("  -> Scanning filesystem...")
    fs_info = filesystem.collect()
    context_sections.append(f"## Filesystem Context\n{fs_info}")
    
    # 4. Terminal Context
    click.echo("  -> Retrieving terminal history...")
    term_info = terminal.collect()
    context_sections.append(f"## Terminal Context\n{term_info}")
    
    # Write to file
    with open(output, 'w', encoding='utf-8') as f:
        f.write("\n---\n".join(context_sections))
        
    click.echo(click.style(f"Successfully synced to {output}", fg='green', bold=True))

if __name__ == '__main__':
    cli()
