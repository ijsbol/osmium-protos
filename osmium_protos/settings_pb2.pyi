import media_pb2 as _media_pb2
import refs_pb2 as _refs_pb2
import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EditProfilePhoto(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _media_pb2.UploadedFileRef
    def __init__(self, file: _Optional[_Union[_media_pb2.UploadedFileRef, _Mapping]] = ...) -> None: ...

class RegisterPushSubscription(_message.Message):
    __slots__ = ("web", "push")
    class PushType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[RegisterPushSubscription.PushType]
        WEB: _ClassVar[RegisterPushSubscription.PushType]
        IOS: _ClassVar[RegisterPushSubscription.PushType]
        ANDROID_FCM: _ClassVar[RegisterPushSubscription.PushType]
    UNKNOWN: RegisterPushSubscription.PushType
    WEB: RegisterPushSubscription.PushType
    IOS: RegisterPushSubscription.PushType
    ANDROID_FCM: RegisterPushSubscription.PushType
    class PushEncryptionScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PUSH_ENCRYPTION_UNKNOWN: _ClassVar[RegisterPushSubscription.PushEncryptionScheme]
        P256_HKDF_SHA256_AES256GCM_V1: _ClassVar[RegisterPushSubscription.PushEncryptionScheme]
    PUSH_ENCRYPTION_UNKNOWN: RegisterPushSubscription.PushEncryptionScheme
    P256_HKDF_SHA256_AES256GCM_V1: RegisterPushSubscription.PushEncryptionScheme
    class WebPush(_message.Message):
        __slots__ = ("endpoint", "p256dh", "auth")
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        P256DH_FIELD_NUMBER: _ClassVar[int]
        AUTH_FIELD_NUMBER: _ClassVar[int]
        endpoint: str
        p256dh: str
        auth: str
        def __init__(self, endpoint: _Optional[str] = ..., p256dh: _Optional[str] = ..., auth: _Optional[str] = ...) -> None: ...
    class Push(_message.Message):
        __slots__ = ("type", "token", "encryption_public_key", "encryption_auth_secret", "encryption_key_id", "encryption_scheme")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_AUTH_SECRET_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_SCHEME_FIELD_NUMBER: _ClassVar[int]
        type: RegisterPushSubscription.PushType
        token: str
        encryption_public_key: str
        encryption_auth_secret: str
        encryption_key_id: str
        encryption_scheme: RegisterPushSubscription.PushEncryptionScheme
        def __init__(self, type: _Optional[_Union[RegisterPushSubscription.PushType, str]] = ..., token: _Optional[str] = ..., encryption_public_key: _Optional[str] = ..., encryption_auth_secret: _Optional[str] = ..., encryption_key_id: _Optional[str] = ..., encryption_scheme: _Optional[_Union[RegisterPushSubscription.PushEncryptionScheme, str]] = ...) -> None: ...
    WEB_FIELD_NUMBER: _ClassVar[int]
    PUSH_FIELD_NUMBER: _ClassVar[int]
    web: RegisterPushSubscription.WebPush
    push: RegisterPushSubscription.Push
    def __init__(self, web: _Optional[_Union[RegisterPushSubscription.WebPush, _Mapping]] = ..., push: _Optional[_Union[RegisterPushSubscription.Push, _Mapping]] = ...) -> None: ...

class UnregisterPushSubscription(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChangeNotificationPreferences(_message.Message):
    __slots__ = ("prefs", "chat_ref", "community_id")
    PREFS_FIELD_NUMBER: _ClassVar[int]
    CHAT_REF_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    prefs: _types_pb2.NotifPrefs
    chat_ref: _refs_pb2.ChatRef
    community_id: int
    def __init__(self, prefs: _Optional[_Union[_types_pb2.NotifPrefs, str]] = ..., chat_ref: _Optional[_Union[_refs_pb2.ChatRef, _Mapping]] = ..., community_id: _Optional[int] = ...) -> None: ...

class EditUserSettings(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: UserSettings
    def __init__(self, settings: _Optional[_Union[UserSettings, _Mapping]] = ...) -> None: ...

class UserSettings(_message.Message):
    __slots__ = ("community_order",)
    class CommunityOrder(_message.Message):
        __slots__ = ("community_ids",)
        COMMUNITY_IDS_FIELD_NUMBER: _ClassVar[int]
        community_ids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, community_ids: _Optional[_Iterable[int]] = ...) -> None: ...
    COMMUNITY_ORDER_FIELD_NUMBER: _ClassVar[int]
    community_order: UserSettings.CommunityOrder
    def __init__(self, community_order: _Optional[_Union[UserSettings.CommunityOrder, _Mapping]] = ...) -> None: ...

class EditProfile(_message.Message):
    __slots__ = ("name", "username", "bio", "icon", "color")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    BIO_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    username: str
    bio: str
    icon: int
    color: int
    def __init__(self, name: _Optional[str] = ..., username: _Optional[str] = ..., bio: _Optional[str] = ..., icon: _Optional[int] = ..., color: _Optional[int] = ...) -> None: ...

class GetAccount(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Account(_message.Message):
    __slots__ = ("email", "confirmed", "has_password", "totp_enabled", "pending_delete")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    HAS_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TOTP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PENDING_DELETE_FIELD_NUMBER: _ClassVar[int]
    email: str
    confirmed: bool
    has_password: bool
    totp_enabled: bool
    pending_delete: bool
    def __init__(self, email: _Optional[str] = ..., confirmed: _Optional[bool] = ..., has_password: _Optional[bool] = ..., totp_enabled: _Optional[bool] = ..., pending_delete: _Optional[bool] = ...) -> None: ...

class ChangePassword(_message.Message):
    __slots__ = ("current_password", "new_password", "revoke_sessions")
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    REVOKE_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    current_password: str
    new_password: str
    revoke_sessions: bool
    def __init__(self, current_password: _Optional[str] = ..., new_password: _Optional[str] = ..., revoke_sessions: _Optional[bool] = ...) -> None: ...

class ChangeEmail(_message.Message):
    __slots__ = ("new_email",)
    NEW_EMAIL_FIELD_NUMBER: _ClassVar[int]
    new_email: str
    def __init__(self, new_email: _Optional[str] = ...) -> None: ...

class ChangeStatus(_message.Message):
    __slots__ = ("status", "activities")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    status: _types_pb2.UserStatus.Status
    activities: _containers.RepeatedCompositeFieldContainer[_types_pb2.UserStatus.Activity]
    def __init__(self, status: _Optional[_Union[_types_pb2.UserStatus.Status, str]] = ..., activities: _Optional[_Iterable[_Union[_types_pb2.UserStatus.Activity, _Mapping]]] = ...) -> None: ...

class SetupTotp(_message.Message):
    __slots__ = ("enabled", "code")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    code: str
    def __init__(self, enabled: _Optional[bool] = ..., code: _Optional[str] = ...) -> None: ...

class Totp(_message.Message):
    __slots__ = ("enabled", "url", "backup_codes")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CODES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    url: str
    backup_codes: _containers.RepeatedCompositeFieldContainer[BackupCode]
    def __init__(self, enabled: _Optional[bool] = ..., url: _Optional[str] = ..., backup_codes: _Optional[_Iterable[_Union[BackupCode, _Mapping]]] = ...) -> None: ...

class BackupCode(_message.Message):
    __slots__ = ("code", "used")
    CODE_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    code: str
    used: bool
    def __init__(self, code: _Optional[str] = ..., used: _Optional[bool] = ...) -> None: ...

class RequestTakeout(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAccount(_message.Message):
    __slots__ = ("cancel",)
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    cancel: bool
    def __init__(self, cancel: _Optional[bool] = ...) -> None: ...
