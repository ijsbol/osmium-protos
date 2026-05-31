import refs_pb2 as _refs_pb2
import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProfile(_message.Message):
    __slots__ = ("ref",)
    REF_FIELD_NUMBER: _ClassVar[int]
    ref: _refs_pb2.UserRef
    def __init__(self, ref: _Optional[_Union[_refs_pb2.UserRef, _Mapping]] = ...) -> None: ...

class Profile(_message.Message):
    __slots__ = ("ref", "bio", "premium_since")
    REF_FIELD_NUMBER: _ClassVar[int]
    BIO_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_SINCE_FIELD_NUMBER: _ClassVar[int]
    ref: _refs_pb2.UserRef
    bio: str
    premium_since: int
    def __init__(self, ref: _Optional[_Union[_refs_pb2.UserRef, _Mapping]] = ..., bio: _Optional[str] = ..., premium_since: _Optional[int] = ...) -> None: ...

class LookupUsername(_message.Message):
    __slots__ = ("username",)
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class UserDetails(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _types_pb2.User
    def __init__(self, user: _Optional[_Union[_types_pb2.User, _Mapping]] = ...) -> None: ...
