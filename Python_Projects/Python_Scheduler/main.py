import argparse
import sys
from enum import IntEnum
import re
from pathlib import Path
import os
import subprocess
from datetime import datetime
import logging


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
        self.LOG_FILE_NAME = 'scheduler_run.log'
        self.__init__logging()

    def __init__logging(self):
        logging.basicConfig(
            filename=self.LOG_FILE_NAME,
            level=logging.INFO,  # Sets the minimum log level to capture
            format='%(message)s'  # We will use our own formatter
        )
        self.logger = logging.getLogger(__name__)

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
            self.log_run(f"ERROR: Invalid interval provided: '{interval}'", level=logging.ERROR)
            sys.exit(Exit_Codes.INVALID_INPUTS)

        interval_int = int(interval)

        if not script_path:
            self.log_run(f"ERROR: Invalid script_path provided: '{script_path}'", level=logging.ERROR)
            sys.exit(Exit_Codes.INVALID_INPUTS)

        path = Path(script_path).expanduser().resolve()

        if not path.exists():
            self.log_run(f"ERROR: Path not found: '{script_path}'", level=logging.ERROR)
            sys.exit(Exit_Codes.PATH_NOT_FOUND)

        if path.is_dir():
            self.log_run(f"ERROR: Path is a directory: '{script_path}'", level=logging.ERROR)
            sys.exit(Exit_Codes.PATH_IS_DIR)

        # If file is already executable (POSIX bit) or on Windows assume ok if file exists
        if os.access(path, os.X_OK):
            return path, interval_int

        # Attempt to make executable via git bash chmod (if available)
        result_code = self.make_executable(path)
        if result_code == Exit_Codes.GIT_BASH_NOT_FOUND:
            self.log_run("ERROR: Git Bash executable not found.", level=logging.ERROR)
            sys.exit(result_code)
        elif result_code == Exit_Codes.PATH_NOT_EXECUTABLE:
            self.log_run(f"ERROR: Failed to make script executable: '{script_path}'", level=logging.ERROR)
            sys.exit(result_code)
        else:
            self.log_run(f"INFO: Successfully made script executable: '{script_path}'", level=logging.INFO)
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

        except subprocess.CalledProcessError:
            return Exit_Codes.PATH_NOT_EXECUTABLE

    def run_scripts(self, script_path, log_filename):
        start_time = datetime.now()
        timeout = 600  # seconds
        git_bash_executable = self.GIT_BASH_EXECUTABLE

        if not os.path.exists(git_bash_executable):
            return {
                'Script': script_path,
                'start_time': start_time,
                'end_time': datetime.now(),
                'duration': (datetime.now() - start_time).total_seconds(),
                'stdout': '',
                'stderr': 'Git Bash executable not found.',
                'exit_code': Exit_Codes.GIT_BASH_NOT_FOUND
            }

        try:
            completed = subprocess.run(
                [git_bash_executable, "-c", str(script_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=timeout,
                check=True
            )
            stdout = completed.stdout
            stderr = completed.stderr
            exit_code = Exit_Codes.SUCCESS if completed.returncode == 0 else completed.returncode

        except subprocess.TimeoutExpired as e:
            stdout = e.stdout or ''
            stderr = (e.stderr or '') + "\nProcess timed out."
            exit_code = Exit_Codes.PROCESS_TIMEOUT

        except subprocess.CalledProcessError as e:
            stdout = e.stdout or ''
            stderr = e.stderr or ''
            # preserve the underlying return code if useful
            exit_code = Exit_Codes.PROCESS_CLOSED

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        params = {
            'Script': script_path,
            'start_time': start_time,
            'end_time': end_time,
            'duration': duration,
            'stdout': stdout,
            'stderr': stderr,
            'exit_code': exit_code
        }

        return params

    def log_msg_formatter(self, params: dict):
        # use imported datetime
        timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        start_str = params['start_time'].strftime("%Y-%m-%d %H:%M:%S") if hasattr(params['start_time'], 'strftime') else str(params['start_time'])
        end_str = params['end_time'].strftime("%Y-%m-%d %H:%M:%S") if hasattr(params['end_time'], 'strftime') else str(params['end_time'])

        exit_val = params['exit_code'].value if isinstance(params['exit_code'], Exit_Codes) else params['exit_code']
        exit_name = params['exit_code'].name if isinstance(params['exit_code'], Exit_Codes) else str(params['exit_code'])

        log_message = (
            "------------------------------------------------------------\n"
            f"Script: {str(params['Script'])}  Timestamp: {timestamp_str}\n"
            f"Start: {start_str}\n"
            f"End:   {end_str}\n"
            f"Duration: {params['duration']}\n"
            f"Exit Code: {exit_val}   ({exit_name})\n\n"
            f"STDOUT:\n{params['stdout']}\n\n"
            f"STDERR:\n{params['stderr']}\n"
        )

        return log_message

    def log_run(self, log_message,level=logging.INFO):

        if level == logging.ERROR:
            self.logger.error(log_message)
        elif level == logging.WARNING:
             self.logger.warning(log_message)
        else:
            self.logger.info(log_message)

        # You can optionally print to console at the same time:
        print(log_message)

