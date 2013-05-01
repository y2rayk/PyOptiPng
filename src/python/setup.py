from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# gcc -fPIC -shared optipng.o pyutil.o ../optipng.o ../opngoptim.o ../../lib/libpng/libpng.a ../cbitset.o ../osys.o ../../lib/pngxtern/pngxtern.a ../opngreduc.o -o pyoptipng.so   
#Extension("optipng", ["optipngmodule.c"], include_dirs=["/home/ubuntu/optipng-0.7.4/src/lib/libpng/", "/home/ubuntu/optipng-0.7.4/src/lib/pngxtern", "/home/ubuntu/optipng-0.7.4/src/optipng/"], libraries=[], extra_objects=['pyutil.o', '../optipng.o', '../opngoptim.o', '../../lib/libpng/libpng.a', '../cbitset.o', '../osys.o', '../../lib/pngxtern/pngxtern.a', '../opngreduc.o'])
setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
	Extension("optipng", ["optipngmodule.c", 'pyutil.c'], include_dirs=[".."], libraries=[], extra_objects=['../optipng.o', '../opngoptim.o', '../../lib/libpng/libpng.a', '../cbitset.o', '../osys.o', '../../lib/pngxtern/pngxtern.a', '../opngreduc.o'])
	#Extension("pyoptipng", ["optipng.pyx","optipngmodule.c"], include_dirs=["."], libraries=[])
	]
)
