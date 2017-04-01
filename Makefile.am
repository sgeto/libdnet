## $Id: Makefile.am 618 2006-01-15 06:42:19Z dugsong $

ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}

SUBDIRS = include src python test

bin_SCRIPTS = dumbnet-config

man_MANS = dumbnet-config.1 dumbnet.3

dumbnet.3.txt: dumbnet.3
	groff -t -e -mdoc -Tascii dumbnet.3 | col -bx > $@

EXTRA_DIST = LICENSE acconfig.h $(man_MANS)

CLEANFILES = dumbnet-config

# (GNU make only) Unless we say otherwise, spare us the
# “Entering/Leaving directory ...” messages
GNUMAKEFLAGS = $(if $(value VERBOSE),,--no-print-directory)