from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatRef(_message.Message):
    __slots__ = ("user", "channel", "group", "self")
    USER_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    user: UserRef
    channel: ChannelRef
    group: GroupRef
    self: RefSelf
    def __init__(self_, user: _Optional[_Union[UserRef, _Mapping]] = ..., channel: _Optional[_Union[ChannelRef, _Mapping]] = ..., group: _Optional[_Union[GroupRef, _Mapping]] = ..., self: _Optional[_Union[RefSelf, _Mapping]] = ...) -> None: ...

class UserRef(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class RefSelf(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChannelRef(_message.Message):
    __slots__ = ("community_id", "channel_id")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    channel_id: int
    def __init__(self, community_id: _Optional[int] = ..., channel_id: _Optional[int] = ...) -> None: ...

class GroupRef(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class StickerPackRef(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
