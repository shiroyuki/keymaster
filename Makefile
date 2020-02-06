PY_PROTO_DIR=.

proto-generated-python:
	(rm keymaster_pb2.py keymaster_pb2_grpc.py || echo "No old generated code"); \
		echo "Generating the code from the proto file..." \
		&& python -m grpc_tools.protoc \
			-I data \
			--python_out=$(PY_PROTO_DIR) \
			--grpc_python_out=$(PY_PROTO_DIR) \
			data/keymaster.proto \
		&& echo "The code generation is complete."

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