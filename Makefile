PREVIEW_SRC_DEST=/tmp/site_preview

preview:
	mkdir -p $(PREVIEW_SRC_DEST)
	rm -rf $(PREVIEW_SRC_DEST)
	git clone https://github.com/scientific-python/scientific-python.org $(PREVIEW_SRC_DEST)
	git -C $(PREVIEW_SRC_DEST) submodule update --init
	rm -rf $(PREVIEW_SRC_DEST)/content/specs/*
	cp -r * $(PREVIEW_SRC_DEST)/content/specs
	cd $(PREVIEW_SRC_DEST) && hugo server --disableFastRender

clean:
	rm -rf $(PREVIEW_SRC_DEST)

.PHONY: clean preview
