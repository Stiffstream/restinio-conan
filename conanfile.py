from conans import ConanFile, CMake, tools
import os


class SobjectizerConan(ConanFile):
    name = "restinio"
    version = "0.4.8.6"

    license = "BSD-3-Clause"
    url = "https://github.com/Stiffstream/restinio-conan"

    description = (
            "RESTinio is a header-only C++14 library that gives you "
            "an embedded HTTP/Websocket server."
    )

    settings = "os", "compiler", "build_type", "arch"

    options = {'boost_libs': ['none', 'static', 'shared']}
    default_options = {'boost_libs': 'none'}

    requires = "http-parser/2.8.1@bincrafters/stable", "asio/1.12.0@bincrafters/stable", "fmt/5.3.0@bincrafters/stable"

    generators = "cmake"

    source_subfolder = "restinio"

    def source(self):
        source_url = "https://bitbucket.org/sobjectizerteam/restinio-0.4/downloads"
        tools.get("{0}/restinio-{1}.zip".format(source_url, self.version))
        extracted_dir = "restinio-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.definitions['RESTINIO_INSTALL'] = True
        cmake.definitions['RESTINIO_FIND_DEPS'] = False
        cmake.definitions['RESTINIO_USE_BOOST_ASIO'] = self.options.boost_libs
        cmake.configure(source_folder = self.source_subfolder + "/dev/restinio")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.hpp", dst="include/restinio", src=self.source_subfolder + "/dev/restinio")
        self.copy("license*", src=self.source_subfolder, dst="licenses",  ignore_case=True, keep_path=False)

