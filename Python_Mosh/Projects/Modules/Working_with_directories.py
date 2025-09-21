from pathlib import Path

path = Path('ecommerce')

# path.exits()
# path.mkdir()  # creates the directory
# path.rmdir() # removes the directory
# path.rename('ecommerce2') # rename the directory

# iterdir returns a generator object of the list of flies and directories in the given directory
paths = [p for p in path.iterdir() if p.is_dir]

# glob() is similar to iterdir but better if you are looking a pattern in files and for recursive
pyfiles = [p for p in path.glob('*.py')]  # * means all files with .py
# rglob recursively checks director and  all its sub directories for the pattern
pyfiles_1 = [p for p in path.rglob('*.py')]

print(paths)
print(pyfiles)
print(pyfiles_1)
