from __future__ import annotations

import logging
from collections import namedtuple
from functools import cache
from typing import Generator

from pydantic import ValidationError

from d2d.contracts.payload import Source, SourceDict, SourceHandler, SourcePayload
from d2d.providers.factory import get_source_handling_provider
from d2d.tasks.common import transform_function_with_options

SourceMetaItems = namedtuple("SourceMetaItems", "source_text source_uid")


def payload_handler(payload: dict) -> SourcePayload:
    """First contact point for the payload to get pass to the pipeline


    :param payload: _description_
    :type payload: dict
    :return: _description_
    :rtype: SourcePayload
    """
    return SourcePayload.model_validate(payload)


@cache
def _get_source_text(source: Source, handler_payload: SourceHandler) -> str:
    # converting between Source to dict to allow cache,
    # this allow function to only interact with external source once to get the content

    # NOTE - maybe using a singleton class to cache the text with a map instead?

    provider_name = handler_payload.provider
    provider = get_source_handling_provider(provider_name=provider_name)

    fn = transform_function_with_options(provider.source_text, handler_payload.options)
    return fn(source.model_dump())


@cache
def _get_source_uid(source: Source, handler_payload: SourceHandler) -> str:
    provider_name = handler_payload.provider
    provider = get_source_handling_provider(provider_name=provider_name)

    fn = transform_function_with_options(provider.uid_gen, handler_payload.options)
    return fn(source.model_dump())


def get_source_contents(source: Source, spec: SourceHandler) -> SourceMetaItems:
    # just returning source_text and source_uid from a single function
    source_text = _get_source_text(source=source, handler_payload=spec)
    source_uid = _get_source_uid(source=source, handler_payload=spec)
    return SourceMetaItems(source_text, source_uid)
