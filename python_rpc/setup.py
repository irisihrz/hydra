from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["libtorrent"],
    "build_exe": "hydra-python-rpc",
}

# Windows-specific options
if sys.platform == "win32":
    build_exe_options["include_msvcr"] = True

setup(
    name="hydra-python-rpc",
    version="0.1",
    description="Hydra",
    options={"build_exe": build_exe_options},
    executables=[Executable(
      "main.py",
      target_name="hydra-python-rpc",
      icon="build/icon.ico" if sys.platform == "win32" else None
    )]
)
