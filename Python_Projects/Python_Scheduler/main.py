import argparse
import sys
from enum import IntEnum
import re
from pathlib import Path
import os
import subprocess


class Exit_Codes(IntEnum):
    SUCCESS = 0
    INVALID_INPUTS = 10
    PATH_NOT_FOUND = 20
    PATH_IS_DIR = 21
    PATH_EXECUTABLE = 30
    GIT_BASH_NOT_FOUND = 31
    PATH_NOT_EXECUTABLE = 32


class Python_Scheduler:
    def __init__(self):
        pass

    def get_input(self):
        num: int = len(sys.argv) - 1
        if num != 0:
            script_path = sys.argv[1]
            interval = sys.argv[2]

        else:
            script_path: str = input(f'Enter Bash Script Path: ')
            interval: str = input(f'Enter Task Interval: ')

        return script_path, interval

    def validate_inputs(self, script_path: str, interval: str):
        script_path, interval = script_path.strip(), interval.strip()
        if not interval or interval == '0':
            error_code: Exit_Codes = Exit_Codes.INVALID_INPUTS
            self.log_run(error_code)
            sys.exit(error_code)

        if not re.fullmatch(r"^\d+$", interval):
            error_code: Exit_Codes = Exit_Codes.INVALID_INPUTS
            self.log_run(error_code)
            sys.exit(error_code)

        interval_int = int(interval)

        if not script_path:
            error_code: Exit_Codes = Exit_Codes.INVALID_INPUTS
            self.log_run(error_code)
            sys.exit(error_code)

        path = Path(script_path).expanduser().resolve()

        if not path.exists():
            error_code: Exit_Codes = Exit_Codes.PATH_NOT_FOUND
            self.log_run(error_code)
            sys.exit(error_code)

        if path.is_dir():
            error_code: Exit_Codes = Exit_Codes.PATH_IS_DIR
            self.log_run(error_code)
            sys.exit(error_code)

        if not os.access(path, os.X_OK):
            result_code = self.make_executable(path)
            if result_code == Exit_Codes.GIT_BASH_NOT_FOUND or result_code == Exit_Codes.PATH_NOT_EXECUTABLE:
                error_code: Exit_Codes = result_code
                self.log_run(error_code)
                sys.exit(error_code)
            else:
                return path, interval_int

    def make_executable(self, script_path):

        script_path_abs = os.path.abspath(script_path)

        git_bash_executable = "C:/Program Files/Git/bin/bash.exe"

        if not os.path.exists(git_bash_executable):
            return Exit_Codes.GIT_BASH_NOT_FOUND

        chmod_command = f"chmod +x '{script_path_abs}'"

        try:
            subprocess.run(
                [git_bash_executable, "-c", chmod_command],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            return Exit_Codes.PATH_EXECUTABLE

        except subprocess.CalledProcessError as e:
            return Exit_Codes.PATH_NOT_EXECUTABLE

    def run_scripts(self):
        pass

    def log_run(self, error_code):
        pass
