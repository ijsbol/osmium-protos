"""Helpers for decoding raw Osmium server frames into betterproto2 messages."""

from __future__ import annotations

import betterproto2

from osmium_protos.osmium.client.core import ServerMessage


def unwrap(data: bytes) -> tuple[str, betterproto2.Message]:
    """Parse a server frame and descend through oneof envelopes to the leaf payload.

    Returns the dotted oneof path and the innermost message, e.g.
    ``("result.error", RpcError(...))`` or ``("update.message_created", ...)``.
    """
    msg: betterproto2.Message = ServerMessage.parse(data)

    path: list[str] = []
    while True:
        # Descend into the first oneof group whose set member is itself a message.
        for group in getattr(msg._betterproto, "oneof_field_by_group", {}):
            field, value = betterproto2.which_one_of(msg, group)
            if isinstance(value, betterproto2.Message):
                path.append(field)
                msg = value
                break
        else:
            break

    return ".".join(path), msg
