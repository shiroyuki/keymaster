# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keymaster.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='keymaster.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fkeymaster.proto\"\x1e\n\x0f\x41\x62stractRequest\x12\x0b\n\x03jwt\x18\x01 \x01(\t\"0\n\x10\x41\x62stractResponse\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"M\n\x19UserAuthenticationRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\")\n\x1aUserAuthenticationResponse\x12\x0b\n\x03jwt\x18\x01 \x01(\t\"7\n\x0cQueryRequest\x12\x0b\n\x03jwt\x18\x01 \x01(\t\x12\x0c\n\x04term\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x03(\t\"G\n\x0eQueriedEntries\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x17\n\x07\x65ntries\x18\x03 \x03(\x0b\x32\x06.Entry\"\x87\x01\n\x05\x45ntry\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x0c\n\x04tags\x18\x05 \x03(\t\x12\x10\n\x08username\x18\x06 \x01(\t\x12\x10\n\x08password\x18\x07 \x01(\t\x12\x13\n\x0bmodified_at\x18\x08 \x01(\x01\"%\n\nGetRequest\x12\x0b\n\x03jwt\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"B\n\x0bGetResponse\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x15\n\x05\x65ntry\x18\x03 \x03(\x0b\x32\x06.Entry\"0\n\nPutRequest\x12\x0b\n\x03jwt\x18\x01 \x01(\t\x12\x15\n\x05\x65ntry\x18\x02 \x01(\x0b\x32\x06.Entry\"7\n\x0bPutResponse\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\"1\n\x11\x44\x65\x63ryptionRequest\x12\x0b\n\x03jwt\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"C\n\x12\x44\x65\x63ryptionResponse\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t2\xfa\x01\n\tKeymaster\x12K\n\x10\x41uthenticateUser\x12\x1a.UserAuthenticationRequest\x1a\x1b.UserAuthenticationResponse\x12(\n\x06Search\x12\r.QueryRequest\x1a\x0f.QueriedEntries\x12\x32\n\x07\x44\x65\x63rypt\x12\x12.DecryptionRequest\x1a\x13.DecryptionResponse\x12 \n\x03Get\x12\x0b.GetRequest\x1a\x0c.GetResponse\x12 \n\x03Put\x12\x0b.PutRequest\x1a\x0c.PutResponseb\x06proto3')
)




_ABSTRACTREQUEST = _descriptor.Descriptor(
  name='AbstractRequest',
  full_name='AbstractRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jwt', full_name='AbstractRequest.jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=19,
  serialized_end=49,
)


_ABSTRACTRESPONSE = _descriptor.Descriptor(
  name='AbstractResponse',
  full_name='AbstractResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='AbstractResponse.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='AbstractResponse.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=51,
  serialized_end=99,
)


_USERAUTHENTICATIONREQUEST = _descriptor.Descriptor(
  name='UserAuthenticationRequest',
  full_name='UserAuthenticationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='UserAuthenticationRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='UserAuthenticationRequest.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='UserAuthenticationRequest.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=101,
  serialized_end=178,
)


_USERAUTHENTICATIONRESPONSE = _descriptor.Descriptor(
  name='UserAuthenticationResponse',
  full_name='UserAuthenticationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jwt', full_name='UserAuthenticationResponse.jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=180,
  serialized_end=221,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jwt', full_name='QueryRequest.jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='term', full_name='QueryRequest.term', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='QueryRequest.type', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=223,
  serialized_end=278,
)


_QUERIEDENTRIES = _descriptor.Descriptor(
  name='QueriedEntries',
  full_name='QueriedEntries',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='QueriedEntries.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='QueriedEntries.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='QueriedEntries.entries', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=280,
  serialized_end=351,
)


_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Entry.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='Entry.kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Entry.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='Entry.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='Entry.tags', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='Entry.username', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='Entry.password', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modified_at', full_name='Entry.modified_at', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=354,
  serialized_end=489,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jwt', full_name='GetRequest.jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='GetRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=491,
  serialized_end=528,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='GetResponse.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='GetResponse.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entry', full_name='GetResponse.entry', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=530,
  serialized_end=596,
)


_PUTREQUEST = _descriptor.Descriptor(
  name='PutRequest',
  full_name='PutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jwt', full_name='PutRequest.jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entry', full_name='PutRequest.entry', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=598,
  serialized_end=646,
)


_PUTRESPONSE = _descriptor.Descriptor(
  name='PutResponse',
  full_name='PutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='PutResponse.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='PutResponse.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='PutResponse.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=648,
  serialized_end=703,
)


_DECRYPTIONREQUEST = _descriptor.Descriptor(
  name='DecryptionRequest',
  full_name='DecryptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jwt', full_name='DecryptionRequest.jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='DecryptionRequest.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=705,
  serialized_end=754,
)


