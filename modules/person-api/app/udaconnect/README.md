# UdaConnect Person API

gRPC server is running on port: `5005`.

## Generate Python Code from Protobuf

### Install Protobuf Compiler

```bash
pip install grpcio-tools
```

### Generate Python Code

```bash
python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ person.proto
```
