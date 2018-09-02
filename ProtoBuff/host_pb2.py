# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: host.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='host.proto',
  package='ProtoBuff',
  syntax='proto3',
  serialized_pb=_b('\n\nhost.proto\x12\tProtoBuff\"g\n\x08hostData\x12\x1e\n\x05hosts\x18\x01 \x03(\x0b\x32\x0f.ProtoBuff.host\x12\x12\n\nsnapshotId\x18\x02 \x01(\t\x12\x14\n\x0csnapshotTime\x18\x03 \x01(\x03\x12\x11\n\toperation\x18\x04 \x01(\t\"\x82\x07\n\x04host\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ssVLANId\x18\x02 \x01(\t\x12\x0e\n\x06hostIp\x18\x03 \x01(\t\x12\x17\n\x0f\x63onnectedDevice\x18\x04 \x01(\t\x12\x1a\n\x12\x63onnectedInterface\x18\x05 \x01(\t\x12\x13\n\x0b\x63onnectedAP\x18\x06 \x01(\t\x12\x10\n\x08hostType\x18\x07 \x01(\t\x12\x17\n\x0fisAuthenticated\x18\x08 \x01(\x08\x12\x1b\n\x13isDirectlyConnected\x18\t \x01(\x08\x12\x13\n\x0blastUpdated\x18\n \x01(\t\x12\x12\n\nnumUpdates\x18\x0b \x01(\t\x12\x19\n\x11pointOfAttachment\x18\x0c \x01(\t\x12\x17\n\x0fpointOfPresence\x18\r \x01(\t\x12\x12\n\nuserGroups\x18\x0e \x01(\t\x12\x12\n\nuserStatus\x18\x0f \x01(\t\x12\x17\n\x0fwlanProfileName\x18\x10 \x01(\t\x12\x16\n\x0e\x63onnectedAPUrl\x18\x11 \x01(\t\x12\x1a\n\x12\x63onnectedDeviceUrl\x18\x12 \x01(\t\x12\x1d\n\x15\x63onnectedInterfaceUrl\x18\x13 \x01(\t\x12\x1c\n\x14\x63onnectedAPIpAddress\x18\x14 \x01(\t\x12\x1d\n\x15\x63onnectedAPMacAddress\x18\x15 \x01(\t\x12\x17\n\x0f\x63onnectedAPName\x18\x16 \x01(\t\x12\x1c\n\x14\x63onnectedInterfaceId\x18\x17 \x01(\t\x12\x1e\n\x16\x63onnectedInterfaceName\x18\x18 \x01(\t\x12 \n\x18\x63onnectedNetworkDeviceId\x18\x19 \x01(\t\x12\'\n\x1f\x63onnectedNetworkDeviceIpAddress\x18\x1a \x01(\t\x12\x0f\n\x07hostMac\x18\x1b \x01(\t\x12\x10\n\x08hostName\x18\x1c \x01(\t\x12\x1a\n\x12\x61vgUpdateFrequency\x18\x1d \x01(\t\x12\x15\n\rconnectedAPId\x18\x1e \x01(\t\x12\x0e\n\x06userId\x18\x1f \x01(\t\x12\x0f\n\x07subType\x18  \x01(\t\x12\x0e\n\x06vlanId\x18! \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\" \x01(\t\x12\x16\n\x0eowningEntityId\x18# \x01(\t\x12\x0c\n\x04name\x18$ \x01(\t\x12\x14\n\x0cinstanceUuid\x18% \x01(\t\x12\n\n\x02id\x18& \x01(\tb\x06proto3')
)




_HOSTDATA = _descriptor.Descriptor(
  name='hostData',
  full_name='ProtoBuff.hostData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hosts', full_name='ProtoBuff.hostData.hosts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapshotId', full_name='ProtoBuff.hostData.snapshotId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapshotTime', full_name='ProtoBuff.hostData.snapshotTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='ProtoBuff.hostData.operation', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=128,
)


