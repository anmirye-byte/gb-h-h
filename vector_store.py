from pathlib import Path
import os

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

from pdf_search import load_pdf_pages, split_documents


DB_FOLDER = Path("chroma_db")
COLLECTION_NAME = "gb_documents"


def build_vector_db():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("OPENAI_API_KEY를 찾을 수 없습니다.")
        print(".env 파일을 확인해 주세요.")
        return

    client_openai = OpenAI(api_key=api_key)

    print("1. PDF 자료를 읽고 있습니다...")

    documents = load_pdf_pages()
    chunks = split_documents(documents)

    print(f"\n생성된 청크 수: {len(chunks)}")

    if not chunks:
        print("저장할 청크가 없습니다.")
        return

    print("\n2. OpenAI 임베딩을 생성하고 있습니다...")

    texts = [chunk["text"] for chunk in chunks]

    response = client_openai.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )

    embeddings = [
        item.embedding
        for item in response.data
    ]

    print("\n3. ChromaDB에 저장하고 있습니다...")

    chroma_client = chromadb.PersistentClient(
        path=str(DB_FOLDER)
    )

    try:
        chroma_client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = chroma_client.create_collection(
        name=COLLECTION_NAME
    )

    ids = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(f"chunk_{i}")

        metadatas.append(
            {
                "file_name": chunk["file_name"],
                "page": chunk["page"],
            }
        )

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    print("\n==============================")
    print("벡터DB 생성 완료!")
    print(f"저장된 청크 수: {collection.count()}")
    print("==============================")


if __name__ == "__main__":
    build_vector_db()