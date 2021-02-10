PREVIEW_SRC_DEST=/tmp/site_preview
HUGO_OPTS=--disableFastRender --buildDrafts

preview:
	mkdir -p $(PREVIEW_SRC_DEST)
	rm -rf $(PREVIEW_SRC_DEST)
	git clone https://github.com/scientific-python/scientific-python.org $(PREVIEW_SRC_DEST)
	git -C $(PREVIEW_SRC_DEST) submodule update --init
	rm -rf $(PREVIEW_SRC_DEST)/content/specs/*
	cp -r * $(PREVIEW_SRC_DEST)/content/specs
	cd $(PREVIEW_SRC_DEST) && hugo server $(HUGO_OPTS)

clean:
	rm -rf $(PREVIEW_SRC_DEST)

.PHONY: clean preview
