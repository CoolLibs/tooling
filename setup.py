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

def copy_clang_format():
    copy_file_to_parent_directory(".clang-format")

def copy_clang_tidy():
    copy_file_to_parent_directory(".clang-tidy")

copy_clang_format()
copy_clang_tidy()