from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
    Extension("optipng", ["optipngmodule.c", 'pyutil.c'], include_dirs=[".."], libraries=[], extra_objects=['../optipng.o', '../opngoptim.o', '../../lib/libpng/libpng14_la-png.o', '../../lib/libpng/libpng14_la-pngrio.o', '../../lib/libpng/libpng14_la-pngwio.o', '../../lib/libpng/libpng14_la-pngrtran.o', '../../lib/libpng/libpng14_la-pngrutil.o', '../../lib/libpng/libpng14_la-pngread.o', '../../lib/libpng/libpng14_la-pngset.o', '../../lib/libpng/libpng14_la-pngwtran.o', '../../lib/libpng/libpng14_la-pngwutil.o', '../../lib/libpng/libpng14_la-pngerror.o', '../../lib/libpng/libpng14_la-pngmem.o', '../../lib/libpng/libpng14_la-pngwrite.o', '../../lib/libpng/libpng14_la-pngtrans.o', '../../lib/libpng/libpng14_la-pngget.o', '../cbitset.o', '../osys.o', '../../lib/pngxtern/pngxrbmp.o', '../../lib/pngxtern/pnmout.o', '../../lib/pngxtern/pnmutil.o', '../../lib/pngxtern/pngxset.o', '../../lib/pngxtern/pngxmem.o', '../../lib/pngxtern/pnmin.o', '../../lib/pngxtern/pngxrpnm.o', '../../lib/pngxtern/minitiff.o', '../../lib/pngxtern/tiffread.o', '../../lib/pngxtern/pngxrtif.o', '../../lib/pngxtern/gifread.o', '../../lib/pngxtern/pngxrgif.o', '../../lib/pngxtern/pngxread.o', '../../lib/pngxtern/pngxrjpg.o', '../opngreduc.o', '../../lib/zlib/inflate.o', '../../lib/zlib/zutil.o', '../../lib/zlib/inftrees.o', '../../lib/zlib/inffast.o', '../../lib/zlib/crc32.o', '../../lib/zlib/deflate.o', '../../lib/zlib/trees.o', '../../lib/zlib/adler32.o'], extra_compile_args=['-fPIC'])
	]
)

