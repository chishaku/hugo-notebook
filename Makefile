.PHONY: clone-theme serve

help: 
	@echo "\nHelp:"
	@echo "\tinstall: Install hugo and clone themes."
	@echo "\tserve: Serve notebook."
	@echo ""
	@echo "\tinstall-hugo: Install hugo."
	@echo "\tclone-theme: Clone requisite theme and delete git reference."
	@echo ""

serve:
	hugo serve --buildDrafts

install: install-hugo clone-theme 

install-hugo:
	@echo "\nInstalling hugo.\n"
	brew update && brew install hugo

clone-theme:
	@echo "\nInstalling themes.\n"
	git clone https://github.com/chishaku/hugo-theme-crisp themes/hugo-theme-crisp
	rm -rf themes/hugo-theme-crisp/.git
