
class Directory():
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.subdirectories = []
        self.file_sizes = 0

    def add_file_size(self, file_size):
        self.file_sizes += file_size

    def add_subdirectory(self, directory):
        self.subdirectories.append(directory)

    def get_size(self):
        subdirectory_sizes = 0
        for subdirectory in self.subdirectories:
            subdirectory_sizes += subdirectory.get_size()
        return self.file_sizes + subdirectory_sizes

def main():
    with open('data/day07_commands.data') as f:
        result = 0
        row = next(f)
        current_directory = Directory('/')
        for row in f:
            if row.startswith('$ ls'):
                continue
            elif row.startswith('dir'):
                continue
            elif row.startswith('$ cd ..'):
                current_directory = current_directory.parent
            elif row.startswith('$ cd'):
                directory_name = row[5:-1]
                directory = Directory(directory_name, current_directory)
                current_directory.add_subdirectory(directory)
                current_directory = directory
            else:
                file_size = int(row.split(' ')[0])
                current_directory.add_file_size(file_size)

            print('loop')


    print(f"answer: {result}")

if __name__ == "__main__":
    main()