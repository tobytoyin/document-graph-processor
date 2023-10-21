from typing import Set

from d2d.doc_processor.factory import DocumentAdapterContainer
from d2d.doc_processor.interfaces import DocumentAdapter
from d2d.doc_processor.types import DocID, MetadataKVPair, NormalisedContents

from .processors import frontmatter_processor, links_processor


@DocumentAdapterContainer.register(name="obsidian")
class ObsidianAdapter(DocumentAdapter):
    def __init__(self, path: str) -> None:
        self.text = self._read(path)
        self.path = path

    @staticmethod
    def _read(path):
        with open(path, "r") as f:
            return f.read()

    def id_processor(self) -> DocID:
        return self.path.split("/")[-1].split(".")[0]

    def metadata_processor(self) -> MetadataKVPair:
        return frontmatter_processor(self.text)

    def relations_processor(self):
        out = []
        links = links_processor(self.text)
        for link in links:
            doc_id = link.pop("rel_uid")
            rel_type = link.pop("rel_type")
            new_obj = {"rel_uid": doc_id, "rel_type": rel_type, "properties": link}
            out.append(new_obj)

        return out

    def contents_normaliser(self) -> NormalisedContents:
        return self.text