# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: speech-v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import speech_types_pb2 as speech__types__pb2

from speech_types_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='speech-v1.proto',
  package='rokid.open.speech.v1',
  syntax='proto2',
  serialized_pb=_b('\n\x0fspeech-v1.proto\x12\x14rokid.open.speech.v1\x1a\x12speech_types.proto\"\xbf\x01\n\rSpeechRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12+\n\x04type\x18\x02 \x02(\x0e\x32\x1d.rokid.open.speech.v1.ReqType\x12\r\n\x05voice\x18\x03 \x01(\x0c\x12\x0b\n\x03\x61sr\x18\x04 \x01(\t\x12\x0c\n\x04lang\x18\x05 \x01(\t\x12\r\n\x05\x63odec\x18\x06 \x01(\t\x12\n\n\x02vt\x18\x07 \x01(\t\x12\x19\n\x11\x66ramework_options\x18\x08 \x01(\t\x12\x15\n\rskill_options\x18\t \x01(\t\"\x9c\x01\n\x0eSpeechResponse\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x35\n\x06result\x18\x02 \x02(\x0e\x32%.rokid.open.speech.v1.SpeechErrorCode\x12\x0b\n\x03\x61sr\x18\x03 \x01(\t\x12\x0b\n\x03nlp\x18\x04 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x05 \x01(\t\x12\x0e\n\x06\x66inish\x18\x06 \x01(\x08\x12\r\n\x05\x65xtra\x18\x07 \x01(\tP\x00')
  ,
  dependencies=[speech__types__pb2.DESCRIPTOR,],
  public_dependencies=[speech__types__pb2.DESCRIPTOR,])




_SPEECHREQUEST = _descriptor.Descriptor(
  name='SpeechRequest',
  full_name='rokid.open.speech.v1.SpeechRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rokid.open.speech.v1.SpeechRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='rokid.open.speech.v1.SpeechRequest.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voice', full_name='rokid.open.speech.v1.SpeechRequest.voice', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='asr', full_name='rokid.open.speech.v1.SpeechRequest.asr', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lang', full_name='rokid.open.speech.v1.SpeechRequest.lang', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='codec', full_name='rokid.open.speech.v1.SpeechRequest.codec', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vt', full_name='rokid.open.speech.v1.SpeechRequest.vt', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='framework_options', full_name='rokid.open.speech.v1.SpeechRequest.framework_options', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skill_options', full_name='rokid.open.speech.v1.SpeechRequest.skill_options', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=253,
)


_SPEECHRESPONSE = _descriptor.Descriptor(
  name='SpeechResponse',
  full_name='rokid.open.speech.v1.SpeechResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rokid.open.speech.v1.SpeechResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='rokid.open.speech.v1.SpeechResponse.result', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='asr', full_name='rokid.open.speech.v1.SpeechResponse.asr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nlp', full_name='rokid.open.speech.v1.SpeechResponse.nlp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='rokid.open.speech.v1.SpeechResponse.action', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finish', full_name='rokid.open.speech.v1.SpeechResponse.finish', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra', full_name='rokid.open.speech.v1.SpeechResponse.extra', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=412,
)

_SPEECHREQUEST.fields_by_name['type'].enum_type = speech__types__pb2._REQTYPE
_SPEECHRESPONSE.fields_by_name['result'].enum_type = speech__types__pb2._SPEECHERRORCODE
DESCRIPTOR.message_types_by_name['SpeechRequest'] = _SPEECHREQUEST
DESCRIPTOR.message_types_by_name['SpeechResponse'] = _SPEECHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpeechRequest = _reflection.GeneratedProtocolMessageType('SpeechRequest', (_message.Message,), dict(
  DESCRIPTOR = _SPEECHREQUEST,
  __module__ = 'speech_v1_pb2'
  # @@protoc_insertion_point(class_scope:rokid.open.speech.v1.SpeechRequest)
  ))
_sym_db.RegisterMessage(SpeechRequest)

SpeechResponse = _reflection.GeneratedProtocolMessageType('SpeechResponse', (_message.Message,), dict(
  DESCRIPTOR = _SPEECHRESPONSE,
  __module__ = 'speech_v1_pb2'
  # @@protoc_insertion_point(class_scope:rokid.open.speech.v1.SpeechResponse)
  ))
_sym_db.RegisterMessage(SpeechResponse)


# @@protoc_insertion_point(module_scope)