import refs_pb2 as _refs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoomInfo(_message.Message):
    __slots__ = ("room_id", "chat_ref", "endpoint", "token")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    room_id: int
    chat_ref: _refs_pb2.ChatRef
    endpoint: str
    token: str
    def __init__(self, room_id: _Optional[int] = ..., chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., endpoint: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class RoomParticipant(_message.Message):
    __slots__ = ("room_id", "session_id", "user_id", "muted", "deafened", "video_available", "screen_available")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    DEAFENED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SCREEN_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    room_id: int
    session_id: str
    user_id: int
    muted: bool
    deafened: bool
    video_available: bool
    screen_available: bool
    def __init__(self, room_id: _Optional[int] = ..., session_id: _Optional[str] = ..., user_id: _Optional[int] = ..., muted: _Optional[bool] = ..., deafened: _Optional[bool] = ..., video_available: _Optional[bool] = ..., screen_available: _Optional[bool] = ...) -> None: ...

class RequestRoom(_message.Message):
    __slots__ = ("chat_ref",)
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ...) -> None: ...

class UpdateRoomState(_message.Message):
    __slots__ = ("chat_ref", "state")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    state: RoomState
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., state: _Optional[_Union[RoomState, _Mapping]] = ...) -> None: ...

class RoomState(_message.Message):
    __slots__ = ("room_id", "participants")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    room_id: int
    participants: _containers.RepeatedCompositeFieldContainer[RoomParticipant]
    def __init__(self, room_id: _Optional[int] = ..., participants: _Optional[_Iterable[_Union[RoomParticipant, _Mapping]]] = ...) -> None: ...

class UpdateRoomParticipant(_message.Message):
    __slots__ = ("chat_ref", "participant")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    participant: RoomParticipant
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., participant: _Optional[_Union[RoomParticipant, _Mapping]] = ...) -> None: ...
