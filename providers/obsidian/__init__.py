# follows the services.SourceIO interface
from .processor import frontmatter_processor, links_processor


class SourceCatalog:
    @staticmethod
    def source_text(d: dict):
        with open(d["path"], "r") as f:
            return f.read()

    @staticmethod
    def metadata(d):
        return {
            "uid": str(d["path"]).split("/")[-1].split(".")[0],
        }


# follows the services.SourceTasks interface
class TaskCatalog:
    @staticmethod
    def metadata(text):
        return frontmatter_processor(text)

    @staticmethod
    def relations(text):
        return {"items": links_processor(text)}
