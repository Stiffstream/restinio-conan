from conans import ConanFile, CMake, tools
import os


class RestinioConan(ConanFile):
    name = "restinio"
    version = "0.6.6"

    license = "BSD-3-Clause"
    url = "https://github.com/Stiffstream/restinio-conan"

    description = (
            "RESTinio is a header-only C++14 library that gives you "
            "an embedded HTTP/Websocket server."
    )

    settings = "os", "compiler", "build_type", "arch"
    options = {'boost_libs': ['none', 'static', 'shared'],
               'use_openssl': ['false', 'true'],
               'fmt_header_only': ['false', 'true']}
    default_options = {'boost_libs': 'none',
                       'use_openssl': 'false',
                       'fmt_header_only': 'false'}
    generators = "cmake"
    source_subfolder = "restinio"
    build_policy = "missing"

    def requirements(self):
        self.requires.add("http_parser/2.9.2")
        self.requires.add("fmt/6.1.2")
        self.requires("expected-lite/0.4.0")
        self.requires("optional-lite/3.2.0")
        self.requires("string-view-lite/1.3.0")
        self.requires("variant-lite/1.2.2")
        if self.options.fmt_header_only == "true":
            self.options["fmt"].header_only = True
        else:
            self.options["fmt"].header_only = False

        if self.options.boost_libs == "none":
            self.requires.add("asio/1.12.2")
        else:
            self.requires.add("boost/1.69.0")
            if self.options.boost_libs == "shared":
                self.options["boost"].shared = True
            else:
                self.options["boost"].shared = False
                
        if self.options.use_openssl == "true":
            self.requires.add("openssl/1.1.1d")

    def source(self):
        source_url = "https://github.com/Stiffstream/restinio/releases/download/"
        tools.get("{0}v.{1}/restinio-{1}.zip".format(source_url, self.version))
        extracted_dir = "restinio-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['RESTINIO_INSTALL'] = True
        cmake.definitions['RESTINIO_FIND_DEPS'] = False
        cmake.definitions['RESTINIO_USE_BOOST_ASIO'] = self.options.boost_libs
        cmake.definitions['RESTINIO_FMT_HEADER_ONLY'] = self.options.fmt_header_only
        cmake.definitions['RESTINIO_USE_EXTERNAL_EXPECTED_LITE'] = True
        cmake.definitions['RESTINIO_USE_EXTERNAL_OPTIONAL_LITE'] = True
        cmake.definitions['RESTINIO_USE_EXTERNAL_STRING_VIEW_LITE'] = True
        cmake.definitions['RESTINIO_USE_EXTERNAL_VARIANT_LITE'] = True
        cmake.configure(source_folder = self.source_subfolder + "/dev/restinio")
        return cmake

    def package(self):
        self.copy(src=self.source_subfolder, pattern="LICENSE*", dst="licenses")
        cmake = self._configure_cmake()
        self.output.info(cmake.definitions)
        cmake.install()

    def package_info(self):
        self.info.header_only()
        self.cpp_info.defines.extend(["RESTINIO_EXTERNAL_EXPECTED_LITE", "RESTINIO_EXTERNAL_OPTIONAL_LITE",
                                      "RESTINIO_EXTERNAL_STRING_VIEW_LITE", "RESTINIO_EXTERNAL_VARIANT_LITE"])
        if self.options.boost_libs != "none":
            self.cpp_info.defines.append("RESTINIO_USE_BOOST_ASIO")
