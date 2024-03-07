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
import torch

from importlib.metadata import version, PackageNotFoundError
from typing import Any


def print_version_info() -> None:
    """Print out system, dependency, and CUDA information.

    This information is valuable for debugging, and we kindly ask contributors to include
     the result when submitting a bug report.

    :return: None
    """
    print(f"\nRIA Core Version: {version('ria')}")

    sys_info = _get_sys_info()
    cuda_info = _get_cuda_info()
    dependency_info = _get_dependency_info()

    print("\nSYSTEM")
    print("------")
    max_len = max(len(x) for x in sys_info)
    for k, v in sys_info.items():
        print(f"{k:<{max_len}}: {v}")

    print("\nCUDA")
    print("----")
    max_len = max(len(x) for x in cuda_info)
    for k, v in cuda_info.items():
        print(f"{k:<{max_len}}: {v}")

    print("\nDEPENDENCIES")
    print("------------")
    max_len = max(len(x) for x in dependency_info)
    for k, v in dependency_info.items():
        print(f"{k:<{max_len}}: {v}")

    print("\nPlease include the above version information in all bug reports.\n")


def _get_sys_info() -> dict[str, Any]:
    """ :return: A dictionary of relevant system information. """
    uname_result = platform.uname()
    language_code, encoding = locale.getlocale()

    return {
        "commit": "",  # TODO: Get commit hash.
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
    """:return: A dictionary of relevant cuda information. """
    if torch.cuda.is_available():
        return {
            "available": True,
            "device": torch.cuda.get_device_name(0),
            "version": torch.version.cuda,
            "count": torch.cuda.device_count(),
            "index": torch.version.cuda
        }

    else:
        return {
            "available": False,
            "device": None,
            "version": None,
            "count": None,
            "index": None
        }


def _get_dependency_info() -> dict[str, Any]:
    """:return: A dictionary containing project dependencies along with their respective version numbers. """
    deps = [
        # required:
        "matplotlib",
        "torch",
        "dateutil",
        # install/build:
        "poetry"
        "pip",
        # test:
        "pytest",
        # docs:
        "sphinx",
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
