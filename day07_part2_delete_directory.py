class DirectoryRepository():
    def __init__(self) -> None:
        self.directories = []

    def add_directory(self, directory):
        self.directories.append(directory)


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
    directory_repository = DirectoryRepository()
    root_directory = None
    with open('data/day07_commands.data') as f:
        row = next(f)
        current_directory = Directory('/')
        directory_repository.add_directory(current_directory)
        root_directory = current_directory
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
                directory_repository.add_directory(directory)
                current_directory.add_subdirectory(directory)
                current_directory = directory
            else:
                file_size = int(row.split(' ')[0])
                current_directory.add_file_size(file_size)
            pass

    TOTAL_DISK_SPACE = 70000000
    MINIMUM_SPACE_REQUIRED = 30000000
    ADDITIONAL_SPACE_NEEDED = MINIMUM_SPACE_REQUIRED - (TOTAL_DISK_SPACE - root_directory.get_size())
    smallest_directory_size_to_delete = float('inf')

    for directory in directory_repository.directories:
        directory_size = directory.get_size()
        if directory_size < ADDITIONAL_SPACE_NEEDED:
            continue
        if directory_size < smallest_directory_size_to_delete:
            smallest_directory_size_to_delete = directory_size



    # with open('day07_directories', 'w') as f:
    #     for directory in directory_repository.directories:
    #         f.write(f'{directory.name} - {directory.get_size()}\n')


    print(f"answer: {smallest_directory_size_to_delete}")

if __name__ == "__main__":
    main()

# 1265003 too low
# 1667443
# problem pwcvj
# pwcvj - 292769