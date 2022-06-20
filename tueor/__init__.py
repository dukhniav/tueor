# pylint: disable=broad-except
"""
Tueor - personal finance manager
"""

__version__ = "develop"
__logger__ = "tueor"

if __version__ == "develop":

    try:
        import subprocess

        __version__ = "develop-" + subprocess.check_output(
            ["git", "log", '--format="%h"', "-n 1"], stderr=subprocess.DEVNULL
        ).decode("utf-8").rstrip().strip('"')

    except Exception:  # pragma: no cover
        # git not available, ignore
        try:
            # Try Fallback to tueor_commit file
            from pathlib import Path

            versionfile = Path("./tueor_commit")
            if versionfile.is_file():
                __version__ = f"docker-{versionfile.read_text()[:8]}"
        except Exception:
            pass
