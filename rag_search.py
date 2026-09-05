import os

import chromadb
from dotenv import load_dotenv
from openai import OpenAI


DB_FOLDER = "chroma_db"
COLLECTION_NAME = "gb_documents"


def search_and_answer(question, n_results=3):
    # 1. API 키 불러오기
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "OPENAI_API_KEY를 찾을 수 없습니다.", []

    openai_client = OpenAI(api_key=api_key)

    # 2. 질문을 임베딩으로 변환
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=[question],
    )

    question_embedding = response.data[0].embedding

    # 3. ChromaDB 연결
    chroma_client = chromadb.PersistentClient(
        path=DB_FOLDER
    )

    collection = chroma_client.get_collection(
        name=COLLECTION_NAME
    )

    # 4. 관련 자료 검색
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results,
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    # 5. AI에게 전달할 근거자료 만들기
    context_parts = []

    for document, metadata in zip(documents, metadatas):
        context_parts.append(
            f"""
[자료]
파일명: {metadata['file_name']}
페이지: {metadata['page']}
내용:
{document}
"""
        )

    context = "\n".join(context_parts)

    # 6. AI 답변 생성
    prompt = f"""
당신은 개발제한구역 업무를 지원하는 AI 도우미입니다.

아래 제공된 근거자료만 사용하여 질문에 답변하세요.

원칙:
1. 근거자료에 없는 내용은 임의로 만들지 마세요.
2. 확실하지 않으면 "제공된 자료만으로는 확인하기 어렵습니다."라고 답하세요.
3. 답변은 공무원이 업무에 참고하기 쉽도록 간결하고 명확하게 작성하세요.
4. 관련 조건이나 예외가 있다면 함께 설명하세요.
5. 최종 법적 판단을 위해 최신 법령과 해당 지역 관리계획을 확인하도록 안내하세요.

[사용자 질문]
{question}

[근거자료]
{context}
"""

    answer_response = openai_client.responses.create(
        model="gpt-5-mini",
        input=prompt,
    )

    answer = answer_response.output_text

    # 7. 웹에 표시할 근거자료 만들기
    # 같은 파일 + 같은 페이지는 중복 제거
    sources = []
    seen_sources = set()

    for document, metadata in zip(documents, metadatas):
        source_key = (
            metadata["file_name"],
            metadata["page"],
        )

        if source_key in seen_sources:
            continue

        seen_sources.add(source_key)

        sources.append(
            {
                "file_name": metadata["file_name"],
                "page": metadata["page"],
                "text": document,
            }
        )

    return answer, sources


if __name__ == "__main__":
    question = input("질문을 입력하세요: ")

    answer, sources = search_and_answer(question)

    print("\nAI 답변")
    print(answer)

    print("\n근거자료")

    for i, source in enumerate(sources, start=1):
        print(f"\n[근거 {i}]")
        print("파일:", source["file_name"])
        print("페이지:", source["page"])
        print("내용:")
        print(source["text"])