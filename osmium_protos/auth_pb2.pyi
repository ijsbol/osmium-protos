import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InviteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[InviteType]
    COMMUNITY: _ClassVar[InviteType]
    GROUP: _ClassVar[InviteType]
    USER: _ClassVar[InviteType]
UNKNOWN: InviteType
COMMUNITY: InviteType
GROUP: InviteType
USER: InviteType

class SignIn(_message.Message):
    __slots__ = ("email", "password", "totp")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TOTP_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    totp: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., totp: _Optional[str] = ...) -> None: ...

class SignUp(_message.Message):
    __slots__ = ("email", "password", "name")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    name: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Authorize(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class Authorization(_message.Message):
    __slots__ = ("token", "user", "session_id")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    token: str
    user: _types_pb2.User
    session_id: int
    def __init__(self, token: _Optional[str] = ..., user: _Optional[_Union[_types_pb2.User, _Mapping]] = ..., session_id: _Optional[int] = ...) -> None: ...

class GetSessions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Sessions(_message.Message):
    __slots__ = ("sessions", "current")
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    current: int
    def __init__(self, sessions: _Optional[_Iterable[_Union[Session, _Mapping]]] = ..., current: _Optional[int] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("id", "client_id", "device_type", "device_version", "app_name", "app_version", "last_active", "country", "region")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    id: int
    client_id: int
    device_type: str
    device_version: str
    app_name: str
    app_version: str
    last_active: int
    country: str
    region: str
    def __init__(self, id: _Optional[int] = ..., client_id: _Optional[int] = ..., device_type: _Optional[str] = ..., device_version: _Optional[str] = ..., app_name: _Optional[str] = ..., app_version: _Optional[str] = ..., last_active: _Optional[int] = ..., country: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class RevokeSessions(_message.Message):
    __slots__ = ("session_ids",)
    SESSION_IDS_FIELD_NUMBER: _ClassVar[int]
    session_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, session_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class ResetPassword(_message.Message):
    __slots__ = ("email", "confirm")
    class ResetPasswordConfirm(_message.Message):
        __slots__ = ("code", "new_password")
        CODE_FIELD_NUMBER: _ClassVar[int]
        NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        code: str
        new_password: str
        def __init__(self, code: _Optional[str] = ..., new_password: _Optional[str] = ...) -> None: ...
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    email: str
    confirm: ResetPassword.ResetPasswordConfirm
    def __init__(self, email: _Optional[str] = ..., confirm: _Optional[_Union[ResetPassword.ResetPasswordConfirm, _Mapping]] = ...) -> None: ...

class VerifyEmail(_message.Message):
    __slots__ = ("email", "code")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    email: str
    code: str
    def __init__(self, email: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class ResendEmailVerification(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class LookupInvite(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class CreatedInvite(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class InvitePreview(_message.Message):
    __slots__ = ("code", "creator_id", "target_id", "target_type", "expires_at", "creator", "community", "chat", "user")
    CODE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    code: str
    creator_id: int
    target_id: int
    target_type: InviteType
    expires_at: int
    creator: _types_pb2.User
    community: _types_pb2.Community
    chat: _types_pb2.Group
    user: _types_pb2.User
    def __init__(self, code: _Optional[str] = ..., creator_id: _Optional[int] = ..., target_id: _Optional[int] = ..., target_type: _Optional[_Union[InviteType, str]] = ..., expires_at: _Optional[int] = ..., creator: _Optional[_Union[_types_pb2.User, _Mapping]] = ..., community: _Optional[_Union[_types_pb2.Community, _Mapping]] = ..., chat: _Optional[_Union[_types_pb2.Group, _Mapping]] = ..., user: _Optional[_Union[_types_pb2.User, _Mapping]] = ...) -> None: ...

class UseInvite(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class InviteList(_message.Message):
    __slots__ = ("invites",)
    INVITES_FIELD_NUMBER: _ClassVar[int]
    invites: _containers.RepeatedCompositeFieldContainer[InvitePreview]
    def __init__(self, invites: _Optional[_Iterable[_Union[InvitePreview, _Mapping]]] = ...) -> None: ...
