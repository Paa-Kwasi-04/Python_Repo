from pathlib import Path
from time import ctime  # give human readable creation time of a file
import shutil


# for copying for content to another place
path = Path('ecommerce/__init__.py')
target = Path()/'__init__.py'

target.write_text(path.read_text())

# Or to copy content
shutil.copy(path, target)


# path.exists()
# path.rename('init.txt')
# path.unlink() # removes files like how rmdkir would for directories
# print(ctime(path.stat().st_ctime))   # returns info about the file

# path.read_bytes()  # returns data as a binary object


# print(path.read_text())  # returns text in the file

# # this is way better than

# # with open('__init__.py','r') as file:
# #     pass

# # since it takes care of close and releasing resources as well

# path.write_text('Some string')
# path.write_bytes() # oens file to  be written to in byte mode