_HOST = _descriptor.Descriptor(
  name='host',
  full_name='ProtoBuff.host',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='ProtoBuff.host.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accessVLANId', full_name='ProtoBuff.host.accessVLANId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostIp', full_name='ProtoBuff.host.hostIp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedDevice', full_name='ProtoBuff.host.connectedDevice', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedInterface', full_name='ProtoBuff.host.connectedInterface', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedAP', full_name='ProtoBuff.host.connectedAP', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostType', full_name='ProtoBuff.host.hostType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isAuthenticated', full_name='ProtoBuff.host.isAuthenticated', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isDirectlyConnected', full_name='ProtoBuff.host.isDirectlyConnected', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastUpdated', full_name='ProtoBuff.host.lastUpdated', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numUpdates', full_name='ProtoBuff.host.numUpdates', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pointOfAttachment', full_name='ProtoBuff.host.pointOfAttachment', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pointOfPresence', full_name='ProtoBuff.host.pointOfPresence', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userGroups', full_name='ProtoBuff.host.userGroups', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userStatus', full_name='ProtoBuff.host.userStatus', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wlanProfileName', full_name='ProtoBuff.host.wlanProfileName', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedAPUrl', full_name='ProtoBuff.host.connectedAPUrl', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedDeviceUrl', full_name='ProtoBuff.host.connectedDeviceUrl', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedInterfaceUrl', full_name='ProtoBuff.host.connectedInterfaceUrl', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedAPIpAddress', full_name='ProtoBuff.host.connectedAPIpAddress', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedAPMacAddress', full_name='ProtoBuff.host.connectedAPMacAddress', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedAPName', full_name='ProtoBuff.host.connectedAPName', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedInterfaceId', full_name='ProtoBuff.host.connectedInterfaceId', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedInterfaceName', full_name='ProtoBuff.host.connectedInterfaceName', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedNetworkDeviceId', full_name='ProtoBuff.host.connectedNetworkDeviceId', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedNetworkDeviceIpAddress', full_name='ProtoBuff.host.connectedNetworkDeviceIpAddress', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostMac', full_name='ProtoBuff.host.hostMac', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostName', full_name='ProtoBuff.host.hostName', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avgUpdateFrequency', full_name='ProtoBuff.host.avgUpdateFrequency', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connectedAPId', full_name='ProtoBuff.host.connectedAPId', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userId', full_name='ProtoBuff.host.userId', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subType', full_name='ProtoBuff.host.subType', index=31,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vlanId', full_name='ProtoBuff.host.vlanId', index=32,
      number=33, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ProtoBuff.host.description', index=33,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owningEntityId', full_name='ProtoBuff.host.owningEntityId', index=34,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ProtoBuff.host.name', index=35,
      number=36, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceUuid', full_name='ProtoBuff.host.instanceUuid', index=36,
      number=37, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='ProtoBuff.host.id', index=37,
      number=38, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=1029,
)

_HOSTDATA.fields_by_name['hosts'].message_type = _HOST
DESCRIPTOR.message_types_by_name['hostData'] = _HOSTDATA
DESCRIPTOR.message_types_by_name['host'] = _HOST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

hostData = _reflection.GeneratedProtocolMessageType('hostData', (_message.Message,), dict(
  DESCRIPTOR = _HOSTDATA,
  __module__ = 'host_pb2'
  # @@protoc_insertion_point(class_scope:ProtoBuff.hostData)
  ))
_sym_db.RegisterMessage(hostData)

host = _reflection.GeneratedProtocolMessageType('host', (_message.Message,), dict(
  DESCRIPTOR = _HOST,
  __module__ = 'host_pb2'
  # @@protoc_insertion_point(class_scope:ProtoBuff.host)
  ))
_sym_db.RegisterMessage(host)


# @@protoc_insertion_point(module_scope)