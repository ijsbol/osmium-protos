import types_pb2 as _types_pb2
import refs_pb2 as _refs_pb2
import chats_pb2 as _chats_pb2
import voice_pb2 as _voice_pb2
import reactions_pb2 as _reactions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Update(_message.Message):
    __slots__ = ("message_created", "channel", "message_deleted", "user_status", "user", "community", "channel_deleted", "message", "chat_typing", "community_member", "community_deleted", "conversation_permissions", "chat", "session_deleted", "community_unavailable", "member_list", "community_member_deleted", "update_user_relationship", "update_user_relationship_deleted", "group", "room_state", "room_participant", "message_reactions", "conversation_last_read", "community_member_created")
    MESSAGE_CREATED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_DELETED_FIELD_NUMBER: _ClassVar[int]
    USER_STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_DELETED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHAT_TYPING_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_MEMBER_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_DELETED_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    SESSION_DELETED_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_LIST_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_MEMBER_DELETED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_USER_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_USER_RELATIONSHIP_DELETED_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ROOM_STATE_FIELD_NUMBER: _ClassVar[int]
    ROOM_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_REACTIONS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_LAST_READ_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_MEMBER_CREATED_FIELD_NUMBER: _ClassVar[int]
    message_created: UpdateMessageCreated
    channel: UpdateChannel
    message_deleted: UpdateMessageDeleted
    user_status: UpdateUserStatus
    user: UpdateUser
    community: UpdateCommunity
    channel_deleted: UpdateChannelDeleted
    message: UpdateMessage
    chat_typing: UpdateChatTyping
    community_member: UpdateCommunityMember
    community_deleted: UpdateCommunityDeleted
    conversation_permissions: UpdateConversationPermissions
    chat: UpdateChat
    session_deleted: UpdateSessionDeleted
    community_unavailable: UpdateCommunityUnavailable
    member_list: UpdateMemberList
    community_member_deleted: UpdateCommunityMemberDeleted
    update_user_relationship: UpdateUserRelationship
    update_user_relationship_deleted: UpdateUserRelationshipDeleted
    group: UpdateGroup
    room_state: _voice_pb2.UpdateRoomState
    room_participant: _voice_pb2.UpdateRoomParticipant
    message_reactions: UpdateMessageReactions
    conversation_last_read: UpdateConversationLastRead
    community_member_created: UpdateCommunityMemberCreated
    def __init__(self, message_created: _Optional[_Union[UpdateMessageCreated, _Mapping]] = ..., channel: _Optional[_Union[UpdateChannel, _Mapping]] = ..., message_deleted: _Optional[_Union[UpdateMessageDeleted, _Mapping]] = ..., user_status: _Optional[_Union[UpdateUserStatus, _Mapping]] = ..., user: _Optional[_Union[UpdateUser, _Mapping]] = ..., community: _Optional[_Union[UpdateCommunity, _Mapping]] = ..., channel_deleted: _Optional[_Union[UpdateChannelDeleted, _Mapping]] = ..., message: _Optional[_Union[UpdateMessage, _Mapping]] = ..., chat_typing: _Optional[_Union[UpdateChatTyping, _Mapping]] = ..., community_member: _Optional[_Union[UpdateCommunityMember, _Mapping]] = ..., community_deleted: _Optional[_Union[UpdateCommunityDeleted, _Mapping]] = ..., conversation_permissions: _Optional[_Union[UpdateConversationPermissions, _Mapping]] = ..., chat: _Optional[_Union[UpdateChat, _Mapping]] = ..., session_deleted: _Optional[_Union[UpdateSessionDeleted, _Mapping]] = ..., community_unavailable: _Optional[_Union[UpdateCommunityUnavailable, _Mapping]] = ..., member_list: _Optional[_Union[UpdateMemberList, _Mapping]] = ..., community_member_deleted: _Optional[_Union[UpdateCommunityMemberDeleted, _Mapping]] = ..., update_user_relationship: _Optional[_Union[UpdateUserRelationship, _Mapping]] = ..., update_user_relationship_deleted: _Optional[_Union[UpdateUserRelationshipDeleted, _Mapping]] = ..., group: _Optional[_Union[UpdateGroup, _Mapping]] = ..., room_state: _Optional[_Union[_voice_pb2.UpdateRoomState, _Mapping]] = ..., room_participant: _Optional[_Union[_voice_pb2.UpdateRoomParticipant, _Mapping]] = ..., message_reactions: _Optional[_Union[UpdateMessageReactions, _Mapping]] = ..., conversation_last_read: _Optional[_Union[UpdateConversationLastRead, _Mapping]] = ..., community_member_created: _Optional[_Union[UpdateCommunityMemberCreated, _Mapping]] = ...) -> None: ...

