import types_pb2 as _types_pb2
import refs_pb2 as _refs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TypingAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPING: _ClassVar[TypingAction]
    UPLOAD_IMAGE: _ClassVar[TypingAction]
    UPLOAD_VIDEO: _ClassVar[TypingAction]
    UPLOAD_FILE: _ClassVar[TypingAction]
    RECORDING_AUDIO: _ClassVar[TypingAction]
    RECORDING_VIDEO: _ClassVar[TypingAction]
TYPING: TypingAction
UPLOAD_IMAGE: TypingAction
UPLOAD_VIDEO: TypingAction
UPLOAD_FILE: TypingAction
RECORDING_AUDIO: TypingAction
RECORDING_VIDEO: TypingAction

class GetChats(_message.Message):
    __slots__ = ("limit", "max_id", "min_id")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    MAX_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_ID_FIELD_NUMBER: _ClassVar[int]
    limit: int
    max_id: int
    min_id: int
    def __init__(self, limit: _Optional[int] = ..., max_id: _Optional[int] = ..., min_id: _Optional[int] = ...) -> None: ...

class Chats(_message.Message):
    __slots__ = ("chats", "users", "groups", "channels", "messages")
    CHATS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    chats: _containers.RepeatedCompositeFieldContainer[_types_pb2.Conversation]
    users: _containers.RepeatedCompositeFieldContainer[_types_pb2.User]
    groups: _containers.RepeatedCompositeFieldContainer[_types_pb2.Group]
    channels: _containers.RepeatedCompositeFieldContainer[_types_pb2.Channel]
    messages: _containers.RepeatedCompositeFieldContainer[_types_pb2.Message]
    def __init__(self, chats: _Optional[_Iterable[_Union[_types_pb2.Conversation, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_types_pb2.User, _Mapping]]] = ..., groups: _Optional[_Iterable[_Union[_types_pb2.Group, _Mapping]]] = ..., channels: _Optional[_Iterable[_Union[_types_pb2.Channel, _Mapping]]] = ..., messages: _Optional[_Iterable[_Union[_types_pb2.Message, _Mapping]]] = ...) -> None: ...

class GetChat(_message.Message):
    __slots__ = ("chat_ref",)
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ...) -> None: ...

class Chat(_message.Message):
    __slots__ = ("chat", "message", "users", "group", "channel")
    CHAT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    chat: _types_pb2.Conversation
    message: _types_pb2.Message
    users: _containers.RepeatedCompositeFieldContainer[_types_pb2.User]
    group: _types_pb2.Group
    channel: _types_pb2.Channel
    def __init__(self, chat: _Optional[_Union[_types_pb2.Conversation, _Mapping]] = ..., message: _Optional[_Union[_types_pb2.Message, _Mapping]] = ..., users: _Optional[_Iterable[_Union[_types_pb2.User, _Mapping]]] = ..., group: _Optional[_Union[_types_pb2.Group, _Mapping]] = ..., channel: _Optional[_Union[_types_pb2.Channel, _Mapping]] = ...) -> None: ...

class CreateChatInvite(_message.Message):
    __slots__ = ("chat_ref", "expires_at", "max_uses")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    MAX_USES_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    expires_at: int
    max_uses: int
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., expires_at: _Optional[int] = ..., max_uses: _Optional[int] = ...) -> None: ...

class ListChatInvites(_message.Message):
    __slots__ = ("chat_ref",)
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ...) -> None: ...

class DeleteChatInvite(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class MarkChatRead(_message.Message):
    __slots__ = ("chat_ref", "message_id", "read_amount")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    READ_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    message_id: int
    read_amount: int
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., message_id: _Optional[int] = ..., read_amount: _Optional[int] = ...) -> None: ...

class SetTyping(_message.Message):
    __slots__ = ("chat_ref", "typing", "action")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    TYPING_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    typing: bool
    action: TypingAction
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., typing: _Optional[bool] = ..., action: _Optional[_Union[TypingAction, str]] = ...) -> None: ...

class CreateChat(_message.Message):
    __slots__ = ("users", "name")
    USERS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_refs_pb2.UserRef]
    name: str
    def __init__(self, users: _Optional[_Iterable[_Union[_refs_pb2.UserRef, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateChat(_message.Message):
    __slots__ = ("chat_ref", "name", "highlighted_msg_id")
    class HighlightedMessage(_message.Message):
        __slots__ = ("highlighted_msg_id",)
        HIGHLIGHTED_MSG_ID_FIELD_NUMBER: _ClassVar[int]
        highlighted_msg_id: int
        def __init__(self, highlighted_msg_id: _Optional[int] = ...) -> None: ...
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHTED_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    name: str
    highlighted_msg_id: UpdateChat.HighlightedMessage
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., name: _Optional[str] = ..., highlighted_msg_id: _Optional[_Union[UpdateChat.HighlightedMessage, _Mapping]] = ...) -> None: ...

class RemoveChatMember(_message.Message):
    __slots__ = ("chat_ref", "user_id")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    user_id: int
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., user_id: _Optional[int] = ...) -> None: ...
