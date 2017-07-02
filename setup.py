#!/usr/bin/env python
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
import glob
import os
import sys


dnet_srcs = [ 'python/dnet.c' ]
dnet_incdirs = [ 'include' ]
dnet_libdirs = []
dnet_libs = []
dnet_extargs = []
dnet_extobj = []

if sys.platform == 'win32':
    dnet_srcs.extend(['src/addr-util.c', 'src/addr.c', 'src/blob.c', 'src/ip-util.c', 'src/ip6.c', 'src/rand.c', 'src/err.c', 'src/strlcat.c', 'src/strlcpy.c', 'src/strsep.c', 'src/arp-win32.c', 'src/eth-win32.c', 'src/fw-pktfilter.c', 'src/intf-win32.c', 'src/ip-win32.c', 'src/route-win32.c', 'src/tun-none.c'])
    dnet_libs.extend([ 'iphlpapi', 'ws2_32', 'packet', 'wpcap' ])
elif sys.platform.startswith('linux'):
    dnet_srcs.extend(['src/addr-util.c', 'src/addr.c', 'src/blob.c', 'src/ip-util.c', 'src/ip6.c', 'src/rand.c', 'src/strlcat.c', 'src/strlcpy.c', 'src/arp-ioctl.c', 'src/eth-linux.c', 'src/fw-none.c', 'src/intf.c', 'src/ip.c', 'src/route-linux.c', 'src/tun-linux.c'])
elif sys.platform == 'darwin':
    dnet_srcs.extend(['src/addr-util.c', 'src/addr.c', 'src/blob.c', 'src/ip-util.c', 'src/ip6.c', 'src/rand.c', 'src/arp-bsd.c', 'src/eth-bsd.c', 'src/fw-none.c', 'src/intf.c', 'src/ip.c', 'src/route-bsd.c', 'src/tun-none.c'])
else:
    # XXX - can't build on Cygwin+MinGW yet.
    #if sys.platform == 'cygwin':
    #    dnet_extargs.append('-mno-cygwin')
    dnet_extobj.extend(glob.glob('src/.libs/*.o'))

dnet = Extension('dnet',
                 dnet_srcs,
                 include_dirs=dnet_incdirs,
                 library_dirs=dnet_libdirs,
                 libraries=dnet_libs,
                 extra_compile_args=dnet_extargs,
                 extra_objects=dnet_extobj)

setup(name='dnet',
      version='1.12',
      description='low-level networking library',
      author='Dug Song',
      author_email='dugsong@monkey.org',
      url='http://libdnet.sourceforge.net/',
      ext_modules = [ dnet ])
