import argparse
import sys
from enum import IntEnum
import re
from pathlib import Path
import os
import subprocess
from datetime import datetime


class Exit_Codes(IntEnum):
    SUCCESS = 0
    INVALID_INPUTS = 10
    PATH_NOT_FOUND = 20
    PATH_IS_DIR = 21
    PATH_EXECUTABLE = 30
    GIT_BASH_NOT_FOUND = 31
    PATH_NOT_EXECUTABLE = 32
    PROCESS_TIMEOUT = 40
    PROCESS_CLOSED = 41


class Python_Scheduler:
    
    def __init__(self):
        self.GIT_BASH_EXECUTABLE = r"C:\Program Files\Git\bin\bash.exe"

    def get_input(self):
        if len(sys.argv) >= 3:
            script_path = sys.argv[1]
            interval = sys.argv[2]

        else:
            script_path: str = input(f'Enter Bash Script Path: ')
            interval: str = input(f'Enter Task Interval: ')

        return script_path, interval

    def validate_inputs(self, script_path: str, interval: str):
        script_path, interval = script_path.strip(), interval.strip()
        if not interval or interval == '0' or not re.fullmatch(r"^\d+$", interval):
            self.log_run(Exit_Codes.INVALID_INPUTS)
            sys.exit(Exit_Codes.INVALID_INPUTS)

        interval_int = int(interval)

        if not script_path:
            self.log_run(Exit_Codes.INVALID_INPUTS)
            sys.exit(Exit_Codes.INVALID_INPUTS)

        path = Path(script_path).expanduser().resolve()

        if not path.exists():
            self.log_run(Exit_Codes.PATH_NOT_FOUND)
            sys.exit(Exit_Codes.PATH_NOT_FOUND)

        if path.is_dir():
            self.log_run(Exit_Codes.PATH_IS_DIR)
            sys.exit(Exit_Codes.PATH_IS_DIR)

        if not os.access(path, os.X_OK):
            result_code = self.make_executable(path)
            if result_code == Exit_Codes.GIT_BASH_NOT_FOUND or result_code == Exit_Codes.PATH_NOT_EXECUTABLE:
                self.log_run(result_code)
                sys.exit(result_code)
            else:
                return path, interval_int

    def make_executable(self, script_path:Path):

        script_path_abs = str(script_path.resolve())

        git_bash_executable = self.GIT_BASH_EXECUTABLE
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

    def run_scripts(self,script_path,log_filename):
        start_time =  datetime.now()
        timeout = 600
        stdout = ''
        stderr = ''
        exit_code = ''
        git_bash_executable = self.GIT_BASH_EXECUTABLE

        if not os.path.exists(git_bash_executable):
            return Exit_Codes.GIT_BASH_NOT_FOUND


        try:
            process = subprocess.Popen(
                [git_bash_executable, "-c", script_path],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            try:
                stdout,stderr = process.communicate(timeout=timeout)
                exit_code = process.returncode
            except subprocess.TimeoutExpired as e:
                process.kill()
                stdout,stderr = process.communicate()
                exit_code = Exit_Codes.PROCESS_TIMEOUT
        except subprocess.CalledProcessError as e:
            stdout = e.stdout
            stderr = e.stderr
            exit_code = Exit_Codes.PROCESS_CLOSED

        stdout = process.stdout
        stderr = process.stderr
        exit_code = Exit_Codes.SUCCESS
        end_time = datetime.now()

        duration = start_time - end_time

        params = {
            'start_time':start_time,
            'end_time':end_time,
            'duration':duration,
            'stdout':stdout,
            'stderr':stderr,
            'exit_code':exit_code
        }

        log_message = self.log_formatter(params=params)

    def log_formatter(self,params:dict):
        pass

    def log_run(self, error_code):
        pass
