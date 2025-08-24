import click

from src.cli.cli_options import cli_options


@click.group()
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Enable verbose mode",
)
@click.option(
    "--debug",
    "-d",
    is_flag=True,
    help="Enable debug mode",
)
@click.option(
    "--quiet",
    "-q",
    is_flag=True,
    help="Enable quiet mode",
)
@click.option(
    "--version",
    "-V",
    is_flag=True,
    help="Show version",
)
@click.pass_context
def cli(ctx, verbose, debug, quiet, version):
    """Advanced Python code obfuscator with semantic preservation"""
    if verbose:
        ctx.obj["verbose"] = True
    if debug:
        ctx.obj["debug"] = True
    if quiet:
        ctx.obj["quiet"] = True
    if version:
        ctx.obj["version"] = True
    if not ctx.obj:
        ctx.obj = {}
