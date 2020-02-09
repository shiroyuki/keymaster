IMAGE_TAG=shiroyuki/keymaster
PY_PROTO_DIR=keymaster/common/proto

proto-generated-python:
	echo "Generating the code from the proto file..." \
		&& python -m grpc_tools.protoc \
			-I . \
			--python_out=. \
			--grpc_python_out=. \
			$(PY_PROTO_DIR)/keymaster.proto \
		&& echo "The code generation is complete."

install:
	@echo "INFO: Installing the package"
	@pip3 install --no-deps -qI .
	@echo "INFO: Installation complete"

docker-build: proto-generated-python
	docker build -t $(IMAGE_TAG) .

dev-reset:
	(python -m keymaster server:teardown || echo "Nothing to reset"); python -m keymaster server:setup

dev-run: test-server

test-server:
	python3 -m keymaster serve -p 8000

test-login:
	python3 -m keymaster login --non-secure --port 8000 localhost developer password

test-sh:
	python3 -m keymaster sh

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