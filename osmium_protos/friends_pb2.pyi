import types_pb2 as _types_pb2
import refs_pb2 as _refs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRelationships(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Relationships(_message.Message):
    __slots__ = ("relationships", "users")
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    relationships: _containers.RepeatedCompositeFieldContainer[_types_pb2.Relationship]
    users: _containers.RepeatedCompositeFieldContainer[_types_pb2.User]
    def __init__(self, relationships: _Optional[_Iterable[_Union[_types_pb2.Relationship, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_types_pb2.User, _Mapping]]] = ...) -> None: ...

class SyncFriends(_message.Message):
    __slots__ = ("platform_user_id", "hashed_platform_user_id", "platform_user_name", "platform", "friend_ids_hashed", "community_ids_hashed")
    PLATFORM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    HASHED_PLATFORM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    FRIEND_IDS_HASHED_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_IDS_HASHED_FIELD_NUMBER: _ClassVar[int]
    platform_user_id: str
    hashed_platform_user_id: bytes
    platform_user_name: str
    platform: str
    friend_ids_hashed: _containers.RepeatedScalarFieldContainer[bytes]
    community_ids_hashed: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, platform_user_id: _Optional[str] = ..., hashed_platform_user_id: _Optional[bytes] = ..., platform_user_name: _Optional[str] = ..., platform: _Optional[str] = ..., friend_ids_hashed: _Optional[_Iterable[bytes]] = ..., community_ids_hashed: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ChangeRelationship(_message.Message):
    __slots__ = ("user", "change")
    class RelationshipChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[ChangeRelationship.RelationshipChangeType]
        REQUEST_FRIEND: _ClassVar[ChangeRelationship.RelationshipChangeType]
        ACCEPT_FRIEND: _ClassVar[ChangeRelationship.RelationshipChangeType]
        REMOVE_FRIEND: _ClassVar[ChangeRelationship.RelationshipChangeType]
        BLOCK: _ClassVar[ChangeRelationship.RelationshipChangeType]
        UNBLOCK: _ClassVar[ChangeRelationship.RelationshipChangeType]
    INVALID: ChangeRelationship.RelationshipChangeType
    REQUEST_FRIEND: ChangeRelationship.RelationshipChangeType
    ACCEPT_FRIEND: ChangeRelationship.RelationshipChangeType
    REMOVE_FRIEND: ChangeRelationship.RelationshipChangeType
    BLOCK: ChangeRelationship.RelationshipChangeType
    UNBLOCK: ChangeRelationship.RelationshipChangeType
    USER_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    user: _refs_pb2.UserRef
    change: ChangeRelationship.RelationshipChangeType
    def __init__(self, user: _Optional[_Union[_refs_pb2.UserRef, _Mapping]] = ..., change: _Optional[_Union[ChangeRelationship.RelationshipChangeType, str]] = ...) -> None: ...
