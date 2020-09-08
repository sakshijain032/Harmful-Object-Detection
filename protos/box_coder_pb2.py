# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/box_coder.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import faster_rcnn_box_coder_pb2 as object__detection_dot_protos_dot_faster__rcnn__box__coder__pb2
from protos import keypoint_box_coder_pb2 as object__detection_dot_protos_dot_keypoint__box__coder__pb2
from protos import mean_stddev_box_coder_pb2 as object__detection_dot_protos_dot_mean__stddev__box__coder__pb2
from protos import square_box_coder_pb2 as object__detection_dot_protos_dot_square__box__coder__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/box_coder.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\'object_detection/protos/box_coder.proto\x12\x17object_detection.protos\x1a\x33object_detection/protos/faster_rcnn_box_coder.proto\x1a\x30object_detection/protos/keypoint_box_coder.proto\x1a\x33object_detection/protos/mean_stddev_box_coder.proto\x1a.object_detection/protos/square_box_coder.proto\"\xc7\x02\n\x08\x42oxCoder\x12L\n\x15\x66\x61ster_rcnn_box_coder\x18\x01 \x01(\x0b\x32+.object_detection.protos.FasterRcnnBoxCoderH\x00\x12L\n\x15mean_stddev_box_coder\x18\x02 \x01(\x0b\x32+.object_detection.protos.MeanStddevBoxCoderH\x00\x12\x43\n\x10square_box_coder\x18\x03 \x01(\x0b\x32\'.object_detection.protos.SquareBoxCoderH\x00\x12G\n\x12keypoint_box_coder\x18\x04 \x01(\x0b\x32).object_detection.protos.KeypointBoxCoderH\x00\x42\x11\n\x0f\x62ox_coder_oneof'
  ,
  dependencies=[object__detection_dot_protos_dot_faster__rcnn__box__coder__pb2.DESCRIPTOR,object__detection_dot_protos_dot_keypoint__box__coder__pb2.DESCRIPTOR,object__detection_dot_protos_dot_mean__stddev__box__coder__pb2.DESCRIPTOR,object__detection_dot_protos_dot_square__box__coder__pb2.DESCRIPTOR,])




_BOXCODER = _descriptor.Descriptor(
  name='BoxCoder',
  full_name='object_detection.protos.BoxCoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faster_rcnn_box_coder', full_name='object_detection.protos.BoxCoder.faster_rcnn_box_coder', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_stddev_box_coder', full_name='object_detection.protos.BoxCoder.mean_stddev_box_coder', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='square_box_coder', full_name='object_detection.protos.BoxCoder.square_box_coder', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keypoint_box_coder', full_name='object_detection.protos.BoxCoder.keypoint_box_coder', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='box_coder_oneof', full_name='object_detection.protos.BoxCoder.box_coder_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=273,
  serialized_end=600,
)

_BOXCODER.fields_by_name['faster_rcnn_box_coder'].message_type = object__detection_dot_protos_dot_faster__rcnn__box__coder__pb2._FASTERRCNNBOXCODER
_BOXCODER.fields_by_name['mean_stddev_box_coder'].message_type = object__detection_dot_protos_dot_mean__stddev__box__coder__pb2._MEANSTDDEVBOXCODER
_BOXCODER.fields_by_name['square_box_coder'].message_type = object__detection_dot_protos_dot_square__box__coder__pb2._SQUAREBOXCODER
_BOXCODER.fields_by_name['keypoint_box_coder'].message_type = object__detection_dot_protos_dot_keypoint__box__coder__pb2._KEYPOINTBOXCODER
_BOXCODER.oneofs_by_name['box_coder_oneof'].fields.append(
  _BOXCODER.fields_by_name['faster_rcnn_box_coder'])
_BOXCODER.fields_by_name['faster_rcnn_box_coder'].containing_oneof = _BOXCODER.oneofs_by_name['box_coder_oneof']
_BOXCODER.oneofs_by_name['box_coder_oneof'].fields.append(
  _BOXCODER.fields_by_name['mean_stddev_box_coder'])
_BOXCODER.fields_by_name['mean_stddev_box_coder'].containing_oneof = _BOXCODER.oneofs_by_name['box_coder_oneof']
_BOXCODER.oneofs_by_name['box_coder_oneof'].fields.append(
  _BOXCODER.fields_by_name['square_box_coder'])
_BOXCODER.fields_by_name['square_box_coder'].containing_oneof = _BOXCODER.oneofs_by_name['box_coder_oneof']
_BOXCODER.oneofs_by_name['box_coder_oneof'].fields.append(
  _BOXCODER.fields_by_name['keypoint_box_coder'])
_BOXCODER.fields_by_name['keypoint_box_coder'].containing_oneof = _BOXCODER.oneofs_by_name['box_coder_oneof']
DESCRIPTOR.message_types_by_name['BoxCoder'] = _BOXCODER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BoxCoder = _reflection.GeneratedProtocolMessageType('BoxCoder', (_message.Message,), {
  'DESCRIPTOR' : _BOXCODER,
  '__module__' : 'object_detection.protos.box_coder_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.BoxCoder)
  })
_sym_db.RegisterMessage(BoxCoder)


# @@protoc_insertion_point(module_scope)
