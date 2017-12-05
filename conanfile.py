# -*- coding: utf-8 -*-
from conans import AutoToolsBuildEnvironment, ConanFile, tools
from conans.util import files
import os


class OggConan(ConanFile):
    name = "ogg"
    version = "1.3.3"
    ZIP_FOLDER_NAME = "libogg-{}".format(version)
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = "shared=False", "fPIC=True"
    exports_sources = ["CMakeLists.txt"]
    url = "https://github.com/fogo/conan-ogg"
    license = "https://github.com/xiph/ogg#license"
    description = "Ogg project codecs use the Ogg bitstream format to arrange " \
                  "the raw, compressed bitstream into a more robust, useful " \
                  "form. For example, the Ogg bitstream makes seeking, time " \
                  "stamping and error recovery possible, as well as mixing " \
                  "several separate, concurrent media streams into a single " \
                  "physical bitstream."
    checksum = "c2e8a485110b97550f453226ec644ebac6cb29d1caef2902c007edab4308d985"

    def configure(self):
        # it is just C code, this is unnecessary
        del self.settings.compiler.libcxx

    def source(self):
        # https://archive.mozilla.org/pub/opus/opus-1.2.1.tar.gz
        zip_name = "libogg-{version}.tar.gz".format(version=self.version)
        tools.download(
            "http://downloads.xiph.org/releases/ogg/{zip_name}".format(zip_name=zip_name),
            zip_name)

        tools.check_sha256(zip_name, self.checksum)

        tools.unzip(zip_name)
        os.unlink(zip_name)
        if self.settings.os != "Windows":
            self.run("chmod +x ./{}/configure".format(self.ZIP_FOLDER_NAME))

    def build(self):
        with tools.chdir(self.ZIP_FOLDER_NAME):
            files.mkdir("_build")
            with tools.chdir("_build"):
                if not tools.os_info.is_windows:
                    args = []
                    if self.options.shared:
                        args.append("--enable-shared=yes")
                        args.append("--enable-static=no")
                    else:
                        args.append("--enable-shared=no")
                        args.append("--enable-static=yes")

                    env_build = AutoToolsBuildEnvironment(self)
                    env_build.fpic = self.options.fPIC
                    env_build.configure("..", args=args)
                    env_build.make()
                else:
                    raise Exception("TODO: windows")

    def package(self):
        self.copy(
            "*.h",
            dst="include/ogg",
            src="{basedir}/include/ogg".format(basedir=self.ZIP_FOLDER_NAME))
        self.copy(
            "*.h",
            dst="include/ogg",
            src="{basedir}/_build/include/ogg".format(basedir=self.ZIP_FOLDER_NAME))
        self.copy(
            "*.a",
            dst="lib",
            src="{basedir}/_build/src/.libs".format(basedir=self.ZIP_FOLDER_NAME))
        self.copy(
            "*.so",
            dst="lib",
            src="{basedir}/_build/src/.libs".format(basedir=self.ZIP_FOLDER_NAME))

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
