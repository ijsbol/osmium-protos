from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestPaymentLink(_message.Message):
    __slots__ = ("redirect_url", "plan", "billing_period")
    REDIRECT_URL_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    BILLING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    redirect_url: str
    plan: str
    billing_period: str
    def __init__(self, redirect_url: _Optional[str] = ..., plan: _Optional[str] = ..., billing_period: _Optional[str] = ...) -> None: ...

class PaymentLink(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class CancelSubscription(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSubscription(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Subscription(_message.Message):
    __slots__ = ("active", "since", "next_renewal_date", "last_card_digits", "method", "end_date")
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    NEXT_RENEWAL_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_CARD_DIGITS_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    since: int
    next_renewal_date: int
    last_card_digits: str
    method: str
    end_date: int
    def __init__(self, active: _Optional[bool] = ..., since: _Optional[int] = ..., next_renewal_date: _Optional[int] = ..., last_card_digits: _Optional[str] = ..., method: _Optional[str] = ..., end_date: _Optional[int] = ...) -> None: ...
