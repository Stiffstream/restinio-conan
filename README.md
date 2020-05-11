# restinio-conan
This is Conan package for [RESTinio](https://stiffstream.com/en/products/restinio.html) framework.

# How To Use

## Installing Via Conan

To use RESTinio via Conan it is necessary to do the following steps:

1. Add the corresponding remote to your conan:

```bash
conan remote add stiffstream https://api.bintray.com/conan/stiffstream/public
```
It can be also necessary to add public-conan remote:
```bash
conan remote add public-conan https://api.bintray.com/conan/bincrafters/public-conan  
```

2. Add RESTinio to `conanfile.txt` of your project:
```
[requires]
restinio/0.6.7@stiffstream/stable
```
RESTinio will use standalone version of Asio by default.

3. Install dependencies for your project:
```bash
conan install SOME_PATH --build=missing
```

### Usage of Boost.Asio

It you want to use RESTinio with Boost.Asio you can do so by configuring the options `restinio:boost_libs` in your `conanfile.txt`:
```
[options]
restinio:boost_libs=static
```
Or if you wish to link dynamically:
```
[options]
restinio:boost_libs=shared
```

### Usage of OpenSSL

Since v0.6.1 the usage of OpenSSL can be turned on or off by `restinio:use_openssl` option. By the default this option has `false` value, but can be changed to `true`:

```
[options]
restinio:use_openssl=true
```
If `restinio:use_openssl` is `true` the OpenSSL is automatically added to RESTinio's dependencies.

### Usage of fmtlib

Since v0.6.6 RESTinio allows to use fmtlib in header-only or compiled form.

By the default fmtlib is used in the compiled form. If header-only version of fmtlib is needed then it can be forced by:

```
[options]
restinio:fmt_header_only=true
```

### Different versions of requirements

RESTinio can work with different versions of its requirements. For example,
http-parser version 2.8.1, 2.9.1 or 2.9.2 can be used. Or asio-1.12.2 or asio-1.1.14.0.

RESTinio's recipe for Conan fixes some versions of RESTinio's dependecies but those version can be somewhat outdated. For example, RESTinio's Conan package requires Boost-1.69, but there are more fresh versions of Boost.

So a user can have to override RESTinio's versions of requirements to more appropriate versions he/she needs:

```
[requires]
restinio/0.6.7@stiffstream/stable
boost/1.72.0
```

## Adding RESTinio To Your CMakeLists.txt

Please note that RESTinio should be added to your CMakeLists.txt via `find_package` command:
```cmake
...
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(restinio CONFIG REQUIRED)
...
target_link_libraries(your_target restinio::restinio)
target_link_libraries(your_target ${CONAN_LIBS})
```

# Some Notes

If you have any questions about RESTinio feel free to ask us via `info at stiffstream dot com`.

If you have some problems with RESTinio or this conan-recipe please open an [issue](https://github.com/Stiffstream/restinio-conan/issues).
