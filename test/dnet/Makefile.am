## $Id: Makefile.am 427 2003-03-28 06:02:44Z dugsong $

sbin_PROGRAMS = dnet

dnet_SOURCES = addr.c arp.c aton.c aton.h dnet.c eth.c fw.c hex.c \
	icmp.c intf.c ip.c mod.h rand.c route.c send.c tcp.c udp.c

EXTRA_DIST = $(man_MANS)

dnet_LDADD = $(top_builddir)/src/libdnet.la

