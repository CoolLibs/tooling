# ---HOW TO---
# Create one function per file you want to generate. The file will have the same name as the function.
# Each function should compute and return the content of the corresponding file as a string.
# Then call `generate`:
# ```python
# def some_function_that_will_generate_a_file():
#     return "The content of the file"
#
# def another_function():
#     return "Another file"
#
# generate(
#     folder="generated", # The name of the output folder where the files will be generated. /!\ Don't put anything manually in that folder, it is erased and regenerated each time you call `generate()`.
#     files=[
#         some_function_that_will_generate_a_file,
#         another_function,
#     ]
# )
# ```
# ------------

def clear_generated_folder(path_relative_to_project_root):
    import shutil
    import os
    folder = output_folder(path_relative_to_project_root)
    if (os.path.isdir(folder)):
        shutil.rmtree(folder)
    os.makedirs(folder)


def output_folder(path_relative_to_project_root):
    import os
    import sys
    from pathlib import Path
    root_folder = Path(sys.argv[0]).parent
    return os.path.join(root_folder, path_relative_to_project_root)


def generate_one(function, path_relative_to_project_root):
    generate_file(function.__name__, function(), path_relative_to_project_root)


def generate_file(name, content, path_relative_to_project_root):
    import os
    with open(os.path.join(output_folder(path_relative_to_project_root), name) + ".inl", 'w') as f:
        f.write(heading(name) + content)


def heading(function_name):
    import os
    import sys
    return f"""/* -----------------------------------------------------------------------------
 * This file was automatically generated by a Python script.
 * PLEASE DON'T EDIT IT DIRECTLY, your changes would be overwritten the next time the script is run.
 * Instead, go to "{os.path.basename(sys.argv[0])}" and edit the "{function_name}" function there.
 * -----------------------------------------------------------------------------
 */
"""


def generate(folder="generated", files=[]):
    clear_generated_folder(folder)
    for function in files:
        generate_one(function, folder)