from __future__ import annotations

import typing as t

import typing_extensions as te

__all__ = (
    "Message",
    "InstanceInfo", 
    "RateLimitConf", 
    "EffisRateLimitConf",
    "OprishRateLimits",
    "EffisRateLimits",
    "InstanceRateLimits",
    "RateLimitedErrorData",
    "RateLimitedError",
    "FileSizeRateLimitedErrorData",
    "FileSizeRateLimitedError",
    "ValidationErrorData",
    "ValidationError",
    "NotFoundError",
    "ServerErrorData",
    "ServerError",
)


## Messages ##


@t.final
class Message(te.TypedDict):
    author: str
    content: str


## Instance Information ##

@t.final
class InstanceInfo(te.TypedDict):
    instance_name: str
    description: t.Optional[str]
    version: str
    message_limit: int
    oprish_url: str
    pandemonium_url: str
    effis_url: str
    file_size: int
    attachment_file_size: int


## Rate Limits ##


class BaseRateLimitConf(te.TypedDict):
    reset_after: int
    limit: int


@t.final
class RateLimitConf(BaseRateLimitConf):
    pass


@t.final
class EffisRateLimitConf(BaseRateLimitConf):
    file_size_limit: int


@t.final
class OprishRateLimits(te.TypedDict):
    info: RateLimitConf
    messsage_create: RateLimitConf
    rate_limits: RateLimitConf


@t.final
class EffisRateLimits(te.TypedDict):
    assets: EffisRateLimitConf
    attachments: EffisRateLimitConf


@t.final
class InstanceRateLimits(te.TypedDict):
    oprish: OprishRateLimits
    pandemonium: RateLimitConf
    effis: EffisRateLimits


## Errors ##

MappingT = t.TypeVar("MappingT", bound=t.Mapping[str, t.Any])


# TODO: make another class where the data is required
class GenericOprishError(te.TypedDict, t.Generic[MappingT]):
    status: int
    message: str
    data: te.NotRequired[MappingT]


@t.final
class RateLimitedErrorData(te.TypedDict):
    retry_after: int


RateLimitedError: t.Final = GenericOprishError[RateLimitedErrorData]

@t.final
class FileSizeRateLimitedErrorData(te.TypedDict):
    retry_after: int
    bytes_left: int

FileSizeRateLimitedError: t.Final = GenericOprishError[FileSizeRateLimitedErrorData]

@t.final
class ValidationErrorData(te.TypedDict):
    field_name: str
    error: str

ValidationError: t.Final = GenericOprishError[ValidationErrorData]

@t.final
class NotFoundErrorData(te.TypedDict):
    pass

NotFoundError: t.Final = GenericOprishError[NotFoundErrorData]

@t.final
class ServerErrorData(te.TypedDict):
    error: str

ServerError: t.Final = GenericOprishError[ServerErrorData]