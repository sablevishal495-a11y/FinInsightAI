class ChunkService:

    @staticmethod
    def create_chunks(pages, chunk_size=500):

        chunks = []

        for page in pages:

            text = page["text"]
            page_number = page["page"]

            start = 0

            while start < len(text):

                chunk = text[start:start + chunk_size]

                chunks.append({
                    "page": page_number,
                    "text": chunk
                })

                start += chunk_size

        return chunks