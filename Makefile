test-sh:
	python3 -m keymaster.client sh

test-installed-sh: test-install
	@km sh; make test-uninstall

test-install:
	@echo "INFO: Installing the package without dependencies..."
	@pip3 install --no-deps -qI .
	@echo "INFO: Installation complete"

test-uninstall:
	@echo "INFO: Uninstalling..."
	@pip3 uninstall -qy keymaster
	@echo "INFO: Uninstalled"