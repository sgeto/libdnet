dnl
dnl configure.ac
dnl
dnl Copyright (c) 2000 Dug Song <dugsong@monkey.org>
dnl Modified by Ali Abdulkadir <autostart.ini@gmail.com>
dnl
dnl Process this file with autoconf to produce a configure script.

AC_INIT(
    [libdnet],
    [1.12],
    [https://github.com/sgeto/libdnet/issues],
    [libdnet],
    [https://github.com/sgeto/libdnet])

AC_CONFIG_SRCDIR([include/dnet.h])
AC_CONFIG_AUX_DIR([build-aux])
AC_SUBST(ac_aux_dir)
AC_PREREQ([2.69])
LT_PREREQ([2.4.2])
AC_COPYRIGHT([Copyright 2000 - 2017 The libdnet Developer Community])
AC_MSG_RESULT(Beginning autoconfiguration process for libdnet-${PACKAGE_VERSION} ...)
AC_PROG_SHELL
AC_CONFIG_HEADERS([include/config.h])
AM_INIT_AUTOMAKE([1.14 foreign no-dependencies tar-ustar dist-zip])
AM_SILENT_RULES([yes])

# for libtoolize
AC_CONFIG_MACRO_DIR([m4])

dnl the default compiler flags are "-O2 -g" if the user does not set anything.
dnl IMO O2 optimizations are fine, but debugging should be completely up to the
dnl user. The following test does just that. (Do not move these lines
dnl below "AC_PROG_CC"!!)
if test -z $CFLAGS; then
    CFLAGS="-O2"
fi

dnl Check for system type.
dnl We do this to qualify our later feature checks
AC_CANONICAL_HOST

case "$host_os" in
  *mingw*) MINGW=yes;;
        *) MINGW=no;;
esac

dnl Initialize and Handle the --prefix=... option
if test "${prefix}" = "NONE"; then
    prefix=/usr/local
fi
if test "${exec_prefix}" = "NONE"; then
    exec_prefix=$prefix
fi
dnl libdir must be a fully qualified path (not ${exec_prefix}/lib)
eval libdir="$libdir"

dnl Checks for programs.
AC_PROG_CC
AC_PROG_INSTALL
LT_INIT([dlopen pic-only])

dnl Checks for Python.
dnl AM_PATH_PYTHON([2.7.6],, [:])
AC_CHECK_TOOL(PYTHON, python2, :)

AC_ARG_ENABLE([python],
  [AS_HELP_STRING([--disable-python], [Do not try to build Python module @<:@default=check@:>@])],
  [:],
  [enable_python=check])

AS_IF([test "$enable_python" != "no"],
  [PKG_CHECK_MODULES([PYTHON],
    [python2],
    [enable_python=yes],
    [AS_IF([test "$enable_python" = "yes"],
      [AC_MSG_ERROR([Python required, but not found.])],
      [enable_python=no])])])

AM_CONDITIONAL([ENABLE_PYTHON], [test "$enable_python" = "yes"])

dnl FIXME Tcl (Tool Command Language). Is this even used?
dnl AC_SUBST(TCLINC)
dnl AC_SUBST(TCLLIB)
dnl AM_CONDITIONAL(TCL, [test "x$TCLINC" != "x"])

dnl XXX - stupid IRIX cpp
if test -r /usr/include/sgidefs.h ; then
    CPPFLAGS="$CPPFLAGS -D__sgi"
fi

if test "$MINGW" = yes ; then
    WIN32="yes"
    AC_SUBST(WIN32)
    AC_CHECK_TOOL([WINDRES], [windres], AC_MSG_ERROR([windres not found]))
    AC_SUBST(WINDRES)
    AC_DEFINE(WIN32_LEAN_AND_MEAN, 1, 
        [Define for faster code generation.])
    if test "${cross_compiling}" = "yes" ; then
       if test "$host" = "i686-w64-mingw32" ; then
    AC_CHECK_LIB(packet, PacketSetMode, ,AC_MSG_ERROR(libpacket.a not found.))
    AC_CHECK_LIB(wpcap, pcap_setmode, ,AC_MSG_ERROR(libwpcap.a not found.))
    LIBS="$LIBS -lws2_32 -liphlpapi"
    CFLAGS="$CFLAGS -static-libgcc -march=i686 -mwin32"
       else
    AC_CHECK_LIB(packet, PacketSetMode, ,AC_MSG_ERROR(libpacket.a not found.))
    AC_CHECK_LIB(wpcap, pcap_setmode, ,AC_MSG_ERROR(libwpcap.a not found.))
    LIBS="$LIBS -lws2_32 -liphlpapi"
    CFLAGS="$CFLAGS -static-libgcc -mwin32"
    LDFLAGS="$LDFLAGS -Wl,--high-entropy-va"
       fi
    else
       if test "$host" = "i686-w64-mingw32" ; then
    AC_CHECK_LIB(packet, PacketSetMode, ,AC_MSG_ERROR(libpacket.a not found.))
    AC_CHECK_LIB(wpcap, pcap_setmode, ,AC_MSG_ERROR(libwpcap.a not found.))
    LIBS="$LIBS -lws2_32 -liphlpapi"
    CFLAGS="$CFLAGS -march=i686 -mwin32"
       else
    AC_CHECK_LIB(packet, PacketSetMode, ,AC_MSG_ERROR(libpacket.a not found.))
    AC_CHECK_LIB(wpcap, pcap_setmode, ,AC_MSG_ERROR(libwpcap.a not found.))
    LIBS="$LIBS -lws2_32 -liphlpapi"
    CFLAGS="$CFLAGS -mwin32"
       fi
    fi
fi

dnl this should only matter if we are building for Windows...
AM_CONDITIONAL([WIN32], [test "${WIN32}" = "yes"])

dnl Checks for libraries.
if test "$MINGW" != yes ; then
    AC_LBL_LIBRARY_NET
    AC_CHECK_LIB(nm, open_mib)
fi

dnl Checks for Unit testing.
AC_ARG_ENABLE([check],
  [AS_HELP_STRING([--disable-check], [Skip unit tests @<:@default=check@:>@])],
  [:],
  [enable_check=check])

AS_IF([test "$enable_check" != "no"],
  [PKG_CHECK_MODULES([CHECK],
    [check],
    [enable_check=yes],
    [AS_IF([test "$enable_check" = "yes"],
      [AC_MSG_ERROR([Check (https://libcheck.github.io/check/) required, but not found.])],
      [enable_check=no])])])

AM_CONDITIONAL([ENABLE_CHECK], [test "$enable_check" = "yes"])

dnl Checks for header files.
AC_HEADER_STDC
if test "$MINGW" != yes ; then
    AC_CHECK_HEADERS(fcntl.h unistd.h)
    AC_CHECK_HEADERS(sys/bufmod.h sys/dlpi.h sys/dlpihdr.h sys/dlpi_ext.h \
        sys/ioctl.h sys/mib.h sys/ndd_var.h sys/socket.h sys/sockio.h \
        sys/sysctl.h sys/time.h)
    AC_CHECK_HEADERS(net/bpf.h net/if.h net/if_var.h \
        net/if_arp.h net/if_dl.h net/pfilt.h \
        net/pfvar.h net/radix.h net/raw.h net/route.h netinet/in_var.h \
        net/if_tun.h linux/if_tun.h netinet/ip_fw.h linux/ip_fw.h \
        linux/ip_fwchains.h linux/netfilter_ipv4/ipchains_core.h)
    AC_CHECK_HEADERS(ip_fil_compat.h netinet/ip_fil_compat.h ip_compat.h \
        netinet/ip_compat.h ip_fil.h netinet/ip_fil.h)
    AC_CHECK_HEADERS(hpsecurity.h stropts.h)
fi

dnl Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST
AC_C_INLINE
AC_TYPE_PID_T
AC_TYPE_SIZE_T
AC_DNET_SOCKADDR_IN6
if test "$ac_cv_header_sys_socket_h" = yes ; then
    AC_DNET_SOCKADDR_SA_LEN
fi
if test "$ac_cv_header_net_if_arp_h" = yes ; then
    AC_DNET_ARPREQ_ARP_DEV
fi
if test "$ac_cv_header_net_route_h" = yes ; then
    AC_DNET_ROUTE_RT_MSGHDR
fi

dnl Checks for library functions.
AC_FUNC_MEMCMP
AC_REPLACE_FUNCS(err strlcat strlcpy strsep)

dnl Checks for other system-specific jonks.
if test "$MINGW" != yes ; then
    AC_DNET_BSD_BPF
    AC_DNET_LINUX_PROCFS
    AC_DNET_LINUX_PF_PACKET
    AC_DNET_STREAMS_MIB2
    AC_DNET_STREAMS_ROUTE
    AC_DNET_IOCTL_ARP
    AC_DNET_RAWIP_HOST_OFFLEN
    AC_DNET_RAWIP_COOKED
fi

dnl Check for arp interface.
if test "$ac_cv_header_iphlpapi_h" = yes ; then
    AC_LIBOBJ([arp-win32])
elif test "$ac_cv_dnet_ioctl_arp" = yes ; then
    AC_LIBOBJ([arp-ioctl])
elif test "$ac_cv_dnet_route_h_has_rt_msghdr" = yes ; then
    AC_LIBOBJ([arp-bsd])
else
    AC_LIBOBJ([arp-none])
fi

dnl Check for Ethernet interface.
if test "$ac_cv_header_iphlpapi_h" = yes ; then
    AC_LIBOBJ([eth-win32])
elif test "$ac_cv_header_net_pfilt_h" = yes ; then
    AC_LIBOBJ([eth-pfilt])
elif test "$ac_cv_dnet_bsd_bpf" = yes ; then
    AC_LIBOBJ([eth-bsd])
elif test "$ac_cv_dnet_linux_pf_packet" = yes ; then
    AC_LIBOBJ([eth-linux])
elif test "$ac_cv_header_net_raw_h" = yes ; then
    AC_LIBOBJ([eth-snoop])
elif test "$ac_cv_header_sys_ndd_var_h" = yes ; then
    AC_LIBOBJ([eth-ndd])
elif test "$ac_cv_header_sys_dlpi_h" = yes || \
     test "$ac_cv_header_sys_dlpihdr_h" = yes ; then
    AC_LIBOBJ([eth-dlpi])
else
    AC_LIBOBJ([eth-none])
fi

dnl Check for firewall interface.
if test "$ac_cv_header_iphlpapi_h" = yes ; then
        AC_LIBOBJ([fw-pktfilter])
elif test "$ac_cv_header_net_pfvar_h" = yes ; then
    AC_LIBOBJ([fw-pf])
elif test "$ac_cv_header_netinet_ip_fw_h" = yes ; then
     dnl XXX - ipfw2 support later...
     case "$host_os" in
     *freebsd5* | *kfreebsd*)
    AC_LIBOBJ([fw-none]) ;;
     *)
    AC_LIBOBJ([fw-ipfw]) ;;
     esac
elif test "$ac_cv_header_netinet_ip_fil_h" = yes ; then
    AC_LIBOBJ([fw-ipf])
elif test "$ac_cv_header_linux_ip_fw_h" = yes ; then
    AC_LIBOBJ([fw-ipchains])
elif test "$ac_cv_header_linux_ip_fwchains_h" = yes ; then
    AC_LIBOBJ([fw-ipchains])
elif test "$ac_cv_header_linux_netfilter_ipv4_ipchains_core_h" = yes ; then
    AC_LIBOBJ([fw-ipchains])
else
    AC_LIBOBJ([fw-none])
fi

dnl Check for network interface interface.
if test "$ac_cv_header_iphlpapi_h" = yes ; then
    AC_LIBOBJ([intf-win32])
else
    AC_LIBOBJ([intf])
fi

dnl Check for raw IP interface.
if test "$ac_cv_header_iphlpapi_h" = yes ; then
    AC_LIBOBJ([ip-win32])
elif test "$ac_cv_dnet_rawip_cooked" = yes ; then
    AC_LIBOBJ([ip-cooked])
else
    AC_LIBOBJ([ip])
fi

dnl Check for routing interface.
if test "$ac_cv_header_iphlpapi_h" = yes ; then
    AC_LIBOBJ([route-win32])
elif test "$ac_cv_dnet_route_h_has_rt_msghdr" = yes ; then
    AC_LIBOBJ([route-bsd])
elif test "$ac_cv_dnet_linux_procfs" = yes ; then
    AC_LIBOBJ([route-linux])
elif test "$ac_cv_header_hpsecurity_h" = yes ; then
    AC_LIBOBJ([route-hpux])
else
    AC_LIBOBJ([route-none])
fi

dnl Check for tun interface.
if test "$ac_cv_header_linux_if_tun_h" = yes ; then
    AC_LIBOBJ([tun-linux])
elif test "$ac_cv_header_net_if_tun_h" = yes ; then
    AC_LIBOBJ([tun-bsd])
elif test -c "/dev/tun0" ; then
    AC_LIBOBJ([tun-bsd])
else
    AC_LIBOBJ([tun-none])
fi

AC_CONFIG_FILES([Makefile dnet-config include/Makefile
    src/Makefile python/Makefile python/setup.py
    test/Makefile test/check/Makefile test/dnet/Makefile])
AC_CONFIG_COMMANDS([default],[chmod 755 dnet-config],[])
AC_OUTPUT

AC_MSG_RESULT([
$PACKAGE_STRING Configuration Complete
======================================

Configuration Summary
---------------------
    Prefix: ...................... ${prefix}
    CC: .......................... ${CC}
    CFLAGS:....................... ${CFLAGS}
    LD: .......................... ${LD}
    LDFLAGS: ..................... ${LDFLAGS}
    Build Python module: ......... ${enable_python}
    Use Check .................... ${enable_check}

To override options, see ./configure --help

Report bugs to ${PACKAGE_BUGREPORT}
])
