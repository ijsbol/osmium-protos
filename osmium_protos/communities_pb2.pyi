import refs_pb2 as _refs_pb2
import types_pb2 as _types_pb2
import media_pb2 as _media_pb2
import updates_pb2 as _updates_pb2
import discovery_pb2 as _discovery_pb2
import voice_pb2 as _voice_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetCommunities(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommunityUserInfo(_message.Message):
    __slots__ = ("community_id", "unread_count", "unread_mention_count")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNREAD_MENTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    unread_count: int
    unread_mention_count: int
    def __init__(self, community_id: _Optional[int] = ..., unread_count: _Optional[int] = ..., unread_mention_count: _Optional[int] = ...) -> None: ...

class Communities(_message.Message):
    __slots__ = ("communities", "community_user_info", "unavailable")
    COMMUNITIES_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_USER_INFO_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    communities: _containers.RepeatedCompositeFieldContainer[_types_pb2.Community]
    community_user_info: _containers.RepeatedCompositeFieldContainer[CommunityUserInfo]
    unavailable: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, communities: _Optional[_Iterable[_Union[_types_pb2.Community, _Mapping]]] = ..., community_user_info: _Optional[_Iterable[_Union[CommunityUserInfo, _Mapping]]] = ..., unavailable: _Optional[_Iterable[int]] = ...) -> None: ...

class GetChannels(_message.Message):
    __slots__ = ("community_id",)
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    def __init__(self, community_id: _Optional[int] = ...) -> None: ...

class Channels(_message.Message):
    __slots__ = ("conversations", "channels", "messages")
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[_types_pb2.Conversation]
    channels: _containers.RepeatedCompositeFieldContainer[_types_pb2.Channel]
    messages: _containers.RepeatedCompositeFieldContainer[_types_pb2.Message]
    def __init__(self, conversations: _Optional[_Iterable[_Union[_types_pb2.Conversation, _Mapping]]] = ..., channels: _Optional[_Iterable[_Union[_types_pb2.Channel, _Mapping]]] = ..., messages: _Optional[_Iterable[_Union[_types_pb2.Message, _Mapping]]] = ...) -> None: ...

class CreateCommunity(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateChannel(_message.Message):
    __slots__ = ("community_id", "name", "type", "parent_id")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    name: str
    type: _types_pb2.ChannelType
    parent_id: int
    def __init__(self, community_id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_types_pb2.ChannelType, str]] = ..., parent_id: _Optional[int] = ...) -> None: ...

class DeleteChannel(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: _refs_pb2.ChannelRef
    def __init__(self, channel: _Optional[_Union[_refs_pb2.ChannelRef, _Mapping]] = ...) -> None: ...

class EditChannel(_message.Message):
    __slots__ = ("channel", "name", "position", "parent_id", "explicit", "highlighted_msg_id")
    class HighlightedMessage(_message.Message):
        __slots__ = ("highlighted_msg_id",)
        HIGHLIGHTED_MSG_ID_FIELD_NUMBER: _ClassVar[int]
        highlighted_msg_id: int
        def __init__(self, highlighted_msg_id: _Optional[int] = ...) -> None: ...
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHTED_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    channel: _refs_pb2.ChannelRef
    name: str
    position: int
    parent_id: int
    explicit: bool
    highlighted_msg_id: EditChannel.HighlightedMessage
    def __init__(self, channel: _Optional[_Union[_refs_pb2.ChannelRef, _Mapping]] = ..., name: _Optional[str] = ..., position: _Optional[int] = ..., parent_id: _Optional[int] = ..., explicit: _Optional[bool] = ..., highlighted_msg_id: _Optional[_Union[EditChannel.HighlightedMessage, _Mapping]] = ...) -> None: ...

class GetChannelMembers(_message.Message):
    __slots__ = ("community_id", "channel_id")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    channel_id: int
    def __init__(self, community_id: _Optional[int] = ..., channel_id: _Optional[int] = ...) -> None: ...

class Members(_message.Message):
    __slots__ = ("members", "users")
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_types_pb2.CommunityMember]
    users: _containers.RepeatedCompositeFieldContainer[_types_pb2.User]
    def __init__(self, members: _Optional[_Iterable[_Union[_types_pb2.CommunityMember, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_types_pb2.User, _Mapping]]] = ...) -> None: ...

