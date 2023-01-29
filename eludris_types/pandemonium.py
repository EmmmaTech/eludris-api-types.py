from __future__ import annotations

import typing as t

import typing_extensions as te

if t.TYPE_CHECKING:
    from .oprish import Message

__all__ = ("PingEvent", "PongEvent", "MessageCreateEvent",)

@t.final
class PingEvent(te.TypedDict):
    op: t.Literal["PING"]

@t.final
class PongEvent(te.TypedDict):
    op: t.Literal["PONG"]

@t.final
class MessageCreateEvent(te.TypedDict):
    op: t.Literal["MESSAGE_CREATE"]
    d: Message
