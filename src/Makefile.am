
lib_LTLIBRARIES = libdumbnet.la

libdumbnet_la_SOURCES = addr-util.c addr.c blob.c ip-util.c ip6.c rand.c

libdumbnet_la_LIBADD = @LTLIBOBJS@

libdumbnet_la_LDFLAGS = -version-info 1:1:0

noinst_HEADERS = crc32ct.h

if WIN32
libdumbnet_la_SOURCES += dll_info.rc
libdumbnet_la_LDFLAGS += -no-undefined -Wl,--output-def,libdumbnet-1.def

.rc.lo:
			$(AM_V_GEN)$(LIBTOOL) --mode=compile --silent $(WINDRES) $< -o $@
endif