_DECRYPTIONRESPONSE = _descriptor.Descriptor(
  name='DecryptionResponse',
  full_name='DecryptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='DecryptionResponse.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='DecryptionResponse.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='DecryptionResponse.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=756,
  serialized_end=823,
)

_QUERIEDENTRIES.fields_by_name['entries'].message_type = _ENTRY
_GETRESPONSE.fields_by_name['entry'].message_type = _ENTRY
_PUTREQUEST.fields_by_name['entry'].message_type = _ENTRY
DESCRIPTOR.message_types_by_name['AbstractRequest'] = _ABSTRACTREQUEST
DESCRIPTOR.message_types_by_name['AbstractResponse'] = _ABSTRACTRESPONSE
DESCRIPTOR.message_types_by_name['UserAuthenticationRequest'] = _USERAUTHENTICATIONREQUEST
DESCRIPTOR.message_types_by_name['UserAuthenticationResponse'] = _USERAUTHENTICATIONRESPONSE
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueriedEntries'] = _QUERIEDENTRIES
DESCRIPTOR.message_types_by_name['Entry'] = _ENTRY
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['PutRequest'] = _PUTREQUEST
DESCRIPTOR.message_types_by_name['PutResponse'] = _PUTRESPONSE
DESCRIPTOR.message_types_by_name['DecryptionRequest'] = _DECRYPTIONREQUEST
DESCRIPTOR.message_types_by_name['DecryptionResponse'] = _DECRYPTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AbstractRequest = _reflection.GeneratedProtocolMessageType('AbstractRequest', (_message.Message,), {
  'DESCRIPTOR' : _ABSTRACTREQUEST,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:AbstractRequest)
  })
_sym_db.RegisterMessage(AbstractRequest)

AbstractResponse = _reflection.GeneratedProtocolMessageType('AbstractResponse', (_message.Message,), {
  'DESCRIPTOR' : _ABSTRACTRESPONSE,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:AbstractResponse)
  })
_sym_db.RegisterMessage(AbstractResponse)

UserAuthenticationRequest = _reflection.GeneratedProtocolMessageType('UserAuthenticationRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAUTHENTICATIONREQUEST,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:UserAuthenticationRequest)
  })
_sym_db.RegisterMessage(UserAuthenticationRequest)

UserAuthenticationResponse = _reflection.GeneratedProtocolMessageType('UserAuthenticationResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAUTHENTICATIONRESPONSE,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:UserAuthenticationResponse)
  })
_sym_db.RegisterMessage(UserAuthenticationResponse)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

QueriedEntries = _reflection.GeneratedProtocolMessageType('QueriedEntries', (_message.Message,), {
  'DESCRIPTOR' : _QUERIEDENTRIES,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:QueriedEntries)
  })
_sym_db.RegisterMessage(QueriedEntries)

Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
  'DESCRIPTOR' : _ENTRY,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:Entry)
  })
_sym_db.RegisterMessage(Entry)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTREQUEST,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:PutRequest)
  })
_sym_db.RegisterMessage(PutRequest)

PutResponse = _reflection.GeneratedProtocolMessageType('PutResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTRESPONSE,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:PutResponse)
  })
_sym_db.RegisterMessage(PutResponse)

DecryptionRequest = _reflection.GeneratedProtocolMessageType('DecryptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DECRYPTIONREQUEST,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:DecryptionRequest)
  })
_sym_db.RegisterMessage(DecryptionRequest)

DecryptionResponse = _reflection.GeneratedProtocolMessageType('DecryptionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DECRYPTIONRESPONSE,
  '__module__' : 'keymaster_pb2'
  # @@protoc_insertion_point(class_scope:DecryptionResponse)
  })
_sym_db.RegisterMessage(DecryptionResponse)



_KEYMASTER = _descriptor.ServiceDescriptor(
  name='Keymaster',
  full_name='Keymaster',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=826,
  serialized_end=1076,
  methods=[
  _descriptor.MethodDescriptor(
    name='AuthenticateUser',
    full_name='Keymaster.AuthenticateUser',
    index=0,
    containing_service=None,
    input_type=_USERAUTHENTICATIONREQUEST,
    output_type=_USERAUTHENTICATIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='Keymaster.Search',
    index=1,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_QUERIEDENTRIES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Decrypt',
    full_name='Keymaster.Decrypt',
    index=2,
    containing_service=None,
    input_type=_DECRYPTIONREQUEST,
    output_type=_DECRYPTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='Keymaster.Get',
    index=3,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Put',
    full_name='Keymaster.Put',
    index=4,
    containing_service=None,
    input_type=_PUTREQUEST,
    output_type=_PUTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYMASTER)

DESCRIPTOR.services_by_name['Keymaster'] = _KEYMASTER

# @@protoc_insertion_point(module_scope)
