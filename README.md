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
restinio/0.4.9@stiffstream/stable
```
RESTinio will use standalone version of Asio by default.

3. Install dependencies for your project:
```bash
conan install SOME_PATH --build=missing
```

### Usage of Boost.Asio

It you want to use RESTinio with Boost.Asio you have to:

a) add Boost to your `conanfile.txt`:
```
[requires]
restinio/0.4.9@stiffstream/stable
boost/1.68.0@conan/stable
```
b) specify `boost_libs` option for RESTinio. This option should have `static` or `shared`. If you use `static` value then you should specify `shared=False` option for Boost libraries:
```
[options]
restinio:boost_libs=static
boost:shared=False
```
If you use `shared` value for `restinio:boost_libs` then you should specify `shared=True` option for Boost libraries:
```
[options]
restinio:boost_libs=shared
boost:shared=True
```

### Usage of OpenSSL

Since Nov 2019 the usage of OpenSSL can be turned off by `restinio:use_openssl` option. By the default this option has `true` value, but can be changed to `false`:

```
[options]
restinio:use_openssl=false
```

## Adding RESTinio To Your CMakeLists.txt

Please note that SObjectizer should be added to your CMakeLists.txt via `find_package` command:
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
