from pathlib import Path
from zipfile import ZipFile


# with ZipFile('files.zip', 'w') as zip:
#     for path in Path('ecommerce').rglob('*.*'):
#         zip.write(path)

# with ZipFile('files.zip') as zip:
#     print(zip.namelist())  # list of the names of files in zip
#     info = zip.getinfo('ecommerce/__init__.py')  # gets info on file
#     print(info.file_size)
#     print(info.compress_size_size)

#     # extracts content of zip file to the named directory
#     zip.extractall('extract')

path = Path()/'Working_with_Sql.py'

path.write_text('....')
