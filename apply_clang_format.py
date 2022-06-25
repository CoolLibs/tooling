

def allowed_extensions():
    return [
        "c",
        "cpp",
        "h",
        "hpp",
        "inl",
        "tpp",
        "glsl",
        "frag",
        "vert",
        "comp",
        "geom",
        "tese",
        "tesc",
    ]


def at_least_one_file_has_extension(extension, folder):
    from pathlib import Path
    from os import listdir
    from os.path import isfile, join

    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    return any(
        map(lambda f: Path(f).suffix == f".{extension}",
            files)
    )


def run_clang_format_on_one_folder(folder):
    import os
    os.chdir(folder)
    for extension in allowed_extensions():
        if (at_least_one_file_has_extension(extension, folder)):
            os.system(f"clang-format -style=file -i *.{extension}")


def run_clang_format_on_folder(folder):
    import os
    run_clang_format_on_one_folder(folder)
    for subfolder in [x[0] for x in os.walk(folder)]:
        run_clang_format_on_one_folder(subfolder)


def parent_folder():
    from pathlib import Path
    return Path(__file__).parent.parent


def apply_clang_format_impl(folder):
    import os
    from termcolor import colored

    path = os.path.join(parent_folder(), folder)
    if (os.path.isdir(path)):
        run_clang_format_on_folder(path)
        print(colored(
            f"Applying clang-format on '{folder}' (Full path: '{path}')",
            'green'))
    else:
        print(colored(
            f"Applying clang-format on '{folder}' FAILED. We did not find '{path}'",
            'red'))


def apply_clang_format(folder):
    apply_clang_format_impl(folder)


if __name__ == '__main__':
    apply_clang_format('src')
    apply_clang_format('res')
    apply_clang_format('test')
    apply_clang_format('tests')
    apply_clang_format('example')
    apply_clang_format('examples')
