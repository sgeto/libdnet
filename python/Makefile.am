## $Id: Makefile.am 601 2005-02-25 22:44:39Z dugsong $

if ENABLE_PYTHON
AM_CFLAGS = $(PYTHON_CFLAGS)
LDADD = $(PYTHON_CFLAGS)

noinst_SCRIPTS = python-build

$(srcdir)/dnet.c: $(srcdir)/dnet.pyx
	pyrexc $(srcdir)/dnet.pyx || pyrexc.py $(srcdir)/dnet.pyx

python-build: $(srcdir)/dnet.c
	$(PYTHON) setup.py build
	touch python-build

python-clean:
	rm -rf *build

clean: python-clean

distclean: clean

python-install:
	$(PYTHON) setup.py install --prefix=$(DESTDIR)$(prefix)

install-exec-local: python-install

TESTS = test.py

endif

# endif

EXTRA_DIST = dnet.pyx dnet.c setup.py.in test.py

DISTCLEANFILES = *~
