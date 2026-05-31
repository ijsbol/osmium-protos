import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDiscoverableCommunities(_message.Message):
    __slots__ = ("after", "limit")
    AFTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    after: int
    limit: int
    def __init__(self, after: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class DiscoveryCommunities(_message.Message):
    __slots__ = ("listings",)
    LISTINGS_FIELD_NUMBER: _ClassVar[int]
    listings: _containers.RepeatedCompositeFieldContainer[DiscoveryCommunityListing]
    def __init__(self, listings: _Optional[_Iterable[_Union[DiscoveryCommunityListing, _Mapping]]] = ...) -> None: ...

class DiscoveryCommunityListing(_message.Message):
    __slots__ = ("community_id", "name", "photo", "invite_code", "short_description", "long_description", "categories")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    INVITE_CODE_FIELD_NUMBER: _ClassVar[int]
    SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LONG_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    name: str
    photo: _types_pb2.ChatPhoto
    invite_code: str
    short_description: str
    long_description: str
    categories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, community_id: _Optional[int] = ..., name: _Optional[str] = ..., photo: _Optional[_Union[_types_pb2.ChatPhoto, _Mapping]] = ..., invite_code: _Optional[str] = ..., short_description: _Optional[str] = ..., long_description: _Optional[str] = ..., categories: _Optional[_Iterable[str]] = ...) -> None: ...

class DiscoveryListingInfo(_message.Message):
    __slots__ = ("short_description", "long_description", "categories")
    SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LONG_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    short_description: str
    long_description: str
    categories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, short_description: _Optional[str] = ..., long_description: _Optional[str] = ..., categories: _Optional[_Iterable[str]] = ...) -> None: ...
