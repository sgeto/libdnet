if ENABLE_PYTHON
AM_CFLAGS = $(PYTHON_CFLAGS)
LDADD = $(PYTHON_CFLAGS)

noinst_SCRIPTS = python-build

$(srcdir)/dnet.c: $(srcdir)/dnet.pyx
	$(AM_V_GEN)cython -av $(srcdir)/dnet.pyx || $(AM_V_GEN)cython.py -av $(srcdir)/dnet.pyx

python-build: $(srcdir)/dnet.c
#	$(PYTHON) setup.py build
	$(AM_V_GEN)$(PYTHON) setup.py build_ext --inplace
	touch python-build

python-clean:
	rm -rf *build

clean: python-clean

distclean: clean

python-install:
	$(AM_V_GEN)$(PYTHON) setup.py install --prefix=$(DESTDIR)$(prefix)

install-exec-local: python-install

TESTS = test.py

endif

# endif

EXTRA_DIST = dnet.pyx dnet.c setup.py.in test.py

DISTCLEANFILES = *~
