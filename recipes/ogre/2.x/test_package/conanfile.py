from conans import ConanFile, CMake, tools
import os

class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["OGRE_VERSION"] = tools.Version(self.deps_cpp_info["ogre"].version)
        cmake.configure()
        cmake.build()

    def test(self):
        if tools.cross_building(self):
            return
        
        bin_path = os.path.join("bin", "test_package")
        self.run(bin_path, run_environment=True)
