[![Build Status](https://travis-ci.org/fogo/conan-ogg.svg)](https://travis-ci.org/fogo/conan-ogg)
[![Build status](https://ci.appveyor.com/api/projects/status/n3kftilciv1di9kq?svg=true)](https://ci.appveyor.com/project/fogo/conan-ogg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Ogg container format library package

[Conan.io](https://conan.io) package for [Ogg container format library](https://www.xiph.org/ogg/)

The packages generated with this **conanfile** can be found in [Bintray](TODO).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload ogg/1.3.3@fogo/stable --all

## Reuse the packages

### Basic setup

    $ conan install ogg/1.3.3@fogo/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    ogg/1.3.3@fogo/stable

    [options]
    ogg:shared=True # False by default

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

### License
[MIT](LICENSE)
