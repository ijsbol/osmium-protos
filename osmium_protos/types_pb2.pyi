import refs_pb2 as _refs_pb2
import media_pb2 as _media_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEXT: _ClassVar[ChannelType]
    VOICE: _ClassVar[ChannelType]
    CATEGORY: _ClassVar[ChannelType]

class NotifPrefs(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALL: _ClassVar[NotifPrefs]
    MENTIONS: _ClassVar[NotifPrefs]
    NONE: _ClassVar[NotifPrefs]
    DEFAULT: _ClassVar[NotifPrefs]

class CommunityPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_PERMISSION: _ClassVar[CommunityPermission]
    ADMINISTRATOR: _ClassVar[CommunityPermission]
    VIEW_CHANNEL: _ClassVar[CommunityPermission]
    SEND_MESSAGES: _ClassVar[CommunityPermission]
    CONNECT_VOICE: _ClassVar[CommunityPermission]
    MODIFY_CHANNEL: _ClassVar[CommunityPermission]
    SEND_MEDIA: _ClassVar[CommunityPermission]
    DELETE_MESSAGES: _ClassVar[CommunityPermission]
    PIN_MESSAGES: _ClassVar[CommunityPermission]
    SPEAK_VOICE: _ClassVar[CommunityPermission]
    MODIFY_COMMUNITY: _ClassVar[CommunityPermission]
    MODIFY_ROLES: _ClassVar[CommunityPermission]
    REMOVE_MEMBERS: _ClassVar[CommunityPermission]
    ADD_REACTIONS: _ClassVar[CommunityPermission]
    MODIFY_LINKED_STICKERS: _ClassVar[CommunityPermission]

class RelationshipStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID: _ClassVar[RelationshipStatus]
    FRIEND: _ClassVar[RelationshipStatus]
    FRIEND_REQUEST_INCOMING: _ClassVar[RelationshipStatus]
    FRIEND_REQUEST_OUTGOING: _ClassVar[RelationshipStatus]
    BLOCKED: _ClassVar[RelationshipStatus]
    SUGGESTED_FRIEND: _ClassVar[RelationshipStatus]
TEXT: ChannelType
VOICE: ChannelType
CATEGORY: ChannelType
ALL: NotifPrefs
MENTIONS: NotifPrefs
NONE: NotifPrefs
DEFAULT: NotifPrefs
NO_PERMISSION: CommunityPermission
ADMINISTRATOR: CommunityPermission
VIEW_CHANNEL: CommunityPermission
SEND_MESSAGES: CommunityPermission
CONNECT_VOICE: CommunityPermission
MODIFY_CHANNEL: CommunityPermission
SEND_MEDIA: CommunityPermission
DELETE_MESSAGES: CommunityPermission
PIN_MESSAGES: CommunityPermission
SPEAK_VOICE: CommunityPermission
MODIFY_COMMUNITY: CommunityPermission
MODIFY_ROLES: CommunityPermission
REMOVE_MEMBERS: CommunityPermission
ADD_REACTIONS: CommunityPermission
MODIFY_LINKED_STICKERS: CommunityPermission
INVALID: RelationshipStatus
FRIEND: RelationshipStatus
FRIEND_REQUEST_INCOMING: RelationshipStatus
FRIEND_REQUEST_OUTGOING: RelationshipStatus
BLOCKED: RelationshipStatus
SUGGESTED_FRIEND: RelationshipStatus

class User(_message.Message):
    __slots__ = ("id", "name", "username", "status", "photo", "bot", "icon", "color")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    BOT_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    username: str
    status: UserStatus
    photo: ChatPhoto
    bot: bool
    icon: int
    color: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., username: _Optional[str] = ..., status: _Optional[_Union[UserStatus, _Mapping]] = ..., photo: _Optional[_Union[ChatPhoto, _Mapping]] = ..., bot: _Optional[bool] = ..., icon: _Optional[int] = ..., color: _Optional[int] = ...) -> None: ...

class ChatPhoto(_message.Message):
    __slots__ = ("file_id", "preview")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    preview: bytes
    def __init__(self, file_id: _Optional[int] = ..., preview: _Optional[bytes] = ...) -> None: ...

class PermissionOverrides(_message.Message):
    __slots__ = ("pos", "neg")
    POS_FIELD_NUMBER: _ClassVar[int]
    NEG_FIELD_NUMBER: _ClassVar[int]
    pos: int
    neg: int
    def __init__(self, pos: _Optional[int] = ..., neg: _Optional[int] = ...) -> None: ...

