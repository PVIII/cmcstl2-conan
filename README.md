# cmcstl2-conan

[![Build Status](https://travis-ci.com/PVIII/cmcstl2-conan.svg?branch=master)](https://travis-ci.com/PVIII/cmcstl2-conan)

Conan packaging of Casey Carters [Ranges TS](https://en.cppreference.com/w/cpp/experimental/ranges) implementation.

## Getting Started

This library requires C++17 and the Concepts TS. It currently compiles only with GCC 8+.
This is a header-only library.

### Installing

You can just download or clone the library and set your include directory to `include`.

If you use [Conan](https://conan.io/) you can add the Conan remote
```
conan remote add <REMOTE> https://api.bintray.com/conan/pviii/conan
```
and reference the package `cmcstl2/x@pviii/stable` as a dependency.

## Built With

* [CMake](https://cmake.org/) - Build System (Generator)
* [Conan](https://conan.io/) - Dependency Management
* [Bintray](https://bintray.com) - Package Hosting

## Versioning

This package is not versioned upstream. The Conan package uses the short Git hash for its version. This might change in the future.

## License

Parts of this project are licensed under the
* MIT License,
* Boost Software License - Version 1.0,
* libc++ License,
* University of Illinois/NCSA Open Source License,
* Stepanov and McJones, "Elements of Programming" license and the
* SGI C++ Standard Template Library license.

See the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgements

* Casey Carter
* Eric Niebler

