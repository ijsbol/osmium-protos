from google.protobuf.message import Message

from osmium_protos.core_pb2 import ServerMessage


def unwrap(data: bytes) -> tuple[str, Message]:
    """Parse a server frame and descend through oneof envelopes to the leaf payload."""
    msg: Message = ServerMessage()
    msg.ParseFromString(data)

    path: list[str] = []
    while True:
        # find a oneof that wraps a sub-message
        oneof = next(
            (o.name for o in msg.DESCRIPTOR.oneofs
             if msg.WhichOneof(o.name) is not None),
            None,
        )
        if oneof is None:
            break
        field = msg.WhichOneof(oneof)
        child = getattr(msg, field)
        if not isinstance(child, Message):
            break
        path.append(field)
        msg = child

    return ".".join(path), msg   # e.g. ("update.message_created", UpdateMessageCreated(...))
