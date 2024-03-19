"""
This module includes functions for collecting system, dependency, and CUDA information, and printing out this
information.

This module draws inspiration from Pandas' util._print_versions.py module.
"""

import locale
import os
import platform
import struct
import sys
from importlib.metadata import PackageNotFoundError, version
from typing import Any

import torch


def print_version_info() -> None:
    """Print out system, dependency, and CUDA information.

    This information is valuable for debugging, and we kindly ask contributors to include
     the result when submitting a bug report.

    :return: None
    """
    print(f"\nRIA Core Version: {version('ria')}")
    print(f"Python Version: {platform.python_version()}")

    sys_info = _get_sys_info()
    cuda_info = _get_cuda_info()
    dependency_info = _get_dependency_info()
    max_len = 20

    print("\nSYSTEM")
    print("------")
    for k, v in sys_info.items():
        print(f"{k:<{max_len}}: {v}")

    print("\nCUDA")
    print("----")
    for k, v in cuda_info.items():
        print(f"{k:<{max_len}}: {v}")

    print("\nDEPENDENCIES")
    print("------------")
    for k, v in dependency_info.items():
        print(f"{k:<{max_len}}: {v}")

    print("\nPlease include the above version information in all bug reports.\n")


def _get_sys_info() -> dict[str, Any]:
    """:return: A dictionary of relevant system information."""
    uname_result = platform.uname()
    language_code, encoding = locale.getlocale()

    return {
        "commit": _get_commit_hash(),
        "python": ".".join([str(i) for i in sys.version_info]),
        "python-bits": struct.calcsize("P") * 8,
        "OS": uname_result.system,
        "OS-release": uname_result.release,
        "Version": uname_result.version,
        "machine": uname_result.machine,
        "processor": uname_result.processor,
        "byteorder": sys.byteorder,
        "LC_ALL": os.environ.get("LC_ALL"),
        "LANG": os.environ.get("LANG"),
        "LOCALE": {"language-code": language_code, "encoding": encoding},
    }


def _get_cuda_info() -> dict[str, Any]:
    """:return: A dictionary of relevant cuda information."""
    if torch.cuda.is_available():
        return {
            "available": True,
            "device": torch.cuda.get_device_name(0),
            "version": torch.version.cuda,
            "count": torch.cuda.device_count(),
            "index": torch.version.cuda,
        }

    else:
        return {"available": False, "device": None, "version": None, "count": None, "index": None}


def _get_dependency_info() -> dict[str, Any]:
    """:return: A dictionary containing project dependencies along with their respective version numbers."""
    deps = [
        # required:
        "matplotlib",
        "torch",
        "numpy",
        "pandas",
        "click",
        "dateutil",
        # install/build:
        "poetry",
        "pip",
        # test:
        "pytest",
        # docs:
        "sphinx",
        "sphinx-rtd-theme",
        "sphinx-autobuild",
        # dev:
        "flake8",
        "black",
        "isort",
        # other:
    ]

    result: dict[str, Any] = {}
    for d in deps:
        try:
            result[d] = version(d)
        except PackageNotFoundError:
            # TODO: Find dependency version information for packages without metadata.
            result[d] = "COULD NOT RESOLVE"

    return result


def _get_commit_hash() -> str:
    """
    :return: The Git commit hash of the installed instance of RIA Core.

    :raises RuntimeError: If Git is not installed or not accessible from the command line.
    """
    # TODO: Find the Git hash. Note that spawning a subprocess with the command `git rev-parse HEAD` won't work
    #  outside of the 'ria' development directory. Instead, we need to scrape it from the installed package itself.
    return "COULD NOT RESOLVE"
