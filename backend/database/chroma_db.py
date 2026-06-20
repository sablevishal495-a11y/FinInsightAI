import chromadb

class ChromaDBService:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="financial_documents"
        )

    def reset_collection(self):
        try:
            self.client.delete_collection("financial_documents")
        except:
            pass

        self.collection = self.client.create_collection(
            name="financial_documents"
        )

    def store_embeddings(self, chunks, embeddings):

        ids = []
        documents = []
        metadatas = []
        vectors = []

        for index, chunk in enumerate(chunks):

            ids.append(f"chunk_{index}")

            documents.append(chunk["text"])

            metadatas.append({"page": chunk["page"]})

            vectors.append(embeddings[index].tolist())

        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=vectors
        )

    def search(self, question_embedding, top_k=5):

        return self.collection.query(
            query_embeddings=[question_embedding.tolist()],
            n_results=top_k
        )