class UpdateMessageCreated(_message.Message):
    __slots__ = ("message", "channel_unread_count", "author")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    message: _types_pb2.Message
    channel_unread_count: int
    author: _types_pb2.User
    def __init__(self, message: _Optional[_Union[_types_pb2.Message, _Mapping]] = ..., channel_unread_count: _Optional[int] = ..., author: _Optional[_Union[_types_pb2.User, _Mapping]] = ...) -> None: ...

class UpdateMessage(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _types_pb2.Message
    def __init__(self, message: _Optional[_Union[_types_pb2.Message, _Mapping]] = ...) -> None: ...

class UpdateChannel(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: _types_pb2.Channel
    def __init__(self, channel: _Optional[_Union[_types_pb2.Channel, _Mapping]] = ...) -> None: ...

class UpdateChannelDeleted(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: _refs_pb2.ChannelRef
    def __init__(self, channel: _Optional[_Union[_refs_pb2.ChannelRef, _Mapping]] = ...) -> None: ...

class UpdateMessageDeleted(_message.Message):
    __slots__ = ("chat_ref", "message_ids")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    message_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., message_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdateUserStatus(_message.Message):
    __slots__ = ("user_id", "status")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    status: _types_pb2.UserStatus
    def __init__(self, user_id: _Optional[int] = ..., status: _Optional[_Union[_types_pb2.UserStatus, _Mapping]] = ...) -> None: ...

class UpdateUser(_message.Message):
    __slots__ = ("user_id", "user")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    user: _types_pb2.User
    def __init__(self, user_id: _Optional[int] = ..., user: _Optional[_Union[_types_pb2.User, _Mapping]] = ...) -> None: ...

class UpdateCommunity(_message.Message):
    __slots__ = ("community_id", "community")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    community: _types_pb2.Community
    def __init__(self, community_id: _Optional[int] = ..., community: _Optional[_Union[_types_pb2.Community, _Mapping]] = ...) -> None: ...

class UpdateCommunityDeleted(_message.Message):
    __slots__ = ("community_id",)
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    def __init__(self, community_id: _Optional[int] = ...) -> None: ...

class UpdateChatTyping(_message.Message):
    __slots__ = ("chat_ref", "user_id", "typing", "action")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPING_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    user_id: int
    typing: bool
    action: _chats_pb2.TypingAction
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., user_id: _Optional[int] = ..., typing: _Optional[bool] = ..., action: _Optional[_Union[_chats_pb2.TypingAction, str]] = ...) -> None: ...

class UpdateCommunityMember(_message.Message):
    __slots__ = ("community_id", "member_id", "member")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    member_id: int
    member: _types_pb2.CommunityMember
    def __init__(self, community_id: _Optional[int] = ..., member_id: _Optional[int] = ..., member: _Optional[_Union[_types_pb2.CommunityMember, _Mapping]] = ...) -> None: ...

class UpdateCommunityMemberDeleted(_message.Message):
    __slots__ = ("community_id", "member_id")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    member_id: int
    def __init__(self, community_id: _Optional[int] = ..., member_id: _Optional[int] = ...) -> None: ...

class UpdateCommunityMemberCreated(_message.Message):
    __slots__ = ("community_id", "member_id", "member", "user")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    member_id: int
    member: _types_pb2.CommunityMember
    user: _types_pb2.User
    def __init__(self, community_id: _Optional[int] = ..., member_id: _Optional[int] = ..., member: _Optional[_Union[_types_pb2.CommunityMember, _Mapping]] = ..., user: _Optional[_Union[_types_pb2.User, _Mapping]] = ...) -> None: ...

class UpdateConversationPermissions(_message.Message):
    __slots__ = ("chat_ref", "permissions")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    permissions: _types_pb2.PermissionOverrides
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., permissions: _Optional[_Union[_types_pb2.PermissionOverrides, _Mapping]] = ...) -> None: ...

class UpdateChat(_message.Message):
    __slots__ = ("chat",)
    CHAT_FIELD_NUMBER: _ClassVar[int]
    chat: _chats_pb2.Chat
    def __init__(self, chat: _Optional[_Union[_chats_pb2.Chat, _Mapping]] = ...) -> None: ...

class UpdateSessionDeleted(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class UpdateCommunityUnavailable(_message.Message):
    __slots__ = ("community_id",)
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    def __init__(self, community_id: _Optional[int] = ...) -> None: ...

class UpdateMemberList(_message.Message):
    __slots__ = ("community_id", "channel_id", "entries")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    channel_id: int
    entries: _containers.RepeatedCompositeFieldContainer[MemberListEntry]
    def __init__(self, community_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., entries: _Optional[_Iterable[_Union[MemberListEntry, _Mapping]]] = ...) -> None: ...

class MemberListEntry(_message.Message):
    __slots__ = ("user", "divider")
    USER_FIELD_NUMBER: _ClassVar[int]
    DIVIDER_FIELD_NUMBER: _ClassVar[int]
    user: MemberListEntryUser
    divider: MemberListEntryDivider
    def __init__(self, user: _Optional[_Union[MemberListEntryUser, _Mapping]] = ..., divider: _Optional[_Union[MemberListEntryDivider, _Mapping]] = ...) -> None: ...

class MemberListEntryUser(_message.Message):
    __slots__ = ("user", "nickname")
    USER_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    user: _types_pb2.User
    nickname: str
    def __init__(self, user: _Optional[_Union[_types_pb2.User, _Mapping]] = ..., nickname: _Optional[str] = ...) -> None: ...

class MemberListEntryDivider(_message.Message):
    __slots__ = ("online", "role_id", "member_count")
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    online: bool
    role_id: int
    member_count: int
    def __init__(self, online: _Optional[bool] = ..., role_id: _Optional[int] = ..., member_count: _Optional[int] = ...) -> None: ...

class UpdateUserRelationship(_message.Message):
    __slots__ = ("relationship",)
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    relationship: _types_pb2.Relationship
    def __init__(self, relationship: _Optional[_Union[_types_pb2.Relationship, _Mapping]] = ...) -> None: ...

class UpdateUserRelationshipDeleted(_message.Message):
    __slots__ = ("other_user_id",)
    OTHER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    other_user_id: int
    def __init__(self, other_user_id: _Optional[int] = ...) -> None: ...

class UpdateGroup(_message.Message):
    __slots__ = ("group", "users")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    group: _types_pb2.Group
    users: _containers.RepeatedCompositeFieldContainer[_types_pb2.User]
    def __init__(self, group: _Optional[_Union[_types_pb2.Group, _Mapping]] = ..., users: _Optional[_Iterable[_Union[_types_pb2.User, _Mapping]]] = ...) -> None: ...

class UpdateMessageReactions(_message.Message):
    __slots__ = ("chat_ref", "reactions")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    reactions: _reactions_pb2.MessageReactions
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., reactions: _Optional[_Union[_reactions_pb2.MessageReactions, _Mapping]] = ...) -> None: ...

class UpdateConversationLastRead(_message.Message):
    __slots__ = ("chat_ref", "last_read_message_id", "unread_count", "unread_mentions_count")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNREAD_MENTIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    last_read_message_id: int
    unread_count: int
    unread_mentions_count: int
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., last_read_message_id: _Optional[int] = ..., unread_count: _Optional[int] = ..., unread_mentions_count: _Optional[int] = ...) -> None: ...
