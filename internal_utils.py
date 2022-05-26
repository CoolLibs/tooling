def current_folder():
    from pathlib import Path
    return Path(__file__).parent

def parent_folder():
    from pathlib import Path
    return Path(__file__).parent.parent

def copy_file_to_parent_directory(file_name):
    import shutil
    import os
    shutil.copyfile(os.path.join(current_folder(), file_name),
                    os.path.join(parent_folder(),  file_name))

def make_directory_if_necessary(path):
    import os
    if not os.path.exists(path):
        os.mkdir(path)