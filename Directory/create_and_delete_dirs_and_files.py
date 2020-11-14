import os

initial_directory_path = r'C:\Users\admin\Desktop\Python_Homewhork\Directory\test'


def create_a_testing_work_environment(initial_directory_path):
    for i in range(1, 3):
        filepath = os.path.join(initial_directory_path, 'file_' + str(i) + '.txt')
        with open(filepath, 'w'):
            pass
        os.mkdir(os.path.join(initial_directory_path, 'dir_' + str(i)))

    new_dir = os.path.join(initial_directory_path, 'dir_1')
    for i in range(3, 5):
        filepath = os.path.join(new_dir, 'file_' + str(i) + '.txt')
        with open(filepath, 'w'):
            pass
    os.mkdir(os.path.join(new_dir, 'dir_3'))
    new_dir = os.path.join(new_dir, 'dir_3')
    for i in range(4, 6):
        filepath = os.path.join(new_dir, 'file_' + str(i + 1) + '.txt')
        with open(filepath, 'w'):
            pass
        os.mkdir(os.path.join(new_dir, 'dir_' + str(i)))
    new_dir = os.path.join(new_dir, 'dir_4')
    filepath = os.path.join(new_dir, 'file_' + '7' + '.txt')
    with open(filepath, 'w'):
        pass
    new_dir = os.path.join(initial_directory_path, 'dir_2')
    filepath = os.path.join(new_dir, 'file_8' + '.txt')
    with open(filepath, 'w'):
        pass
    for i in range(6, 8):
        os.mkdir(os.path.join(new_dir, 'dir_' + str(i)))
    new_dir = os.path.join(new_dir, 'dir_6')
    for i in range(9, 11):
        filepath = os.path.join(new_dir, 'file_' + str(i) + '.txt')
        with open(filepath, 'w'):
            pass
    new_dir = os.path.join(initial_directory_path, os.path.join('dir_2', 'dir_7'))
    filepath = os.path.join(new_dir, 'file_' + '11' + '.txt')
    with open(filepath, 'w'):
        pass


# create_a_testing_work_environment(initial_directory_path)


def delete_all_the_files_and_directories_recursively(directory):
    for path in os.listdir(directory):
        new_path = os.path.join(directory, path)
        if os.path.isfile(new_path):
            os.remove(new_path)
        elif os.path.isdir(new_path):
            delete_all_the_files_and_directories_recursively(new_path)
            os.rmdir(new_path)

# delete_all_the_files_and_directories_recursively(initial_directory_path)
