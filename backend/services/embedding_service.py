from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        print("Embedding model loaded.")

    def create_embeddings(self, chunks):

        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings