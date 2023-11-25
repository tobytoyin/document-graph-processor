import logging

from d2d.contracts.payload import Source, SourceSpec
from d2d.tasks.document_composer._source_handler import (
    _get_source_text,
    _get_source_uid,
)

from ..payload_fixtures import *


### Assuming upstream validates SourceHanlder
### Proceed to get the text from source
### Note - options are not tested herein, they are tested in common functionality
def test_get_source_text():
    handler_payload = SourceSpec(provider="mock")
    source = Source(path="dummy.txt")  # type: ignore
    reader = _get_source_text(source, handler_payload)
    assert reader == "mock io contents"


def test_source_uid():
    handler_payload = SourceSpec(provider="mock")
    source = Source(path="dummy.txt")  # type: ignore
    reader = _get_source_uid(source, handler_payload)
    assert reader == "dummy"