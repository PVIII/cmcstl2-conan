from conans import ConanFile, CMake, tools

class CmcStl2(ConanFile):
    name = "cmcstl2"
    version = "684a96d"
    url = "http://github.com/CaseyCarter/cmcstl2.git"
    license = "BSL-1.0"
    description = "An implementation of C++ Extensions for Ranges."
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"

    def source(self):
        git = tools.Git()
        git.clone(self.url)
        git.checkout(self.version)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()
        self.copy("LICENSE.txt")
        self.copy("README.md")

    def package_id(self):
        self.info.header_only()