class Conversation(_message.Message):
    __slots__ = ("chat_ref", "last_message_id", "last_read_message_id", "unread_count", "draft", "permissions", "notif_prefs", "unread_mentions_count")
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NOTIF_PREFS_FIELD_NUMBER: _ClassVar[int]
    UNREAD_MENTIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    last_message_id: int
    last_read_message_id: int
    unread_count: int
    draft: str
    permissions: PermissionOverrides
    notif_prefs: NotifPrefs
    unread_mentions_count: int
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., last_message_id: _Optional[int] = ..., last_read_message_id: _Optional[int] = ..., unread_count: _Optional[int] = ..., draft: _Optional[str] = ..., permissions: _Optional[_Union[PermissionOverrides, _Mapping]] = ..., notif_prefs: _Optional[_Union[NotifPrefs, str]] = ..., unread_mentions_count: _Optional[int] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("id", "name", "owner", "participant_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_IDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    owner: bool
    participant_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., owner: _Optional[bool] = ..., participant_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("chat_ref", "message_id", "author_id", "message", "reply_to", "media", "entities", "edited_at", "type", "forward")
    class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Message.MessageType]
        CALL: _ClassVar[Message.MessageType]
        JOIN: _ClassVar[Message.MessageType]
        LEAVE: _ClassVar[Message.MessageType]
    UNKNOWN: Message.MessageType
    CALL: Message.MessageType
    JOIN: Message.MessageType
    LEAVE: Message.MessageType
    class MessageForwardInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    EDITED_AT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FORWARD_FIELD_NUMBER: _ClassVar[int]
    chat_ref: _refs_pb2.ChatRef
    message_id: int
    author_id: int
    message: str
    reply_to: int
    media: _containers.RepeatedCompositeFieldContainer[_media_pb2.MessageMedia]
    entities: _containers.RepeatedCompositeFieldContainer[MessageEntity]
    edited_at: int
    type: Message.MessageType
    forward: Message.MessageForwardInfo
    def __init__(self, chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., message_id: _Optional[int] = ..., author_id: _Optional[int] = ..., message: _Optional[str] = ..., reply_to: _Optional[int] = ..., media: _Optional[_Iterable[_Union[_media_pb2.MessageMedia, _Mapping]]] = ..., entities: _Optional[_Iterable[_Union[MessageEntity, _Mapping]]] = ..., edited_at: _Optional[int] = ..., type: _Optional[_Union[Message.MessageType, str]] = ..., forward: _Optional[_Union[Message.MessageForwardInfo, _Mapping]] = ...) -> None: ...

class MessageEntity(_message.Message):
    __slots__ = ("start_index", "length", "bold", "italic", "underline", "strikethrough", "code", "url", "spoiler", "pre", "textUrl", "custom_emoji", "user_mention", "username")
    class CustomEmojiEntity(_message.Message):
        __slots__ = ("emoji_id",)
        EMOJI_ID_FIELD_NUMBER: _ClassVar[int]
        emoji_id: int
        def __init__(self, emoji_id: _Optional[int] = ...) -> None: ...
    class TextUrlEntity(_message.Message):
        __slots__ = ("url",)
        URL_FIELD_NUMBER: _ClassVar[int]
        url: str
        def __init__(self, url: _Optional[str] = ...) -> None: ...
    class PreEntity(_message.Message):
        __slots__ = ("language",)
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        language: str
        def __init__(self, language: _Optional[str] = ...) -> None: ...
    class SpoilerEntity(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class UserMentionEntity(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    UNDERLINE_FIELD_NUMBER: _ClassVar[int]
    STRIKETHROUGH_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SPOILER_FIELD_NUMBER: _ClassVar[int]
    PRE_FIELD_NUMBER: _ClassVar[int]
    TEXTURL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EMOJI_FIELD_NUMBER: _ClassVar[int]
    USER_MENTION_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    start_index: int
    length: int
    bold: bool
    italic: bool
    underline: bool
    strikethrough: bool
    code: bool
    url: bool
    spoiler: MessageEntity.SpoilerEntity
    pre: MessageEntity.PreEntity
    textUrl: MessageEntity.TextUrlEntity
    custom_emoji: MessageEntity.CustomEmojiEntity
    user_mention: MessageEntity.UserMentionEntity
    username: bool
    def __init__(self, start_index: _Optional[int] = ..., length: _Optional[int] = ..., bold: _Optional[bool] = ..., italic: _Optional[bool] = ..., underline: _Optional[bool] = ..., strikethrough: _Optional[bool] = ..., code: _Optional[bool] = ..., url: _Optional[bool] = ..., spoiler: _Optional[_Union[MessageEntity.SpoilerEntity, _Mapping]] = ..., pre: _Optional[_Union[MessageEntity.PreEntity, _Mapping]] = ..., textUrl: _Optional[_Union[MessageEntity.TextUrlEntity, _Mapping]] = ..., custom_emoji: _Optional[_Union[MessageEntity.CustomEmojiEntity, _Mapping]] = ..., user_mention: _Optional[_Union[MessageEntity.UserMentionEntity, _Mapping]] = ..., username: _Optional[bool] = ...) -> None: ...

class Channel(_message.Message):
    __slots__ = ("id", "community_id", "name", "type", "position", "parent_id", "flags", "highlighted_msg_id")
    class ChannelFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Channel.ChannelFlag]
        EXPLICIT: _ClassVar[Channel.ChannelFlag]
    NONE: Channel.ChannelFlag
    EXPLICIT: Channel.ChannelFlag
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHTED_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    community_id: int
    name: str
    type: ChannelType
    position: int
    parent_id: int
    flags: int
    highlighted_msg_id: int
    def __init__(self, id: _Optional[int] = ..., community_id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[ChannelType, str]] = ..., position: _Optional[int] = ..., parent_id: _Optional[int] = ..., flags: _Optional[int] = ..., highlighted_msg_id: _Optional[int] = ...) -> None: ...

