# flydoc

## Information

the flydoc is an documentation generator that uses a simple folder structure and Markdown files to create custom documentation. it is writed by python that can be compiled on windows and linux, and we pack a exe file to help use easily.

## Features

1. the templates are writed by bootstrap, the users can modify it easily.

2. support the style of github markdown.

3. support the more beautiful table mark.

4. support custom the config file. of course, it can work normally with no config file.

5. support the code syntax highlighting.

6. supports unlimited hierarchical directory.

## Folder Structure

by default, the flydoc will find the `/docs` folder to build the markdown file. if you don't want to use the default folder, that can transfer an parameter to specify the document folder. normally, the folder structure is like that:

    docs
        1.examplemarkdown.md
        2.markdown2-.md
        subfolder
            1.markdownfile.md
            2.file2-.md
            3.file3.md
    config.json
    flydoc.exe


if you don't use flydoc.exe, and use `python main.py [inputfolder] [outputfolder]` command to complie. the folder structure is like that:

    common
    themes
    docs
        1.examplemarkdown.md
        2.markdown2-.md
        subfolder
            1.markdownfile.md
            2.file2-.md
            3.file3.md
    __init__.py
    config.json
    main.py

## Install

1. download the sources from  github.

2. install the dependence.

    pip install simplejson codecs shutil markdown Jinja2

## Usage

1. use the flydoc.exe

    flydoc.exe [inputfolder] [outputfolder]

2. use the sources.

    python main.py [inputfolder] [outputfolder]

## Configuration

```javascript
{
"title": "",
"author": "",
"description": "",
"headers": [
    {"name": "the header nav title", "url": "the url"}
],
"theme": "default",
"catalog": true,

// support regex
"ignore": {
    "files": [],
    "folders": []
}
}
```

## Thanks

the idea is inspired by these projects:

1. [Daux.io](https://github.com/justinwalsh/daux.io)

2. [doxmate](https://github.com/JacksonTian/doxmate)

3. [readthedocs.org](https://github.com/rtfd/readthedocs.org)



