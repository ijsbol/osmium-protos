"""Helpers for wrapping betterproto2 payloads into Osmium client frames."""

from __future__ import annotations

import betterproto2

from osmium_protos.osmium.client.core import ClientMessage

# Reverse of ClientMessage's oneof: payload class -> envelope field name. Each
# request type appears in exactly one slot, so the mapping is unambiguous.
_field_by_payload: dict[type, str] = {
    cls: name
    for name, cls in ClientMessage._betterproto.cls_by_field.items()
    if name != "id"
}


def wrap(payload: betterproto2.Message, *, id: int = 0) -> ClientMessage:
    """Wrap a request payload in a ``ClientMessage`` envelope.

    Picks the oneof slot on ``ClientMessage`` whose type matches ``payload`` and
    returns the populated envelope, e.g. ``wrap(SignIn(...))`` ->
    ``ClientMessage(auth_sign_in=SignIn(...))``.

    ``id`` is the client-assigned request id the server echoes back on the
    matching ``RpcResult``/``RpcError``.
    """
    field = _field_by_payload.get(type(payload))
    if field is None:
        raise TypeError(
            f"{type(payload).__name__} is not a valid ClientMessage payload"
        )
    return ClientMessage(id=id, **{field: payload})