class MemberList(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[_updates_pb2.MemberListEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[_updates_pb2.MemberListEntry, _Mapping]]] = ...) -> None: ...

class EditPhoto(_message.Message):
    __slots__ = ("community_id", "file")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    file: _media_pb2.UploadedFileRef
    def __init__(self, community_id: _Optional[int] = ..., file: _Optional[_Union[_media_pb2.UploadedFileRef, _Mapping]] = ...) -> None: ...

class GetRoles(_message.Message):
    __slots__ = ("community_id",)
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    def __init__(self, community_id: _Optional[int] = ...) -> None: ...

class CommunityRoles(_message.Message):
    __slots__ = ("roles", "default_permissions")
    ROLES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[_types_pb2.CommunityRole]
    default_permissions: int
    def __init__(self, roles: _Optional[_Iterable[_Union[_types_pb2.CommunityRole, _Mapping]]] = ..., default_permissions: _Optional[int] = ...) -> None: ...

class CreateRole(_message.Message):
    __slots__ = ("community_id", "name", "permissions", "priority", "color", "separated", "public")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SEPARATED_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    name: str
    permissions: int
    priority: int
    color: int
    separated: bool
    public: bool
    def __init__(self, community_id: _Optional[int] = ..., name: _Optional[str] = ..., permissions: _Optional[int] = ..., priority: _Optional[int] = ..., color: _Optional[int] = ..., separated: _Optional[bool] = ..., public: _Optional[bool] = ...) -> None: ...

class EditRole(_message.Message):
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

