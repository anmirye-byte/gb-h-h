from pathlib import Path
from pypdf import PdfReader

DATA_FOLDER = Path("data")


def load_pdf_pages():
    documents = []

    pdf_files = list(DATA_FOLDER.glob("*.pdf"))

    print(f"PDF 파일 수: {len(pdf_files)}개")

    for pdf_file in pdf_files:
        print(f"\n읽는 중: {pdf_file.name}")

        try:
            reader = PdfReader(pdf_file)

            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text()

                if text:
                    documents.append(
                        {
                            "file_name": pdf_file.name,
                            "page": page_number,
                            "text": text.strip(),
                        }
                    )

            print(f"  → {len(reader.pages)}페이지 확인 완료")

        except Exception as e:
            print(f"  → 오류: {e}")

    return documents


def split_documents(documents, chunk_size=800, overlap=150):
    chunks = []

    for doc in documents:
        text = doc["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append(
                {
                    "file_name": doc["file_name"],
                    "page": doc["page"],
                    "text": chunk_text,
                }
            )

            start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    documents = load_pdf_pages()

    chunks = split_documents(documents)

    print("\n============================")
    print(f"전체 페이지 수: {len(documents)}")
    print(f"생성된 청크 수: {len(chunks)}")
    print("============================")

    if chunks:
        print("\n첫 번째 청크 확인")
        print("파일명:", chunks[0]["file_name"])
        print("페이지:", chunks[0]["page"])
        print("\n내용:")
        print(chunks[0]["text"])