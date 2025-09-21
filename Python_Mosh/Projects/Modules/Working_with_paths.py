from pathlib import Path

# Path(r"C:\Program Files\Microsoft")  # Absolute path
# Path()  # Path object of current directory ie Modules directory
# Path("ecommerce/__init__.py")  # relative path
# Path() / "ecommerce"/"__init__.py"
# Path.home()  # path of home directory

path = Path("ecommerce/__init__.py")
path.exists()  # checks if path exits
path.is_file()  # checks if path is a file
path.is_dir()  # checks if path is a directory

# Methods
print(path.name)  # returns file or directory name
print(path.stem)  # returns file name without the extension
print(path.suffix)  # returns extension of file
print(path.parent)  # returns parent of file


# creates a new path based on the existing path with name of file changed
path = path.with_name('file.txt')
print(path)
print(path.absolute())  # gets the absolute path


path = path.with_suffix('.txt')  # same as above
print(path)
