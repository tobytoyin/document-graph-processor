from typing import Protocol

from doc_uploader.contracts.document import Document


class DocumentAdapter(Protocol):
    def create_document(self) -> Document:
        ...


class SourceHandlersCatalog(Protocol):
    SOURCE_READER = None
    LINK_PROCESSOR = None
    META_PROCESSOR = None
