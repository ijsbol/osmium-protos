import refs_pb2 as _refs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadFilePart(_message.Message):
    __slots__ = ("upload_id", "part", "data")
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PART_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    upload_id: int
    part: int
    data: bytes
    def __init__(self, upload_id: _Optional[int] = ..., part: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class DownloadFilePart(_message.Message):
    __slots__ = ("file_ref", "offset", "length")
    FILE_REF_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_ref: FileRef
    offset: int
    length: int
    def __init__(self, file_ref: _Optional[_Union[FileRef, _Mapping]] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class FilePart(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class FileRef(_message.Message):
    __slots__ = ("media_file", "chat_photo")
    class MediaFileRef(_message.Message):
        __slots__ = ("file_id",)
        FILE_ID_FIELD_NUMBER: _ClassVar[int]
        file_id: int
        def __init__(self, file_id: _Optional[int] = ...) -> None: ...
    class ChatPhotoFileRef(_message.Message):
        __slots__ = ("file_id",)
        FILE_ID_FIELD_NUMBER: _ClassVar[int]
        file_id: int
        def __init__(self, file_id: _Optional[int] = ...) -> None: ...
    MEDIA_FILE_FIELD_NUMBER: _ClassVar[int]
    CHAT_PHOTO_FIELD_NUMBER: _ClassVar[int]
    media_file: FileRef.MediaFileRef
    chat_photo: FileRef.ChatPhotoFileRef
    def __init__(self, media_file: _Optional[_Union[FileRef.MediaFileRef, _Mapping]] = ..., chat_photo: _Optional[_Union[FileRef.ChatPhotoFileRef, _Mapping]] = ...) -> None: ...

class UploadedFileRef(_message.Message):
    __slots__ = ("id", "name", "part_count")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PART_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    part_count: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., part_count: _Optional[int] = ...) -> None: ...

class MediaRef(_message.Message):
    __slots__ = ("uploaded", "embed")
    UPLOADED_FIELD_NUMBER: _ClassVar[int]
    EMBED_FIELD_NUMBER: _ClassVar[int]
    uploaded: MediaRefUploadedFile
    embed: MediaRefEmbed
    def __init__(self, uploaded: _Optional[_Union[MediaRefUploadedFile, _Mapping]] = ..., embed: _Optional[_Union[MediaRefEmbed, _Mapping]] = ...) -> None: ...

class MediaRefUploadedFile(_message.Message):
    __slots__ = ("file", "filename", "mimetype", "metadata")
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    file: UploadedFileRef
    filename: str
    mimetype: str
    metadata: FileMetadata
    def __init__(self, file: _Optional[_Union[UploadedFileRef, _Mapping]] = ..., filename: _Optional[str] = ..., mimetype: _Optional[str] = ..., metadata: _Optional[_Union[FileMetadata, _Mapping]] = ...) -> None: ...

class MediaRefEmbed(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class FileMetadata(_message.Message):
    __slots__ = ("image", "video", "audio", "file", "custom_emoji")
    class MetadataImage(_message.Message):
        __slots__ = ("width", "height", "preview")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        PREVIEW_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        preview: bytes
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., preview: _Optional[bytes] = ...) -> None: ...
    class MetadataVideo(_message.Message):
        __slots__ = ("width", "height", "duration")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        duration: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...
    class MetadataAudio(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: int
        def __init__(self, duration: _Optional[int] = ...) -> None: ...
    class MetadataFile(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MetadataCustomEmoji(_message.Message):
        __slots__ = ("width", "height", "emoji", "pack")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        EMOJI_FIELD_NUMBER: _ClassVar[int]
        PACK_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        emoji: str
        pack: _refs_pb2.StickerPackRef
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., emoji: _Optional[str] = ..., pack: _Optional[_Union[_refs_pb2.StickerPackRef, _Mapping]] = ...) -> None: ...
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EMOJI_FIELD_NUMBER: _ClassVar[int]
    image: FileMetadata.MetadataImage
    video: FileMetadata.MetadataVideo
    audio: FileMetadata.MetadataAudio
    file: FileMetadata.MetadataFile
    custom_emoji: FileMetadata.MetadataCustomEmoji
    def __init__(self, image: _Optional[_Union[FileMetadata.MetadataImage, _Mapping]] = ..., video: _Optional[_Union[FileMetadata.MetadataVideo, _Mapping]] = ..., audio: _Optional[_Union[FileMetadata.MetadataAudio, _Mapping]] = ..., file: _Optional[_Union[FileMetadata.MetadataFile, _Mapping]] = ..., custom_emoji: _Optional[_Union[FileMetadata.MetadataCustomEmoji, _Mapping]] = ...) -> None: ...

class File(_message.Message):
    __slots__ = ("file_id", "region", "size", "mimetype", "filename", "metadata")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    region: int
    size: int
    mimetype: str
    filename: str
    metadata: FileMetadata
    def __init__(self, file_id: _Optional[int] = ..., region: _Optional[int] = ..., size: _Optional[int] = ..., mimetype: _Optional[str] = ..., filename: _Optional[str] = ..., metadata: _Optional[_Union[FileMetadata, _Mapping]] = ...) -> None: ...

class Files(_message.Message):
    __slots__ = ("files",)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[File]
    def __init__(self, files: _Optional[_Iterable[_Union[File, _Mapping]]] = ...) -> None: ...

class MediaFile(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: File
    def __init__(self, file: _Optional[_Union[File, _Mapping]] = ...) -> None: ...

class MediaEmbed(_message.Message):
    __slots__ = ("url", "title", "description")
    URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    url: str
    title: str
    description: str
    def __init__(self, url: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class MessageMedia(_message.Message):
    __slots__ = ("file", "embed")
    FILE_FIELD_NUMBER: _ClassVar[int]
    EMBED_FIELD_NUMBER: _ClassVar[int]
    file: MediaFile
    embed: MediaEmbed
    def __init__(self, file: _Optional[_Union[MediaFile, _Mapping]] = ..., embed: _Optional[_Union[MediaEmbed, _Mapping]] = ...) -> None: ...
