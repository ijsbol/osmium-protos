import types_pb2 as _types_pb2
import refs_pb2 as _refs_pb2
import media_pb2 as _media_pb2
import reactions_pb2 as _reactions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendMessage(_message.Message):
    __slots__ = ("chat_ref", "message", "reply_to", "media", "entities")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    message: str
    reply_to: int
    media: _containers.RepeatedCompositeFieldContainer[_media_pb2.MediaRef]
    entities: _containers.RepeatedCompositeFieldContainer[_types_pb2.MessageEntity]
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., message: _Optional[str] = ..., reply_to: _Optional[int] = ..., media: _Optional[_Iterable[_Union[_media_pb2.MediaRef, _Mapping]]] = ..., entities: _Optional[_Iterable[_Union[_types_pb2.MessageEntity, _Mapping]]] = ...) -> None: ...

class SentMessage(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    def __init__(self, message_id: _Optional[int] = ...) -> None: ...

class EditMessage(_message.Message):
    __slots__ = ("chat_ref", "message_id", "message", "remove_media", "media", "entities")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_MEDIA_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    message_id: int
    message: str
    remove_media: bool
    media: _containers.RepeatedCompositeFieldContainer[_media_pb2.MediaRef]
    entities: _containers.RepeatedCompositeFieldContainer[_types_pb2.MessageEntity]
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., message_id: _Optional[int] = ..., message: _Optional[str] = ..., remove_media: _Optional[bool] = ..., media: _Optional[_Iterable[_Union[_media_pb2.MediaRef, _Mapping]]] = ..., entities: _Optional[_Iterable[_Union[_types_pb2.MessageEntity, _Mapping]]] = ...) -> None: ...

class ForwardMessage(_message.Message):
    __slots__ = ("chat_ref", "message_ids")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    message_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., message_ids: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class DeleteMessage(_message.Message):
    __slots__ = ("chat_ref", "message_ids")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    message_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., message_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class GetHistory(_message.Message):
    __slots__ = ("chat_ref", "limit", "since", "before", "around")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AROUND_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    limit: int
    since: int
    before: int
    around: int
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., limit: _Optional[int] = ..., since: _Optional[int] = ..., before: _Optional[int] = ..., around: _Optional[int] = ...) -> None: ...

class Messages(_message.Message):
    __slots__ = ("messages", "users", "members", "reactions")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_types_pb2.Message]
    users: _containers.RepeatedCompositeFieldContainer[_types_pb2.User]
    members: _containers.RepeatedCompositeFieldContainer[_types_pb2.CommunityMember]
    reactions: _containers.RepeatedCompositeFieldContainer[_reactions_pb2.MessageReactions]
    def __init__(self, messages: _Optional[_Iterable[_Union[_types_pb2.Message, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_types_pb2.User, _Mapping]]] = ..., members: _Optional[_Iterable[_Union[_types_pb2.CommunityMember, _Mapping]]] = ..., reactions: _Optional[_Iterable[_Union[_reactions_pb2.MessageReactions, _Mapping]]] = ...) -> None: ...

class Search(_message.Message):
    __slots__ = ("chat_ref", "query", "scoped", "since", "before")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SCOPED_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    query: str
    scoped: bool
    since: int
    before: int
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., query: _Optional[str] = ..., scoped: _Optional[bool] = ..., since: _Optional[int] = ..., before: _Optional[int] = ...) -> None: ...

class GetEmbedPreview(_message.Message):
    __slots__ = ("message", "entities")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    message: str
    entities: _containers.RepeatedCompositeFieldContainer[_types_pb2.MessageEntity]
    def __init__(self, message: _Optional[str] = ..., entities: _Optional[_Iterable[_Union[_types_pb2.MessageEntity, _Mapping]]] = ...) -> None: ...

class ReportMessage(_message.Message):
    __slots__ = ("message_id", "chat_ref", "reason")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    chat_ref: _refs_pb2.ChatRef
    reason: str
    def __init__(self, message_id: _Optional[int] = ..., chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...

class GetUnreadMentions(_message.Message):
    __slots__ = ("chat_ref",)
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ...) -> None: ...

class UnreadMentions(_message.Message):
    __slots__ = ("message_ids",)
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    message_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, message_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class SetMessagePin(_message.Message):
    __slots__ = ("chat_ref", "message_id", "pin")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    message_id: int
    pin: bool
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., message_id: _Optional[int] = ..., pin: _Optional[bool] = ...) -> None: ...

class GetPinnedMessages(_message.Message):
    __slots__ = ("chat_ref",)
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ...) -> None: ...
