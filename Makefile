PACKAGE = lostlabel
VERSION = 0.1
RELEASE = $(PACKAGE)-$(VERSION)
DIST = $(RELEASE).tar.gz

.PHONY: all

all: $(DIST)
	rpmbuild -D '_rpmdir .' -tb $(DIST)

$(DIST): .git/
	git archive --prefix=$(RELEASE)/ -o $@ HEAD

clean:
	rm -f $(DIST)
	rm -fr noarch/