class DeleteRole(_message.Message):
    __slots__ = ("id", "community_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    community_id: int
    def __init__(self, id: _Optional[int] = ..., community_id: _Optional[int] = ...) -> None: ...

class EditMember(_message.Message):
    __slots__ = ("community_id", "member_id", "nickname", "role_ids")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    member_id: int
    nickname: str
    role_ids: CommunityMemberRoleIds
    def __init__(self, community_id: _Optional[int] = ..., member_id: _Optional[int] = ..., nickname: _Optional[str] = ..., role_ids: _Optional[_Union[CommunityMemberRoleIds, _Mapping]] = ...) -> None: ...

class CommunityMemberRoleIds(_message.Message):
    __slots__ = ("role_ids",)
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    role_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, role_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class GetChannelOverrides(_message.Message):
    __slots__ = ("community_id", "channel_id")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    channel_id: int
    def __init__(self, community_id: _Optional[int] = ..., channel_id: _Optional[int] = ...) -> None: ...

class ChannelOverrides(_message.Message):
    __slots__ = ("overrides",)
    OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    overrides: _containers.RepeatedCompositeFieldContainer[_types_pb2.ChannelOverride]
    def __init__(self, overrides: _Optional[_Iterable[_Union[_types_pb2.ChannelOverride, _Mapping]]] = ...) -> None: ...

class CreateChannelOverride(_message.Message):
    __slots__ = ("community_id", "channel_id", "role_id", "permissions")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    channel_id: int
    role_id: int
    permissions: _types_pb2.PermissionOverrides
    def __init__(self, community_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., role_id: _Optional[int] = ..., permissions: _Optional[_Union[_types_pb2.PermissionOverrides, _Mapping]] = ...) -> None: ...

class ChannelOverride(_message.Message):
    __slots__ = ("override",)
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    override: _types_pb2.ChannelOverride
    def __init__(self, override: _Optional[_Union[_types_pb2.ChannelOverride, _Mapping]] = ...) -> None: ...

class DeleteChannelOverride(_message.Message):
    __slots__ = ("community_id", "channel_id", "role_id")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    channel_id: int
    role_id: int
    def __init__(self, community_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., role_id: _Optional[int] = ...) -> None: ...

class LeaveCommunity(_message.Message):
    __slots__ = ("community_id",)
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    def __init__(self, community_id: _Optional[int] = ...) -> None: ...

class DeleteCommunity(_message.Message):
    __slots__ = ("community_id",)
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    def __init__(self, community_id: _Optional[int] = ...) -> None: ...

class EditCommunity(_message.Message):
    __slots__ = ("community_id", "name", "username")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    name: str
    username: str
    def __init__(self, community_id: _Optional[int] = ..., name: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class RemoveMembers(_message.Message):
    __slots__ = ("community_id", "member_ids", "until", "delete_messages_since", "reason")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    DELETE_MESSAGES_SINCE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    member_ids: _containers.RepeatedScalarFieldContainer[int]
    until: int
    delete_messages_since: int
    reason: str
    def __init__(self, community_id: _Optional[int] = ..., member_ids: _Optional[_Iterable[int]] = ..., until: _Optional[int] = ..., delete_messages_since: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class RemovedMembers(_message.Message):
    __slots__ = ("members",)
    class RemovedMember(_message.Message):
        __slots__ = ("user_id", "user", "until", "reason")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_FIELD_NUMBER: _ClassVar[int]
        UNTIL_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        user_id: int
        user: _types_pb2.User
        until: int
        reason: str
        def __init__(self, user_id: _Optional[int] = ..., user: _Optional[_Union[_types_pb2.User, _Mapping]] = ..., until: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[RemovedMembers.RemovedMember]
    def __init__(self, members: _Optional[_Iterable[_Union[RemovedMembers.RemovedMember, _Mapping]]] = ...) -> None: ...

class GetRemovedMembers(_message.Message):
    __slots__ = ("community_id",)
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    def __init__(self, community_id: _Optional[int] = ...) -> None: ...

class EditDefaultPermissions(_message.Message):
    __slots__ = ("community_id", "permissions")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    permissions: int
    def __init__(self, community_id: _Optional[int] = ..., permissions: _Optional[int] = ...) -> None: ...

class UnbanMembers(_message.Message):
    __slots__ = ("community_id", "member_ids")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    member_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, community_id: _Optional[int] = ..., member_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class GetMembers(_message.Message):
    __slots__ = ("community_id", "member_ids")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    member_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, community_id: _Optional[int] = ..., member_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class EditSettings(_message.Message):
    __slots__ = ("community_id", "settings")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    settings: CommunitySettings
    def __init__(self, community_id: _Optional[int] = ..., settings: _Optional[_Union[CommunitySettings, _Mapping]] = ...) -> None: ...

class CommunitySettings(_message.Message):
    __slots__ = ("system_messages", "discovery_listing")
    class SystemMessages(_message.Message):
        __slots__ = ("channel_id", "join_messages")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        JOIN_MESSAGES_FIELD_NUMBER: _ClassVar[int]
        channel_id: int
        join_messages: bool
        def __init__(self, channel_id: _Optional[int] = ..., join_messages: _Optional[bool] = ...) -> None: ...
    class DiscoveryListing(_message.Message):
        __slots__ = ("listed", "listing")
        LISTED_FIELD_NUMBER: _ClassVar[int]
        LISTING_FIELD_NUMBER: _ClassVar[int]
        listed: bool
        listing: _discovery_pb2.DiscoveryListingInfo
        def __init__(self, listed: _Optional[bool] = ..., listing: _Optional[_Union[_discovery_pb2.DiscoveryListingInfo, _Mapping]] = ...) -> None: ...
    SYSTEM_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_LISTING_FIELD_NUMBER: _ClassVar[int]
    system_messages: CommunitySettings.SystemMessages
    discovery_listing: CommunitySettings.DiscoveryListing
    def __init__(self, system_messages: _Optional[_Union[CommunitySettings.SystemMessages, _Mapping]] = ..., discovery_listing: _Optional[_Union[CommunitySettings.DiscoveryListing, _Mapping]] = ...) -> None: ...

class GetRoomStates(_message.Message):
    __slots__ = ("community_id",)
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    def __init__(self, community_id: _Optional[int] = ...) -> None: ...

class RoomStates(_message.Message):
    __slots__ = ("room_states",)
    class RoomState(_message.Message):
        __slots__ = ("channel_id", "state")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        channel_id: int
        state: _voice_pb2.RoomState
        def __init__(self, channel_id: _Optional[int] = ..., state: _Optional[_Union[_voice_pb2.RoomState, _Mapping]] = ...) -> None: ...
    ROOM_STATES_FIELD_NUMBER: _ClassVar[int]
    room_states: _containers.RepeatedCompositeFieldContainer[RoomStates.RoomState]
    def __init__(self, room_states: _Optional[_Iterable[_Union[RoomStates.RoomState, _Mapping]]] = ...) -> None: ...
