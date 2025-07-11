from pathlib import Path


def read_file(filename, path):
    print((path/filename).read_text())


def write_file(filename, path):
    (path/filename).write_text('')


def main():
    try:
        path = Path()
        file_name = input("Enter the filename to open or create: ").strip()
        if (path/file_name).exists():  # checks to see if file exit if so it reads the file
            read_file(file_name, path)
        else:  # it creates a new file
            write_file(file_name, path)

        with open(f'{file_name}', 'w') as file:  # then it opens file to update it
            print("Enter your text (type SAVE on a new line to save and exit):")
            while True:
                Line_input = input("")
                if Line_input.upper() == 'SAVE':
                    break
                file.write(Line_input)
                file.write('\n')

        print(f'{file_name} saved')

    except OSError:
        print(f'{file_name} could not be opened.')


if __name__ == '__main__':
    main()
