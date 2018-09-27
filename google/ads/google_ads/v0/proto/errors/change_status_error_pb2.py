# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/change_status_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/change_status_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n>google/ads/googleads_v0/proto/errors/change_status_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"z\n\x15\x43hangeStatusErrorEnum\"a\n\x11\x43hangeStatusError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12INVALID_START_DATE\x10\x02\x12\x16\n\x12START_DATE_TOO_OLD\x10\x03\x42\xcc\x01\n\"com.google.ads.googleads.v0.errorsB\x16\x43hangeStatusErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_CHANGESTATUSERRORENUM_CHANGESTATUSERROR = _descriptor.EnumDescriptor(
  name='ChangeStatusError',
  full_name='google.ads.googleads.v0.errors.ChangeStatusErrorEnum.ChangeStatusError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_START_DATE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_DATE_TOO_OLD', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=123,
  serialized_end=220,
)
_sym_db.RegisterEnumDescriptor(_CHANGESTATUSERRORENUM_CHANGESTATUSERROR)


_CHANGESTATUSERRORENUM = _descriptor.Descriptor(
  name='ChangeStatusErrorEnum',
  full_name='google.ads.googleads.v0.errors.ChangeStatusErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHANGESTATUSERRORENUM_CHANGESTATUSERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=220,
)

_CHANGESTATUSERRORENUM_CHANGESTATUSERROR.containing_type = _CHANGESTATUSERRORENUM
DESCRIPTOR.message_types_by_name['ChangeStatusErrorEnum'] = _CHANGESTATUSERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChangeStatusErrorEnum = _reflection.GeneratedProtocolMessageType('ChangeStatusErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _CHANGESTATUSERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.change_status_error_pb2'
  ,
  __doc__ = """Container for enum describing possible change status errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.ChangeStatusErrorEnum)
  ))
_sym_db.RegisterMessage(ChangeStatusErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\026ChangeStatusErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)