class Community(_message.Message):
    __slots__ = ("id", "owner", "name", "photo", "permissions", "notif_prefs", "username")
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NOTIF_PREFS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    owner: bool
    name: str
    photo: ChatPhoto
    permissions: int
    notif_prefs: NotifPrefs
    username: str
    def __init__(self, id: _Optional[int] = ..., owner: _Optional[bool] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[ChatPhoto, _Mapping]] = ..., permissions: _Optional[int] = ..., notif_prefs: _Optional[_Union[NotifPrefs, str]] = ..., username: _Optional[str] = ...) -> None: ...

class Entrypoint(_message.Message):
    __slots__ = ("hostname", "ip_address", "port", "region")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    ip_address: str
    port: int
    region: int
    def __init__(self, hostname: _Optional[str] = ..., ip_address: _Optional[str] = ..., port: _Optional[int] = ..., region: _Optional[int] = ...) -> None: ...

class UserStatus(_message.Message):
    __slots__ = ("online", "status", "activities")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ONLINE: _ClassVar[UserStatus.Status]
        IDLE: _ClassVar[UserStatus.Status]
    ONLINE: UserStatus.Status
    IDLE: UserStatus.Status
    class Activity(_message.Message):
        __slots__ = ("title", "type", "start_time", "end_time", "state")
        class ActivityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CUSTOM: _ClassVar[UserStatus.Activity.ActivityType]
            PLAYING: _ClassVar[UserStatus.Activity.ActivityType]
            LISTENING: _ClassVar[UserStatus.Activity.ActivityType]
            WATCHING: _ClassVar[UserStatus.Activity.ActivityType]
        CUSTOM: UserStatus.Activity.ActivityType
        PLAYING: UserStatus.Activity.ActivityType
        LISTENING: UserStatus.Activity.ActivityType
        WATCHING: UserStatus.Activity.ActivityType
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        title: str
        type: UserStatus.Activity.ActivityType
        start_time: int
        end_time: int
        state: str
        def __init__(self, title: _Optional[str] = ..., type: _Optional[_Union[UserStatus.Activity.ActivityType, str]] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., state: _Optional[str] = ...) -> None: ...
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    online: bool
    status: UserStatus.Status
    activities: _containers.RepeatedCompositeFieldContainer[UserStatus.Activity]
    def __init__(self, online: _Optional[bool] = ..., status: _Optional[_Union[UserStatus.Status, str]] = ..., activities: _Optional[_Iterable[_Union[UserStatus.Activity, _Mapping]]] = ...) -> None: ...

class CommunityMember(_message.Message):
    __slots__ = ("id", "community_id", "role_ids", "nickname")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    community_id: int
    role_ids: _containers.RepeatedScalarFieldContainer[int]
    nickname: str
    def __init__(self, id: _Optional[int] = ..., community_id: _Optional[int] = ..., role_ids: _Optional[_Iterable[int]] = ..., nickname: _Optional[str] = ...) -> None: ...

class CommunityRole(_message.Message):
    __slots__ = ("id", "community_id", "name", "permissions", "priority", "color", "separated", "public")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SEPARATED_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    id: int
    community_id: int
    name: str
    permissions: int
    priority: int
    color: int
    separated: bool
    public: bool
    def __init__(self, id: _Optional[int] = ..., community_id: _Optional[int] = ..., name: _Optional[str] = ..., permissions: _Optional[int] = ..., priority: _Optional[int] = ..., color: _Optional[int] = ..., separated: _Optional[bool] = ..., public: _Optional[bool] = ...) -> None: ...

class ChannelOverride(_message.Message):
    __slots__ = ("community_id", "channel_id", "role_id", "permissions")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    channel_id: int
    role_id: int
    permissions: PermissionOverrides
    def __init__(self, community_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., role_id: _Optional[int] = ..., permissions: _Optional[_Union[PermissionOverrides, _Mapping]] = ...) -> None: ...

class Relationship(_message.Message):
    __slots__ = ("user_id", "status")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    status: RelationshipStatus
    def __init__(self, user_id: _Optional[int] = ..., status: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...
