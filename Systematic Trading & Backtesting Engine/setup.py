from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import sysconfig

try:
    import pybind11  # type: ignore
except ImportError as e:
    raise RuntimeError("pybind11 is required to build exec_core. Install with pip install pybind11") from e


def get_ext_modules():
    include_dirs = [pybind11.get_include()]
    compile_args = ["-std=c++17", "-O3"]
    if sys.platform == "darwin":
        compile_args.append("-mmacosx-version-min=10.14")
    return [
        Extension(
            "exec_core",
            ["exec_core.cpp"],
            include_dirs=include_dirs,
            language="c++",
            extra_compile_args=compile_args,
        )
    ]


class BuildExt(build_ext):
    def build_extensions(self):
        ct = sysconfig.get_config_var("CFLAGS") or ""
        for ext in self.extensions:
            if sys.platform == "win32":
                ext.extra_compile_args = ["/std:c++17", "/O2"]
        super().build_extensions()


setup(
    name="exec_core",
    version="0.1.0",
    ext_modules=get_ext_modules(),
    cmdclass={"build_ext": BuildExt},
    zip_safe=False,
)
