# tooling

Here are all the common things that we use when writing code.

You can simply run *setup.py* to setup everything automatically.<br/>
Currently this script does:
- copy *.clang-format* to the parent directory
- copy *.clang-tidy* to the parent directory

## Formater

We use *ClangFormat* as our [formatting tool](https://julesfouchy.github.io/Learn--Clean-Code-With-Cpp/lessons/formatting-tool/) and we provide a *.clang-format* file to configure it.

## Static analyser

We use *ClangTidy* as our [static analysis tool](https://julesfouchy.github.io/Learn--Clean-Code-With-Cpp/lessons/static-analysers/) and we provide a *.clang-tidy* file to configure it.