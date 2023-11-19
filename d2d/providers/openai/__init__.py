from openai import OpenAI


# follows the services.SourceTasks interface
class TaskCatalog:
    provider_name = "openai"
    client = OpenAI()

    @staticmethod
    def embedding(text: str, api_key: str):
        callback = TaskCatalog.client.embeddings
        callback.api_key = api_key
        res = callback.create(
            model="text-embedding-ada-002",
            input=text,
            encoding_format="float",
        )

        return {"embedding": res.data[0].embedding}