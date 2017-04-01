## $Id: Makefile.am 427 2003-03-28 06:02:44Z dugsong $

sbin_PROGRAMS = dumbnet

dumbnet_SOURCES = addr.c arp.c aton.c aton.h dumbnet.c eth.c fw.c hex.c \
	icmp.c intf.c ip.c mod.h rand.c route.c send.c tcp.c udp.c

man_MANS = dumbnet.8

EXTRA_DIST = $(man_MANS)

dumbnet_LDADD = $(top_builddir)/src/libdumbnet.la

dumbnet.8.txt: dumbnet.8
	groff -t -e -mdoc -Tascii dumbnet.8 | col -bx > $@

