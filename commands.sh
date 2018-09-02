#!/usr/bin/env bash
protoc -I=ProtoBuff/ --python_out=ProtoBuff/  ProtoBuff/host.proto