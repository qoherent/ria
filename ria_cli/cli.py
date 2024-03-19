"""
This module contains the main group for the RIA Core CLI.
"""

import click

from ria_cli.dataset_manager import commands as dataset_manager_commands
from ria_cli.diagnostics import commands as diagnostic_commands
from ria_cli.model_builder import commands as model_builder_commands
from ria_cli.utils import commands as utils_commands


@click.group()
@click.option("-v", "--verbose", is_flag=True, help="Increase verbosity, especially useful for debugging.")
def cli(verbose: bool):
    if verbose:
        click.echo("Verbose mode enabled.")
    pass


modules = [diagnostic_commands, dataset_manager_commands, model_builder_commands, utils_commands]

# Loop through the modules, binding all commands to the CLI.
for module in modules:
    for command_name in dir(module):
        command = getattr(module, command_name)
        if isinstance(command, click.Command):
            cli.add_command(command)
