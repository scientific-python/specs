PREVIEW_DEST:=$(if $(PREVIEW_DEST),$(PREVIEW_DEST),/tmp/__scientific-python.org_site-preview)
HUGO_OPTS=--disableFastRender --buildDrafts

.PHONY: clean preview prepare-preview preview
.DEFAULT_GOAL: preview-serve

# Substitute the SPECs in scientific-python.org with
# those from this repository
prepare-preview: clean
	mkdir -p $(PREVIEW_DEST)
	git clone https://github.com/scientific-python/scientific-python.org $(PREVIEW_DEST)
	git -C $(PREVIEW_DEST) submodule update --init
	cp -r * $(PREVIEW_DEST)/content/specs/

# Serve SPECs to http://localhost:1313
preview-serve: prepare-preview
	cd $(PREVIEW_DEST) && make serve

# Build website to $(PREVIEW_DEST)/public
preview-build: prepare-preview
	cd $(PREVIEW_DEST) && make html

clean:
	rm -rf $(PREVIEW_DEST)

.PHONY: clean preview
