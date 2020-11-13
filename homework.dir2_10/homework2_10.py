import os


def create_a_testing_work_environment(initial_directory_path):
    os.mkdir(os.path.join(initial_directory_path, "Test"))
    with open(os.path.join(initial_directory_path, "Test", "File_1.txt"), "w"):
        pass
    with open(os.path.join(initial_directory_path, "Test", "File_2.txt"), "w"):
        pass
    os.mkdir(os.path.join(initial_directory_path, "Test", "Dir_1"))
    os.mkdir(os.path.join(initial_directory_path, "Test", "Dir_2"))
    with open(os.path.join(initial_directory_path, "Test","Dir_1", "File_3.txt"), "w"):
        pass
    with open(os.path.join(initial_directory_path, "Test","Dir_1", "File_4.txt"), "w"):
        pass
    os.mkdir(os.path.join(initial_directory_path, "Test", "Dir_1", "Dir_3"))
    with open(os.path.join(initial_directory_path, "Test", "Dir_1", "Dir_3", "File_5.txt"), "w"):
        pass
    with open(os.path.join(initial_directory_path, "Test", "Dir_1", "Dir_3", "File_6.txt"), "w"):
        pass
    os.mkdir(os.path.join(initial_directory_path, "Test", "Dir_1", "Dir_3", "Dir_4"))
    os.mkdir(os.path.join(initial_directory_path, "Test", "Dir_1", "Dir_3", "Dir_5"))
    with open(os.path.join(initial_directory_path, "Test", "Dir_1", "Dir_3", "Dir_4", "File_7.txt"), "w"):
        pass
    with open(os.path.join(initial_directory_path, "Test", "Dir_2", "File_8.txt"), "w"):
        pass
    os.mkdir(os.path.join(initial_directory_path, "Test", "Dir_2", "Dir_6"))
    os.mkdir(os.path.join(initial_directory_path, "Test", "Dir_2", "Dir_7"))
    with open(os.path.join(initial_directory_path, "Test", "Dir_2", "Dir_6", "File_9.txt"), "w"):
        pass
    with open(os.path.join(initial_directory_path, "Test", "Dir_2", "Dir_6", "File_10.txt"), "w"):
        pass
    with open(os.path.join(initial_directory_path, "Test", "Dir_2", "Dir_7", "File_11.txt"), "w"):
        pass


#create_a_testing_work_environment("/Users/User/Desktop/")


def delete_all_the_files_and_directories_recursively(directory):
    if not delete_all_the_files_and_directories_recursively.path:
        delete_all_the_files_and_directories_recursively.path += directory
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            os.remove(os.path.join(directory, path))
            if len(os.listdir(directory)) == 0 and directory != delete_all_the_files_and_directories_recursively.path:
                os.rmdir(directory)
        elif os.path.isdir(os.path.join(directory, path)):
            if len(os.listdir(os.path.join(directory, path))) == 0:
                os.rmdir(os.path.join(directory, path))
            else:
                delete_all_the_files_and_directories_recursively(os.path.join(directory, path))


delete_all_the_files_and_directories_recursively.path = ""
#delete_all_the_files_and_directories_recursively("/Users/User/Desktop/Test")

