import media_pb2 as _media_pb2
import refs_pb2 as _refs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSavedStickers(_message.Message):
    __slots__ = ("since",)
    SINCE_FIELD_NUMBER: _ClassVar[int]
    since: int
    def __init__(self, since: _Optional[int] = ...) -> None: ...

class SavedStickers(_message.Message):
    __slots__ = ("saved_packs",)
    SAVED_PACKS_FIELD_NUMBER: _ClassVar[int]
    saved_packs: _containers.RepeatedCompositeFieldContainer[StickerPack]
    def __init__(self, saved_packs: _Optional[_Iterable[_Union[StickerPack, _Mapping]]] = ...) -> None: ...

class StickerPack(_message.Message):
    __slots__ = ("id", "type", "name", "stickers")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[StickerPack.Type]
        STICKER: _ClassVar[StickerPack.Type]
        EMOJI: _ClassVar[StickerPack.Type]
    UNKNOWN: StickerPack.Type
    STICKER: StickerPack.Type
    EMOJI: StickerPack.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STICKERS_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: StickerPack.Type
    name: str
    stickers: _containers.RepeatedCompositeFieldContainer[_media_pb2.File]
    def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[StickerPack.Type, str]] = ..., name: _Optional[str] = ..., stickers: _Optional[_Iterable[_Union[_media_pb2.File, _Mapping]]] = ...) -> None: ...

class GetStickerFiles(_message.Message):
    __slots__ = ("sticker_ids",)
    STICKER_IDS_FIELD_NUMBER: _ClassVar[int]
    sticker_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, sticker_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class GetStickerPack(_message.Message):
    __slots__ = ("pack",)
    PACK_FIELD_NUMBER: _ClassVar[int]
    pack: _refs_pb2.StickerPackRef
    def __init__(self, pack: _Optional[_Union[_refs_pb2.StickerPackRef, _Mapping]] = ...) -> None: ...

class AddStickerToPack(_message.Message):
    __slots__ = ("pack", "sticker")
    PACK_FIELD_NUMBER: _ClassVar[int]
    STICKER_FIELD_NUMBER: _ClassVar[int]
    pack: _refs_pb2.StickerPackRef
    sticker: _media_pb2.MediaRefUploadedFile
    def __init__(self, pack: _Optional[_Union[_refs_pb2.StickerPackRef, _Mapping]] = ..., sticker: _Optional[_Union[_media_pb2.MediaRefUploadedFile, _Mapping]] = ...) -> None: ...

class RemoveStickerFromPack(_message.Message):
    __slots__ = ("pack", "sticker_id")
    PACK_FIELD_NUMBER: _ClassVar[int]
    STICKER_ID_FIELD_NUMBER: _ClassVar[int]
    pack: _refs_pb2.StickerPackRef
    sticker_id: int
    def __init__(self, pack: _Optional[_Union[_refs_pb2.StickerPackRef, _Mapping]] = ..., sticker_id: _Optional[int] = ...) -> None: ...
