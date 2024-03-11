"""
This module contains all the CLI bindings for the diagnostics package.
"""
import click

from ria import print_version_info as print_version_info


@click.command(help="Print out system, dependency, and CUDA version information.")
def version():
    print_version_info()
