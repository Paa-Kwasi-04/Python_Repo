import subprocess


result = subprocess.run(['ls', '-l'])
print(type(result))
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen
