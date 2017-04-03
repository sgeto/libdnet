## $Id: Makefile.am 618 2006-01-15 06:42:19Z dugsong $

ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}

SUBDIRS = include src python test

bin_SCRIPTS = dnet-config

man_MANS = doc/dnet-config.1 doc/dnet.3 doc/dnet.8

dnet.3.txt: dnet.3
	groff -t -e -mdoc -Tascii dnet.3 | col -bx > $@

EXTRA_DIST = README.md LICENSE doc/THANKS doc/TODO $(m4data_DATA) $(man_MANS)

CLEANFILES = dnet-config

# (GNU make only) Unless we say otherwise, spare us the
# “Entering/Leaving directory ...” messages
GNUMAKEFLAGS = $(if $(value VERBOSE),,--no-print-directory)