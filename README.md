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
restinio/0.6.5@stiffstream/stable
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

Since v0.6.1 the usage of OpenSSL can be turned on or off by `restinio:use_openssl` option. By the default this option has `false` value, but can be changed to `true`:

```
[options]
restinio:use_openssl=true
```
If `restinio:use_openssl` is `true` the OpenSSL is automatically added to RESTinio's dependencies.

### Different versions of requirements

RESTinio can work with different versions of its requirements. For example,
http-parser version 2.8.1, 2.9.1 or 2.9.2 can be used. Or asio-1.12.2 or asio-1.1.14.0.

RESTinio's recipe for Conan fixes some versions of RESTinio's dependecies but those version can be somewhat outdated. For example, RESTinio's Conan package requires Boost-1.69, but there are more fresh versions of Boost.

So a user can have to override RESTinio's versions of requirements to more appropriate versions he/she needs:

```
[requires]
restinio/0.6.5@stiffstream/stable
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
