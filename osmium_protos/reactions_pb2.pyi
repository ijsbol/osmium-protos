import refs_pb2 as _refs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddReaction(_message.Message):
    __slots__ = ("chat_ref", "message_id", "emoji")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    message_id: int
    emoji: ReactionEmoji
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., message_id: _Optional[int] = ..., emoji: _Optional[_Union[ReactionEmoji, _Mapping]] = ...) -> None: ...

class RemoveReaction(_message.Message):
    __slots__ = ("chat_ref", "message_id", "emoji")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    message_id: int
    emoji: ReactionEmoji
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., message_id: _Optional[int] = ..., emoji: _Optional[_Union[ReactionEmoji, _Mapping]] = ...) -> None: ...

class ReactionEmoji(_message.Message):
    __slots__ = ("unicode_emoji", "custom_emoji")
    UNICODE_EMOJI_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EMOJI_FIELD_NUMBER: _ClassVar[int]
    unicode_emoji: str
    custom_emoji: int
    def __init__(self, unicode_emoji: _Optional[str] = ..., custom_emoji: _Optional[int] = ...) -> None: ...

class MessageReactions(_message.Message):
    __slots__ = ("message_id", "reaction_fields")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    reaction_fields: _containers.RepeatedCompositeFieldContainer[MessageReactionField]
    def __init__(self, message_id: _Optional[int] = ..., reaction_fields: _Optional[_Iterable[_Union[MessageReactionField, _Mapping]]] = ...) -> None: ...

class MessageReactionField(_message.Message):
    __slots__ = ("emoji", "count", "me", "preview_user_ids")
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ME_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    emoji: ReactionEmoji
    count: int
    me: bool
    preview_user_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, emoji: _Optional[_Union[ReactionEmoji, _Mapping]] = ..., count: _Optional[int] = ..., me: _Optional[bool] = ..., preview_user_ids: _Optional[_Iterable[int]] = ...) -> None: ...
