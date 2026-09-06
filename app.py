import streamlit as st
from rag_search import search_and_answer


# --------------------------------------------------
# 기본 설정
# --------------------------------------------------
st.set_page_config(
    page_title="개발제한구역 불법행위 업무지원 시스템",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# CSS 디자인
# --------------------------------------------------
st.markdown(
    """
    <style>

    /* 전체 본문 폭과 여백 */
    .block-container {
        max-width: 1150px;
        padding-top: 1.4rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* ----------------------------------
       왼쪽 사이드바
       ---------------------------------- */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #14532d 0%,
            #166534 100%
        );

        min-width: 235px !important;
        max-width: 235px !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        width: 235px !important;
    }

    /* 사이드바 전체 글씨 */
    [data-testid="stSidebar"] * {
        color: white;
    }

    /* GB 업무지원 제목 */
    [data-testid="stSidebar"] h2 {
        font-size: 1.45rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.4rem;
    }

    /* 설명 글씨 */
    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        font-size: 0.95rem !important;
        line-height: 1.5;
    }

    /* 왼쪽 메뉴 글자 */
    [data-testid="stSidebar"] label {
        font-size: 1.05rem !important;
        font-weight: 650 !important;
    }

    /* 라디오 메뉴 줄 간격 */
    [data-testid="stSidebar"] [role="radiogroup"] > label {
        padding-top: 4px !important;
        padding-bottom: 4px !important;
    }

    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.30);
        margin-top: 1.2rem;
        margin-bottom: 1.2rem;
    }

    /* ----------------------------------
       메인 제목
       ---------------------------------- */

    .main-title {
        font-size: 2.05rem;
        font-weight: 800;
        color: #173b2b;
        line-height: 1.2;
        margin-bottom: 0.25rem;
        white-space: nowrap;
    }

    .main-subtitle {
        font-size: 0.98rem;
        color: #667085;
        margin-bottom: 1rem;
    }

    /* 검색 영역 */
    .search-title {
        font-size: 1.05rem;
        font-weight: 750;
        color: #244b38;
        margin-bottom: 0.3rem;
    }

    /* 검색창 높이 */
    .stTextInput input {
        min-height: 42px;
        font-size: 1rem;
    }

    /* ----------------------------------
       주요 업무 카드
       ---------------------------------- */

    .work-card {
        border: 1px solid #dce5df;
        border-radius: 12px;
        padding: 14px;
        min-height: 105px;
        background-color: white;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }

    .work-card-title {
        font-size: 1.02rem;
        font-weight: 750;
        color: #14532d;
        margin-bottom: 7px;
    }

    .work-card-text {
        font-size: 0.88rem;
        color: #505a54;
        line-height: 1.45;
    }

    /* 섹션 제목 */
    .section-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #20352a;
        margin-top: 0.8rem;
        margin-bottom: 0.6rem;
    }

    /* 공지 / 즐겨찾기 */
    .notice-box {
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 15px 18px;
        background-color: #ffffff;
        min-height: 135px;
    }

    .notice-box h3 {
        margin-top: 0;
        margin-bottom: 12px;
        font-size: 1.25rem;
    }

    .notice-box p {
        margin-top: 6px;
        margin-bottom: 6px;
        font-size: 0.9rem;
    }

    /* AI 답변 */
    .ai-answer {
        border-left: 5px solid #15803d;
        background-color: #f0fdf4;
        padding: 16px 18px;
        border-radius: 9px;
        line-height: 1.65;
        font-size: 0.98rem;
        color: #18392a;
    }

    /* 버튼 */
    .stButton > button,
    [data-testid="stFormSubmitButton"] > button {
        border-radius: 8px;
        font-weight: 700;
        min-height: 40px;
        padding-left: 20px;
        padding-right: 20px;
    }

    /* dividers 간격 축소 */
    hr {
        margin-top: 1rem !important;
        margin-bottom: 1rem !important;
    }

    /* ----------------------------------
       휴대폰
       ---------------------------------- */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 0.8rem;
            padding-right: 0.8rem;
        }

        .main-title {
            font-size: 1.45rem;
            white-space: normal;
        }

        .main-subtitle {
            font-size: 0.88rem;
        }

        .work-card {
            min-height: auto;
        }
    }

    /* =========================================
   사이드바 메뉴를 실제 버튼처럼 표시
   ========================================= */

/* 메뉴 전체 간격 */
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 8px !important;
}

/* 각 메뉴 버튼 */
[data-testid="stSidebar"] [role="radiogroup"] > label {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    border-radius: 9px !important;

    padding: 10px 12px !important;
    margin-bottom: 2px !important;

    min-height: 44px !important;

    cursor: pointer !important;

    transition: all 0.15s ease !important;
}

/* 메뉴 글자 */
[data-testid="stSidebar"] [role="radiogroup"] > label p {
    font-size: 1.05rem !important;
    font-weight: 650 !important;
    color: white !important;
}

/* 기존 동그란 라디오 버튼 숨기기 */
[data-testid="stSidebar"] [role="radiogroup"] > label > div:first-child {
    display: none !important;
}

/* 마우스를 올렸을 때 */
[data-testid="stSidebar"] [role="radiogroup"] > label:hover {
    background: rgba(255, 255, 255, 0.13) !important;
    border-color: rgba(255, 255, 255, 0.55) !important;
    transform: translateX(2px);
}

/* 선택된 메뉴 */
[data-testid="stSidebar"] [role="radiogroup"] > label:has(
    input:checked
) {
    background: #2f9e50 !important;
    border-color: #69c77f !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15) !important;
}

/* 선택 메뉴 글자 강조 */
[data-testid="stSidebar"] [role="radiogroup"] > label:has(
    input:checked
) p {
    color: white !important;
    font-weight: 800 !important;
}

/* GB 업무지원 제목 아래 여백 */
[data-testid="stSidebar"] h2 {
    margin-bottom: 10px !important;
}

/* 설명과 구분선 사이 간격 */
[data-testid="stSidebar"] hr {
    margin-top: 22px !important;
    margin-bottom: 20px !important;
}
/* 화면 위쪽 제목 잘림 방지 */
.block-container {
    padding-top: 3rem !important;
    padding-bottom: 2rem !important;
}

/* 세로 스크롤 허용 */
html, body, [data-testid="stAppViewContainer"] {
    overflow-y: auto !important;
}

/* ===== 최종 산뜻한 디자인 보정 ===== */

/* 전체 화면 */
.stApp {
    background: #f7faf8;
}

/* 본문 영역 */
.block-container {
    max-width: 1180px;
}

/* 왼쪽 사이드바 - 밝고 산뜻한 녹색 */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #79B995 0%,
        #68AA85 100%
    ) !important;
}

/* 사이드바 버튼 */
[data-testid="stSidebar"] button {
    border-radius: 10px !important;
    transition: all 0.2s ease !important;
}

/* 사이드바 버튼에 마우스를 올렸을 때 */
[data-testid="stSidebar"] button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.10);
}

/* 일반 버튼 */
.stButton > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}

/* 입력창 */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {
    border-radius: 10px !important;
}

/* selectbox */
[data-baseweb="select"] > div {
    border-radius: 10px !important;
}

/* 알림/안내 박스 */
[data-testid="stAlert"] {
    border-radius: 12px !important;
}

/* 제목 */
h1, h2, h3 {
    color: #173f32;
    letter-spacing: -0.4px;
}
/* 사이드바 메뉴 버튼 - 더 진하게 */
[data-testid="stSidebar"] button {
    background: rgba(34, 120, 76, 0.78) !important;
    border: 1px solid rgba(255, 255, 255, 0.30) !important;
    color: white !important;
    border-radius: 10px !important;
    min-height: 42px !important;
}

/* 마우스 올렸을 때 조금 더 강조 */
[data-testid="stSidebar"] button:hover {
    background: rgba(24, 99, 62, 0.95) !important;
}

/* 사이드바 버튼 글자 줄바꿈 방지 */
[data-testid="stSidebar"] button p {
    white-space: nowrap !important;
    font-size: 15px !important;
}

/* 사이드바 폭을 조금 넓혀 긴 메뉴도 한 줄 표시 */
[data-testid="stSidebar"] {
    min-width: 205px !important;
    max-width: 205px !important;
}

/* ===== 사이드바 최종 폭/글자 보정 ===== */

[data-testid="stSidebar"] {
    min-width: 235px !important;
    width: 235px !important;
    max-width: 235px !important;
}

/* 메뉴 버튼 폭 */
[data-testid="stSidebar"] button {
    width: 100% !important;
    min-width: 195px !important;
    padding-left: 12px !important;
    padding-right: 12px !important;
}

/* 메뉴 글자 - 선명하고 한 줄 */
[data-testid="stSidebar"] button p {
    white-space: nowrap !important;
    word-break: keep-all !important;
    overflow-wrap: normal !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    letter-spacing: -0.3px !important;
    line-height: 1.2 !important;
}

/* ===== 최종 반응형 화면 보정 ===== */

/* 본문을 화면 크기에 맞게 넓게 사용 */
.block-container {
    width: 92% !important;
    max-width: 1450px !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* 전체 기본 글자 크기 */
.stApp {
    font-size: clamp(15px, 0.85vw, 18px) !important;
}

/* 제목도 큰 화면에서 자연스럽게 확대 */
h1 {
    font-size: clamp(28px, 2vw, 38px) !important;
}

h2 {
    font-size: clamp(22px, 1.5vw, 30px) !important;
}

h3 {
    font-size: clamp(18px, 1.15vw, 24px) !important;
}

/* 사이드바 폭 */
[data-testid="stSidebar"] {
    min-width: 250px !important;
    width: 250px !important;
    max-width: 250px !important;
}

/* 사이드바 메뉴 버튼 */
[data-testid="stSidebar"] button {
    width: 215px !important;
    min-width: 215px !important;
    max-width: 215px !important;

    min-height: 44px !important;

    background: rgba(38, 125, 79, 0.82) !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    border-radius: 10px !important;

    padding: 8px 10px !important;
}

/* 사이드바 메뉴 글자 */
[data-testid="stSidebar"] button p {
    white-space: nowrap !important;
    word-break: keep-all !important;
    overflow-wrap: normal !important;

    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: -0.4px !important;
    line-height: 1 !important;

    margin: 0 !important;
}

/* 버튼 내부 요소도 줄바꿈 금지 */
[data-testid="stSidebar"] button div {
    white-space: nowrap !important;
    flex-wrap: nowrap !important;
}

/* 일반 버튼 글자 */
.stButton > button {
    font-size: clamp(14px, 0.8vw, 17px) !important;
}

/* 입력창 글자 */
input {
    font-size: clamp(14px, 0.8vw, 17px) !important;
}

/* 사이드바 기본 메뉴 버튼 - 배경과 선택색의 중간 녹색 */
[data-testid="stSidebar"] button {
    background: #4F9F73 !important;
    border: 1px solid rgba(255, 255, 255, 0.45) !important;
    color: #ffffff !important;

    border-radius: 10px !important;
    min-height: 44px !important;

    box-shadow: 0 2px 5px rgba(25, 90, 55, 0.12) !important;
}

/* 메뉴 글자 */
[data-testid="stSidebar"] button p {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* 마우스를 올렸을 때 */
[data-testid="stSidebar"] button:hover {
    background: #39885E !important;
    border-color: rgba(255, 255, 255, 0.65) !important;
    box-shadow: 0 4px 9px rgba(25, 90, 55, 0.20) !important;
}

/* ===== 사이드바 radio 메뉴 최종 디자인 ===== */

/* 메뉴 한 줄 전체 */
[data-testid="stSidebar"] [role="radiogroup"] label {
    background: #4F9F73 !important;
    border: 1px solid rgba(255,255,255,0.38) !important;
    border-radius: 10px !important;

    padding: 10px 12px !important;
    margin-bottom: 8px !important;

    min-height: 44px !important;
    width: 100% !important;

    box-shadow: 0 2px 5px rgba(25, 90, 55, 0.12) !important;
}

/* 메뉴 글자 */
[data-testid="stSidebar"] [role="radiogroup"] label p {
    color: white !important;
    font-size: 15px !important;
    font-weight: 700 !important;

    white-space: nowrap !important;
    word-break: keep-all !important;
    overflow-wrap: normal !important;

    margin: 0 !important;
}

/* 선택된 메뉴 */
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
    background: #239653 !important;
    border-color: rgba(255,255,255,0.65) !important;
    box-shadow: 0 4px 10px rgba(22, 90, 52, 0.22) !important;
}

/* 마우스 올렸을 때 */
[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: #3D8D64 !important;
}

/* radio 원 자체는 그대로 유지 */
[data-testid="stSidebar"] [role="radiogroup"] input[type="radio"] {
    flex-shrink: 0 !important;
}

    </style>

    


    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# 사이드바
# --------------------------------------------------
with st.sidebar:

    st.markdown("### 🌿 GB 업무지원")
    st.markdown(
    "<div style='font-size:15px; font-weight:600; color:white;'>개발제한구역 불법행위 업무지원</div>",
    unsafe_allow_html=True,
)

    st.divider()

    menu = st.radio(
        "메뉴",
        [
            "🏠 홈",
            "📗 업무가이드",
            "🔍 법령·사례 검색",
            "📋 행정처분 절차",
            "🧮 이행강제금 계산",
            "📁 자료실",
            "⭐ 즐겨찾기",
            "📢 공지사항",
            "⚙️ 설정",
        ],
        label_visibility="collapsed",
    )


# --------------------------------------------------
# 공통 RAG 결과 출력 함수
# --------------------------------------------------
def show_rag_result(question):

    if not question:
        st.warning("질문을 입력해 주세요.")
        return

    try:

        with st.spinner(
            "관련 자료를 검색하고 답변을 생성하고 있습니다..."
        ):

            answer, sources = search_and_answer(question)

        st.markdown(
            '<div class="section-title">🤖 AI 검토의견</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="ai-answer">{answer}</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-title">📚 근거자료</div>',
            unsafe_allow_html=True,
        )

        if not sources:

            st.warning("관련 근거자료를 찾지 못했습니다.")
            return

        for i, source in enumerate(sources, start=1):

            title = (
                f"근거 {i} · "
                f"{source['file_name']} · "
                f"{source['page']}페이지"
            )

            with st.expander(title):

                st.write(source["text"])

    except Exception as e:

        st.error("검색 중 오류가 발생했습니다.")
        st.write(e)


# --------------------------------------------------
# 홈
# --------------------------------------------------
if menu == "🏠 홈":

    st.markdown(
        """
        <div class="main-title">
            🌿 개발제한구역 불법행위 업무지원 시스템
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="main-subtitle">
            개발제한구역 업무를 쉽고 빠르게 처리할 수 있도록 지원합니다.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        '<div class="search-title">🔎 통합검색</div>',
        unsafe_allow_html=True,
    )

    with st.form("home_search_form"):

        search = st.text_input(
            "통합검색",
            placeholder="예) 개발제한구역에서 농막을 설치할 수 있나요?",
            label_visibility="collapsed",
        )

        submitted = st.form_submit_button(
            "🔍 검색"
        )

    if submitted:

        show_rag_result(search)

    st.markdown(
        '<div class="section-title">주요 업무 바로가기</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            """
            <div class="work-card">
                <div class="work-card-title">
                    📗 업무가이드
                </div>
                <div class="work-card-text">
                    단속 업무 절차와 업무 기준을 빠르게 확인합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="work-card">
                <div class="work-card-title">
                    🔨 법령·사례 검색
                </div>
                <div class="work-card-text">
                    관련 법령과 업무자료를 RAG 방식으로 검색합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:

        st.markdown(
            """
            <div class="work-card">
                <div class="work-card-title">
                    📋 행정처분 절차
                </div>
                <div class="work-card-text">
                    사전통지부터 이행 확인까지 처리 절차를 확인합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:

        st.markdown(
            """
            <div class="work-card">
                <div class="work-card-title">
                    🧮 이행강제금 계산
                </div>
                <div class="work-card-text">
                    산정기준을 확인하고 금액을 모의 계산합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    notice_col, favorite_col = st.columns(2)

    with notice_col:

        st.markdown(
            """
            <div class="notice-box">
                <h3>📢 공지사항</h3>
                <p>• 개발제한구역법 시행령 개정사항</p>
                <p>• 이행강제금 산정기준 개선 안내</p>
                <p>• 업무가이드 업데이트</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with favorite_col:

        st.markdown(
            """
            <div class="notice-box">
                <h3>⭐ 즐겨찾기</h3>
                <p>• 농막 설치 관련 사례</p>
                <p>• 토지형질변경(성토) 기준</p>
                <p>• 컨테이너 설치 사례</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# --------------------------------------------------
# 업무가이드
# --------------------------------------------------
elif menu == "📗 업무가이드":

    st.markdown(
        '<div class="main-title">📗 업무가이드</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="main-subtitle">
            개발제한구역 내 행위에 필요한 절차와 업무 흐름을 확인합니다.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # --------------------------------------------------
    # 업무 구분
    # --------------------------------------------------
    guide_type = st.radio(
        "업무 구분",
        [
            "📝 행위허가",
            "📋 행위신고",
            "✅ 허가·신고 없이 가능한 행위",
        ],
        horizontal=True,
        key="guide_type",
    )

    st.divider()

    # ==================================================
    # 1. 행위허가
    # ==================================================
    if guide_type == "📝 행위허가":

        st.subheader("📝 행위허가")

        st.info(
            "행위 유형을 먼저 선택한 뒤 허가 대상 여부, "
            "관련 기준, 필요서류를 확인합니다."
        )

        permit_type = st.radio(
            "행위 유형",
            [
                "🏠 건축-신축",
                "🏠 건축-증축·개축",
                "🔁 건축-용도변경",
                "🏗️ 공작물 설치",
                "🌱 토지 형질변경",
                "⛏️ 토석 채취",
                "🌳 죽목 벌채",
                "📐 토지 분할",
                "📦 물건 적치",
            ],
            horizontal=True,
            key="permit_type",
        )

        st.divider()

        with st.expander("📌 기본 업무 흐름 보기", expanded=False):

            permit_steps = [
                "① 신청 행위 내용 확인",
                "② 행위 유형 구분",
                "③ 허가 대상 여부 확인",
                "④ 해당 허가기준 및 제한사항 확인",
                "⑤ 신청서 및 구비서류 확인",
                "⑥ 현장 및 토지 현황 확인",
                "⑦ 관계 법령·별표·관련 사례 검토",
                "⑧ 허가 가능 여부 판단",
                "⑨ 허가 처리 및 사후관리",
            ]

            for step in permit_steps:
                st.success(step)

        st.divider()

        # --------------------------------------------------
        # 건축-신축
        # --------------------------------------------------
        new_building_type = None
        if permit_type == "🏠 건축-신축":

            st.markdown("### 🏠 건축-신축")

            st.markdown("#### ① 신축하려는 시설 선택")

            new_building_type = st.selectbox(
                "시설 종류를 선택하세요",
                [
                    "시설을 선택하세요",
                    "주택",
                    "농림수산업용 시설",
                    "주민공동이용시설",
                    "개발제한구역의 보전·관리에 도움이 되는 시설",
                    "실외체육시설",
                    "근린생활시설",
                    "공익시설",
                    "기타 시설",
                ],
                key="new_building_type",
            )

            if new_building_type == "시설을 선택하세요":

                st.info(
                    "시설을 선택하면 시행령 별표 1을 기준으로 "
                    "검토사항을 안내합니다."
                )

            else:

                st.success(
                    f"선택한 시설: {new_building_type}"
                )

                st.caption(
                    "📚 1차 검토근거: 개발제한구역법 제12조 → "
                    "시행령 제13조 → 시행령 별표 1"
                )

                # ------------------------------------------
                # 주택 신축
                # ------------------------------------------
                if new_building_type == "주택":

                    st.markdown("#### 🏠 주택 신축 검토")

                    house_type = st.radio(
                        "신축 유형을 선택하세요",
                        [
                            "지정 당시부터 지목이 '대'인 토지 또는 기존 주택이 있는 토지에 신축",                           
                            "농업인의 영농 편의를 위한 신축",
                            "공익사업으로 기존 주택이 철거되는 경우",
                            "재해로 기존 주택에 거주할 수 없게 된 경우",
                            "그 밖의 이축·신축 관련 경우",
                            "잘 모르겠음",
                        ],
                        key="house_new_type",
                    )

                    st.info(
                        f"선택한 주택 신축 유형: {house_type}"
                    )

                    if house_type == "지정 당시부터 지목이 '대'인 토지 또는 기존 주택이 있는 토지에 신축":

                        with st.expander(
                            "⚖️ 법령상 신축요건 확인",
                            expanded=False
                        ):
                            st.write(
                                "① 개발제한구역 지정 당시부터 지목이 '대'인 토지인지 확인"
                            )

                            st.write(
                                "② 또는 개발제한구역 지정 당시부터 있던 "
                                "기존 주택이 있는 토지인지 확인"
                            )

                            st.write(
                                "③ 기존 주택의 경우 개발제한구역 건축물관리대장 "
                                "등재 여부를 확인"
                            )

                            st.info(
                                "위 요건 중 어느 유형에 해당하는지 먼저 확인한 후 "
                                "다른 허가기준을 추가로 검토합니다."
                            )

                        with st.expander(
                            "🏡 토지·기존주택 확인",
                            expanded=False
                        ):

                            land_status = st.radio(
                                "대상 토지의 상황을 선택하세요",
                                [
                                    "개발제한구역 지정 당시부터 지목이 '대'인 토지",
                                    "개발제한구역 지정 당시부터 기존 주택이 있는 토지",
                                    "둘 다 해당하지 않음",
                                    "확인되지 않음",
                                ],
                                key="house_land_status",
                            )

                            if land_status == "개발제한구역 지정 당시부터 지목이 '대'인 토지":

                                st.success(
                                    "🟢 지정 당시부터 지목이 '대'인 토지로 확인되었습니다."
                                )

                                st.caption(
                                    "다만 이것만으로 허가가 확정되는 것은 아니며 "
                                    "별표 1의 다른 요건과 별표 2의 허가기준을 함께 검토해야 합니다."
                                )

                            elif land_status == "개발제한구역 지정 당시부터 기존 주택이 있는 토지":

                                existing_house_register = st.radio(
                                    "기존 주택이 개발제한구역 건축물관리대장에 등재되어 있습니까?",
                                    [
                                        "예",
                                        "아니오",
                                        "확인되지 않음",
                                    ],
                                    key="existing_house_register",
                                )

                                if existing_house_register == "예":

                                    st.success(
                                        "🟢 기존 주택 및 건축물관리대장 등재가 확인되었습니다."
                                    )

                                    st.caption(
                                        "이 경우에도 다른 신축요건과 허가기준을 함께 검토해야 합니다."
                                    )

                                elif existing_house_register == "아니오":

                                    st.error(
                                        "🔴 기존 주택 요건에 대한 추가 검토가 필요합니다.\n\n"
                                        "현행 기준상 '기존 주택'은 개발제한구역 건축물관리대장 "
                                        "등재 여부 확인이 중요합니다."
                                    )

                                else:

                                    st.warning(
                                        "🟡 건축물관리대장 등재 여부를 확인해 주세요."
                                    )

                            elif land_status == "둘 다 해당하지 않음":

                                st.warning(
                                    "🟡 이 주택 신축 유형에는 바로 해당하지 않을 수 있습니다.\n\n"
                                    "농업인 신축, 공익사업에 따른 이축, 재해 관련 신축 등 "
                                    "다른 유형에 해당하는지 추가 검토해야 합니다."
                                )

                            else:

                                st.warning(
                                    "🟡 지정 당시 지목 또는 기존 주택 여부를 먼저 확인해 주세요."
                                )




                        with st.expander(
                            "📐 주택 건축 규모 검토",
                            expanded=False
                        ):

                            st.markdown("##### ① 취락지구 여부 확인")

                            settlement_area = st.radio(
                                "대상 토지가 취락지구 안에 있습니까?",
                                [
                                    "아니오",
                                    "예",
                                    "확인되지 않음",
                                ],
                                key="house_settlement_area",
                                horizontal=True,
                            )

                            if settlement_area == "예":
                                st.info(
                                    "🏘️ 취락지구입니다. "
                                    "개발제한구역법 시행령 제26조의 특례 기준을 "
                                    "함께 적용하여 검토합니다."
                                )

                            elif settlement_area == "확인되지 않음":
                                st.warning(
                                    "🟡 취락지구 여부를 먼저 확인해 주세요. "
                                    "취락지구 여부에 따라 건축 규모 기준이 달라질 수 있습니다."
                                )

                            else:
                                st.info(
                                    "취락지구 밖의 개발제한구역 기준으로 검토합니다."
                                )

                            st.divider()

                            st.markdown("##### ② 적용할 건폐율 기준")


                            if settlement_area == "예":
                                ratio_options = [
                                    "건폐율 60% 이하",
                                    "건폐율 40% 이하",
                                    "잘 모르겠음",
                                ]

                            elif settlement_area == "아니오":
                                ratio_options = [
                                    "건폐율 60% 이하",
                                    "건폐율 20% 이하",
                                    "잘 모르겠음",
                                ]

                            else:
                                ratio_options = [
                                    "잘 모르겠음",
                                ]

                            building_ratio_type = st.radio(
                                "건폐율 기준을 선택하세요",
                                ratio_options,
                                key="house_building_ratio_type",
                            )

                            if building_ratio_type == "잘 모르겠음":                        
                                st.warning(
                                    "🟡 건폐율 기준을 먼저 확인해 주세요. "
                                    "취락지구 여부와 적용 가능한 건폐율 기준이 확인되어야 "
                                    "건축 규모를 정확하게 검토할 수 있습니다."
                                )

                            st.markdown("##### ③ 건축계획 입력")

                            building_ratio = st.number_input(
                                "계획 건폐율(%)",
                                min_value=0.0,
                                max_value=100.0,
                                step=1.0,
                                key="house_building_ratio",
                            )

                            floor_area_ratio = st.number_input(
                                "계획 용적률(%)",
                                min_value=0.0,
                                step=1.0,
                                key="house_floor_area_ratio",
                            )

                            floors = st.number_input(
                                "계획 층수",
                                min_value=1,
                                step=1,
                                key="house_floors",
                            )

                            total_area = st.number_input(
                                "기존 면적을 포함한 연면적(㎡)",
                                min_value=0.0,
                                step=1.0,
                                key="house_total_area",
                            )

                            # ----------------------------------
                            # 건폐율 60% 이하 방식
                            # ----------------------------------

                            if building_ratio_type == "건폐율 60% 이하":

                                problems = []

                                # ----------------------------------
                                # 취락지구 안
                                # ----------------------------------
                                if settlement_area == "예":

                                    max_total_area = 300.0

                                    if building_ratio > 60:
                                        problems.append("건폐율 60% 초과")

                                    if floor_area_ratio > 300:
                                        problems.append("용적률 300% 초과")

                                    if floors > 3:
                                        problems.append("높이 3층 초과")

                                    if total_area > max_total_area:
                                        problems.append("연면적 300㎡ 초과")

                                    if problems:
                                        st.error(
                                            "🔴 취락지구 규모 기준과 맞지 않는 항목\n\n"
                                            + "\n\n".join(
                                                f"• {item}" for item in problems
                                            )
                                        )

                                    elif total_area == 0:
                                        st.info(
                                            "연면적을 입력하면 규모 기준을 검토합니다."
                                        )

                                    else:
                                        st.success(
                                            "🟢 입력한 내용은 취락지구의 "
                                            "건폐율 60% 이하 규모 기준 범위 안에 있습니다."
                                        )

                                    st.caption(
                                        "📚 취락지구 검토근거: "
                                        "개발제한구역법 시행령 제26조제1항제2호가목"
                                    )

                                # ----------------------------------
                                # 취락지구 밖
                                # ----------------------------------
                                elif settlement_area == "아니오":

                                    resident_type = st.radio(
                                        "거주자 유형",
                                        [
                                            "일반",
                                            "지정당시거주자",
                                            "확인되지 않음",
                                        ],
                                        key="house_resident_type",
                                    )

                                    if resident_type == "지정당시거주자":
                                        max_total_area = 300.0
                                    else:
                                        max_total_area = 232.0

                                    if building_ratio > 60:
                                        problems.append("건폐율 60% 초과")

                                    if floor_area_ratio > 300:
                                        problems.append("용적률 300% 초과")

                                    if floors > 3:
                                        problems.append("층수 기준 초과(3층 초과)")

                                    if total_area > max_total_area:
                                        problems.append(
                                            f"연면적 {max_total_area:.0f}㎡ 초과"
                                        )

                                    if resident_type == "확인되지 않음":
                                        st.warning(
                                            "🟡 거주자 유형 확인이 필요합니다."
                                        )

                                    elif problems:
                                        st.error(
                                            "🔴 규모 기준과 맞지 않는 항목\n\n"
                                            + "\n\n".join(
                                                f"• {item}" for item in problems
                                            )
                                        )

                                    elif total_area == 0:
                                        st.info(
                                            "연면적을 입력하면 규모 기준을 검토합니다."
                                        )

                                    else:
                                        st.success(
                                            "🟢 입력한 내용은 취락지구 밖의 "
                                            "건폐율 60% 이하 규모 기준 범위 안에 있습니다."
                                        )

                                    if (
                                        resident_type == "지정당시거주자"
                                        and total_area > 232
                                        and total_area <= 300
                                    ):
                                        st.warning(
                                            "🟡 지정당시거주자가 연면적 232㎡를 "
                                            "초과하여 300㎡까지 건축할 수 있는 것은 "
                                            "1회로 제한되므로 기존 이용 여부를 "
                                            "추가 확인해야 합니다."
                                        )

                                    st.caption(
                                        "📚 취락지구 밖 검토근거: "
                                        "개발제한구역법 시행령 별표 2"
                                    )

                                # ----------------------------------
                                # 취락지구 여부 미확인
                                # ----------------------------------
                                else:

                                    st.warning(
                                        "🟡 취락지구 여부를 먼저 확인해야 "
                                        "건축 규모 기준을 정확히 적용할 수 있습니다."
                                    )

                            # ----------------------------------
                            # 취락지구 건폐율 40% 이하 방식
                            # ----------------------------------
                            elif building_ratio_type == "건폐율 40% 이하":

                                problems = []

                                if building_ratio > 40:
                                    problems.append("건폐율 40% 초과")

                                if floor_area_ratio > 100:
                                    problems.append("용적률 100% 초과")

                                if floors > 3:
                                    problems.append("높이 3층 초과")

                                if problems:
                                    st.error(
                                        "🔴 취락지구 규모 기준과 맞지 않는 항목\n\n"
                                        + "\n\n".join(
                                            f"• {item}" for item in problems
                                        )
                                    )

                                else:
                                    st.success(
                                        "🟢 입력한 내용은 취락지구의 "
                                        "건폐율 40% 이하 규모 기준 범위 안에 있습니다."
                                    )

                            # ----------------------------------
                            # 건폐율 20% 이하 방식
                            # ----------------------------------
                            elif building_ratio_type == "건폐율 20% 이하":

                                problems = []

                                if building_ratio > 20:
                                    problems.append("건폐율 20% 초과")

                                if floor_area_ratio > 100:
                                    problems.append("용적률 100% 초과")

                                if floors > 3:
                                    problems.append("층수 기준 초과(3층 초과)")

                                if problems:
                                    st.error(
                                        "🔴 규모 기준과 맞지 않는 항목\n\n"
                                        + "\n\n".join(
                                            f"• {item}" for item in problems
                                        )
                                    )

                                else:
                                    st.success(
                                        "🟢 입력한 내용은 선택한 규모 기준의 "
                                        "범위 안에 있습니다."
                                    )

                            else:
                                st.warning(
                                    "🟡 적용할 건폐율 기준을 먼저 확인해 주세요."
                                )

                            st.caption(
                                "📚 검토근거: 개발제한구역법 시행령 "
                                "별표 2 제2호 나목"
                            )

                            st.caption(
                                "※ 이 결과는 건축 규모에 대한 1차 검토입니다. "
                                "별표 1의 신축요건과 다른 허가기준도 함께 "
                                "검토해야 합니다."
                            )

                            st.markdown("##### 📐 대지면적 확인")

                            site_area = st.number_input(
                                "건축하려는 대지면적(㎡)",
                                min_value=0.0,
                                step=1.0,
                                key="house_site_area",
                            )

                            if site_area == 0:
                                st.info("대지면적을 입력해 주세요.")

                            elif site_area < 60:
                                st.error(
                                    "🔴 별표 2 기준 추가 확인 필요\n\n"
                                    "건축물을 건축하기 위한 대지면적이 "
                                    "60㎡ 미만인 경우에는 원칙적으로 "
                                    "건축을 허가하지 않습니다."
                                )

                            else:
                                st.success(
                                    "🟢 대지면적 60㎡ 이상 기준을 충족합니다."
                                )

                            st.divider()

                            st.markdown("##### 🌳 일반적 허가기준")

                            st.checkbox(
                                "개발제한구역 훼손을 최소화하는 규모인지 확인",
                                key="house_general_1"
                            )

                            st.checkbox(
                                "주변지역의 환경오염·생태계 파괴·위해 발생 여부 확인",
                                key="house_general_2"
                            )

                            st.checkbox(
                                "역사적·문화적·향토적 가치가 있는 지역의 훼손 여부 확인",
                                key="house_general_3"
                            )

                            land_change = st.checkbox(
                                "토지의 형질변경이 수반됨",
                                key="house_land_change"
                            )

                            if land_change:
                                st.warning(
                                    "🟡 표고·경사도·숲의 상태·인근 도로의 높이·"
                                    "배수 등을 추가로 검토해야 합니다."
                                )

                            st.caption(
                                "📚 검토근거: 개발제한구역법 제12조제9항 → "
                                "시행령 제22조 → 시행령 별표 2"
                            )                           

                        with st.expander(
                            "📚 근거 법령 보기",
                            expanded=False
                        ):

                            st.write(
                                "• 개발제한구역법 제12조"
                            )

                            st.write(
                                "• 개발제한구역법 시행령 제13조제1항"
                            )

                            st.write(
                                "• 개발제한구역법 시행령 별표 1 제5호 다목"
                            )

                            st.caption(
                                "주택: 「건축법 시행령」 별표 1 "
                                "제1호가목에 따른 단독주택"
                            )

                            st.warning(
                                "※ 이 화면은 1차 검토용입니다. "
                                "실제 허가 여부는 별표 1의 나머지 요건, "
                                "별표 2의 세부기준 및 관련 법령을 함께 확인해야 합니다."
                            )

                    elif house_type == "공익사업으로 기존 주택이 철거되는 경우":

                        st.markdown("#### 🏗️ 공익사업으로 기존 주택이 철거되는 경우 검토")

                        with st.expander(
                            "① 철거 원인 및 기존주택 확인",
                            expanded=False
                        ):

                            public_project = st.radio(
                                "기존 주택이 공익사업 시행으로 철거되는 경우입니까?",
                                [
                                    "예",
                                    "아니오",
                                    "확인되지 않음",
                                ],
                                key="public_project_house",
                            )

                            existing_house_confirmed = st.radio(
                                "철거되는 건축물이 기존 주택으로 확인됩니까?",
                                [
                                    "예",
                                    "아니오",
                                    "확인되지 않음",
                                ],
                                key="public_project_existing_house",
                            )

                            if (
                                public_project == "예"
                                and existing_house_confirmed == "예"
                            ):
                                st.success(
                                    "🟢 공익사업에 따른 기존 주택 철거 기본요건은 "
                                    "충족 가능성이 있습니다."
                                )

                            elif (
                                public_project == "아니오"
                                or existing_house_confirmed == "아니오"
                            ):
                                st.error(
                                    "🔴 이 신축 유형의 기본요건과 맞지 않는 항목이 있습니다."
                                )

                            else:
                                st.warning(
                                    "🟡 공익사업 여부와 기존 주택 여부를 추가 확인해 주세요."
                                )

                    elif house_type == "재해로 기존 주택에 거주할 수 없게 된 경우":

                        st.markdown("#### 🌧️ 재해로 기존 주택에 거주할 수 없게 된 경우 검토")

                        with st.expander(
                            "① 재해 및 기존주택 상태 확인",
                            expanded=False
                        ):

                            disaster_occurred = st.radio(
                                "화재·수해 등 재해로 기존 주택에 거주할 수 없게 된 경우입니까?",
                                [
                                    "예",
                                    "아니오",
                                    "확인되지 않음",
                                ],
                                key="disaster_house_occurred",
                            )

                            existing_house_uninhabitable = st.radio(
                                "기존 주택이 실제로 거주하기 어려운 상태로 확인됩니까?",
                                [
                                    "예",
                                    "아니오",
                                    "확인되지 않음",
                                ],
                                key="disaster_house_uninhabitable",
                            )

                            if (
                                disaster_occurred == "예"
                                and existing_house_uninhabitable == "예"
                            ):
                                st.success(
                                    "🟢 재해 및 기존 주택 상태에 대한 기본요건은 "
                                    "충족 가능성이 있습니다."
                                )

                            elif (
                                disaster_occurred == "아니오"
                                or existing_house_uninhabitable == "아니오"
                            ):
                                st.error(
                                    "🔴 이 신축 유형의 기본요건과 맞지 않는 항목이 있습니다."
                                )

                            else:
                                st.warning(
                                    "🟡 재해 발생 여부와 기존 주택 상태를 추가 확인해 주세요."
                                )

                        with st.expander(
                            "② 현장 및 증빙자료 확인",
                            expanded=False
                        ):

                            st.checkbox(
                                "재해 발생 사실을 확인할 수 있는 자료 확인",
                                key="disaster_check_1",
                            )
                            st.checkbox(
                                "기존 주택 현장상태 및 사진 확인",
                                key="disaster_check_2",
                            )
                            st.checkbox(
                                "건축물대장 등 기존 주택 관련 자료 확인",
                                key="disaster_check_3",
                            )
                            st.checkbox(
                                "신축 예정지 및 현장여건 확인",
                                key="disaster_check_4",
                            )

                            st.info(
                                "재해 발생 사실, 기존 주택의 실제 상태 및 신축 예정지의 "
                                "현장여건을 관련 서류와 함께 확인해야 합니다."
                            )
                    elif house_type == "그 밖의 이축·신축 관련 경우":

                        st.markdown("#### 🏠 그 밖의 이축·신축 관련 경우 검토")

                        with st.expander(
                            "① 이축·신축 사유 확인",
                            expanded=False
                        ):

                            other_reason_confirmed = st.radio(
                                "법령상 허용되는 그 밖의 이축·신축 사유에 해당합니까?",
                                [
                                    "예",
                                    "아니오",
                                    "확인되지 않음",
                                ],
                                key="other_house_reason",
                            )

                            relocation_needed = st.radio(
                                "기존 주택의 철거·이축 또는 신축 필요성이 확인됩니까?",
                                [
                                    "예",
                                    "아니오",
                                    "확인되지 않음",
                                ],
                                key="other_house_relocation",
                            )

                            if (
                                other_reason_confirmed == "예"
                                and relocation_needed == "예"
                            ):
                                st.success(
                                    "🟢 그 밖의 이축·신축 관련 기본요건은 "
                                    "충족 가능성이 있습니다."
                                )

                            elif (
                                other_reason_confirmed == "아니오"
                                or relocation_needed == "아니오"
                            ):
                                st.error(
                                    "🔴 이 신축 유형의 기본요건과 맞지 않는 항목이 있습니다."
                                )

                            else:
                                st.warning(
                                    "🟡 이축·신축 사유와 기존 주택 상태를 추가 확인해 주세요."
                                )

                        with st.expander(
                            "② 관련 서류 및 현장 확인",
                            expanded=False
                        ):

                            st.checkbox(
                                "기존 주택의 존재 및 상태 확인",
                                key="other_house_check_1",
                            )
                            st.checkbox(
                                "이축 또는 신축 사유를 증명하는 자료 확인",
                                key="other_house_check_2",
                            )
                            st.checkbox(
                                "신축 예정지 및 현장여건 확인",
                                key="other_house_check_3",
                            )
                            st.checkbox(
                                "관련 법령·별표의 세부요건 확인",
                                key="other_house_check_4",
                            )

                            st.info(
                                "그 밖의 이축·신축은 구체적인 사유에 따라 적용 기준이 달라질 수 있으므로 "
                                "관련 서류와 최신 법령을 함께 확인해야 합니다."
                            )        

                    elif house_type == "농업인의 영농 편의를 위한 신축":

                        st.markdown("#### 🌾 농업인의 영농 편의를 위한 주택 신축 검토")

                        with st.expander(
                            "① 농업인·기존주택 요건 확인",
                            expanded=False
                        ):

                            is_farmer = st.radio(
                                "신청인이 농업인에 해당합니까?",
                                [
                                    "예",
                                    "아니오",
                                    "확인되지 않음",
                                ],
                                key="farmer_house_is_farmer",
                            )

                            has_Errorexisting_house = st.radio(
                                "개발제한구역 안에 자기 소유의 기존 주택이 있습니까?",
                                [
                                    "예",
                                    "아니오",
                                    "확인되지 않음",
                                ],
                                key="farmer_house_existing",
                            )

                            will_remove_existing = st.radio(
                                "기존 주택을 철거하고 신축할 계획입니까?",
                                [
                                    "예",
                                    "아니오",
                                    "확인되지 않음",
                                ],
                                key="farmer_house_remove_existing",
                            )

                            if (
                                is_farmer == "예"
                                and has_Errorexisting_house == "예"
                                and will_remove_existing == "예"
                            ):
                                st.success(
                                    "🟢 농업인 및 기존 주택 관련 기본요건은 "
                                    "충족 가능성이 있습니다."
                                )

                            elif (
                                is_farmer == "아니오"
                                or has_Errorexisting_house == "아니오"
                                or will_remove_existing == "아니오"
                            ):
                                st.error(
                                    "🔴 이 신축 유형의 기본요건과 맞지 않는 항목이 있습니다."
                                )

                            else:
                                st.warning(
                                    "🟡 농업인 여부 또는 기존 주택 관련 사실관계 확인이 필요합니다."
                                )


                        with st.expander(
                            "② 농장·과수원 및 영농 규모 확인",
                            expanded=False
                        ):

                            owns_farm = st.radio(
                                "자기 소유의 농장 또는 과수원에 주택을 신축하려는 경우입니까?",
                                [
                                    "예",
                                    "아니오",
                                    "확인되지 않음",
                                ],
                                key="farmer_house_owns_farm",
                            )

                            farm_area = st.number_input(
                                "생산에 직접 이용되는 토지 면적(㎡)",
                                min_value=0.0,
                                step=100.0,
                                key="farmer_house_farm_area",
                            )

                            if owns_farm == "아니오":
                                st.error(
                                    "🔴 자기 소유 농장·과수원 요건을 추가 검토해야 합니다."
                                )

                            elif farm_area == 0:
                                st.info(
                                    "영농에 직접 이용되는 토지 면적을 입력해 주세요."
                                )

                            elif farm_area < 10000:
                                st.warning(
                                    "🟡 입력 면적이 10,000㎡ 미만입니다. "
                                    "별표 1의 해당 요건 충족 여부를 다시 확인해야 합니다."
                                )

                            else:
                                st.success(
                                    "🟢 입력된 영농 면적은 10,000㎡ 이상입니다."
                                )


                        with st.expander(
                            "③ 진입로·형질변경 확인",
                            expanded=False
                        ):

                            access_road_change = st.radio(
                                "주택 진입로 설치를 위해 새로 토지 형질변경이 필요합니까?",
                                [
                                    "아니오",
                                    "예",
                                    "확인되지 않음",
                                ],
                                key="farmer_house_access_road",
                            )

                            if access_road_change == "아니오":
                                st.success(
                                    "🟢 진입로 설치를 위한 별도 형질변경이 필요하지 않은 것으로 입력되었습니다."
                                )

                            elif access_road_change == "예":
                                st.warning(
                                    "🟡 진입로 설치를 위한 토지 형질변경이 수반되는 경우 "
                                    "이 신축 유형의 세부요건을 다시 확인해야 합니다."
                                )

                            else:
                                st.warning(
                                    "🟡 진입로 및 형질변경 여부를 확인해 주세요."
                                )


                        with st.expander(
                            "📚 관련 법령 근거",
                            expanded=False
                        ):

                            st.write("• 개발제한구역법 제12조")
                            st.write("• 개발제한구역법 시행령 제13조제1항")
                            st.write("• 개발제한구역법 시행령 별표 1 제5호 다목")
                            st.write("• 개발제한구역법 시행령 별표 2")

                            st.caption(
                                "※ 실제 허가 여부는 신청인의 농업인 해당 여부, "
                                "소유·거주관계, 영농 토지 및 현장여건 등을 "
                                "관련 서류와 최신 법령으로 최종 확인해야 합니다."
                            )
        if permit_type == "🏠 건축-신축" and new_building_type == "농림수산업용 시설":
            st.markdown("#### 🌾 농림수산업용 시설 신축 검토")

            st.info(
                "농림수산업용 시설의 설치 가능 여부와 "
                "개발제한구역 관련 허가기준을 확인합니다."
            )

            st.markdown("##### ② 허가기준 확인")

            st.warning(
                "시설의 종류, 신청인의 자격, 규모 및 입지조건 등 "
                "시행령 별표 1의 해당 기준을 확인해야 합니다."
            )

            st.markdown("##### ③ 검토 결과")

            st.success(
                "✅ 행위허가 검토 대상입니다. "
                "세부 허가기준과 신청서류를 확인한 후 허가 여부를 결정합니다."
            )

            with st.expander("📚 관련 법령 근거", expanded=False):
                st.write("• 개발제한구역의 지정 및 관리에 관한 특별조치법 제12조")
                st.write("• 같은 법 시행령 제13조")
                st.write("• 같은 법 시행령 별표 1")

        if new_building_type == "주민공동이용시설":
            st.markdown("#### 🏘️ 주민공동이용시설 신축 검토")

            st.info(
                "주민공동이용시설의 설치 가능 여부와 "
                "개발제한구역 관련 허가기준을 확인합니다."
            )

            st.markdown("##### ② 허가기준 확인")

            st.warning(
                "개발제한구역법 시행령 별표 1의 "
                "주민공동이용시설 관련 설치기준을 확인해야 합니다."
            )

            st.markdown("##### ③ 검토 결과")

            st.success(
                "✅ 행위허가 검토 대상입니다. "
                "세부 설치기준과 신청서류를 확인한 후 허가 여부를 결정합니다."
            )

            with st.expander("📚 관련 법령 근거", expanded=False):
                st.write("• 개발제한구역의 지정 및 관리에 관한 특별조치법 제12조")
                st.write("• 같은 법 시행령 제13조")
                st.write("• 같은 법 시행령 별표 1")

        other_new_building_types = [
            "개발제한구역의 보전·관리에 도움이 되는 시설",
            "실외체육시설",
            "근린생활시설",
            "공익시설",
            "기타 시설",
        ]

        if new_building_type in other_new_building_types:
            st.markdown(f"#### 🏗️ {new_building_type} 신축 검토")

            st.info(
                f"{new_building_type}의 설치 가능 여부와 "
                "개발제한구역 관련 허가기준을 확인합니다."
            )

            st.markdown("##### ② 허가기준 확인")

            st.warning(
                "개발제한구역법 시행령 별표 1의 "
                "해당 시설별 설치기준을 확인해야 합니다."
            )

            st.markdown("##### ③ 검토 결과")

            st.success(
                "✅ 행위허가 검토 대상입니다. "
                "세부 설치기준과 신청서류를 확인한 후 허가 여부를 결정합니다."
            )

            with st.expander("📚 관련 법령 근거", expanded=False):
                st.write("• 개발제한구역의 지정 및 관리에 관한 특별조치법 제12조")
                st.write("• 같은 법 시행령 제13조")
                st.write("• 같은 법 시행령 별표 1")
                
if (
    menu == "📗 업무가이드"
    and st.session_state.get("permit_type") == "🏠 건축-증축·개축"
):

    st.markdown("### 🏠 건축·증축·개축")

    st.info(
        "기존 건축물의 증축·개축 가능 여부와 규모, "
        "기존 건축물의 적법성, 관련 허가기준을 함께 확인합니다."
    )

    with st.expander(
        "① 기존 건축물 적법성 확인",
        expanded=False
    ):

        existing_building_legal = st.radio(
            "기존 건축물이 적법하게 건축된 건축물입니까?",
            [
                "예",
                "아니오",
                "확인되지 않음",
            ],
            key="ext_existing_building_legal",
        )

        if existing_building_legal == "예":
            st.success(
                "🟢 기존 건축물의 적법성은 확인된 것으로 입력되었습니다."
            )

        elif existing_building_legal == "아니오":
            st.error(
                "🔴 기존 건축물의 적법성 확인이 필요합니다."
            )

        else:
            st.warning(
                "🟡 건축물대장·허가서류 등을 통해 기존 건축물의 적법성을 확인해 주세요."
            )

    with st.expander(
        "② 증축·개축 내용 확인",
        expanded=False
    ):

        extension_type = st.radio(
            "검토하려는 행위는 무엇입니까?",
            [
                "증축",
                "개축",
                "확인되지 않음",
            ],
            key="ext_action_type",
        )

        extension_area = st.number_input(
            "증가 또는 변경되는 연면적(㎡)",
            min_value=0.0,
            step=1.0,
            key="ext_area",
        )

        floors_after = st.number_input(
            "변경 후 층수",
            min_value=1,
            step=1,
            key="ext_floors_after",
        )

        if extension_type == "확인되지 않음":
            st.warning(
                "🟡 증축인지 개축인지 먼저 확인해 주세요."
            )

        elif extension_area == 0:
            st.info(
                "증가 또는 변경되는 연면적을 입력해 주세요."
            )

        else:
            st.success(
                "🟢 증축·개축 기본 입력이 완료되었습니다."
            )

    with st.expander(
        "③ 현장 및 관련 서류 확인",
        expanded=False
    ):

        st.checkbox(
            "건축물대장 확인",
            key="ext_check_1",
        )
        st.checkbox(
            "기존 허가·신고 서류 확인",
            key="ext_check_2",
        )
        st.checkbox(
            "현장 상태 및 사진 확인",
            key="ext_check_3",
        )
        st.checkbox(
            "증축·개축 후 건폐율·용적률·층수 검토",
            key="ext_check_4",
        )
        st.checkbox(
            "개발제한구역 허가기준 및 별표 확인",
            key="ext_check_5",
        )

        st.info(
            "기존 건축물의 적법성, 증축·개축 규모, "
            "건폐율·용적률·층수 및 별표의 세부요건을 함께 확인해야 합니다."
        )

    with st.expander(
        "📚 관련 법령 근거",
        expanded=False
    ):

        st.write("• 개발제한구역법 제12조")
        st.write("• 개발제한구역법 시행령 제13조")
        st.write("• 개발제한구역법 시행령 별표 1")
        st.write("• 필요 시 시행령 별표 2 및 시행규칙 확인")

        st.caption(
            "※ 이 화면은 1차 검토용입니다. "
            "실제 허가 여부는 최신 법령과 개별 현장여건을 함께 확인해야 합니다."
        )

# ---------------------------------------------
# 건축-용도변경
# ---------------------------------------------

if (
    menu == "📗 업무가이드"
    and "건축-용도변경" in st.session_state.get("permit_type", "")
):
    st.markdown("### 🔄 건축-용도변경")
    st.info("기존 건축물의 용도를 변경하려는 경우 허가 가능 여부와 관련 기준을 확인합니다.")
    st.markdown("#### ① 기존 건축물 확인")

    existing_building = st.radio(
        "용도변경하려는 건축물의 상태를 선택하세요.",
        [
            "선택하세요",
            "건축물대장에 등재된 기존 건축물",
            "건축물대장 등재 여부를 확인해야 함",
        ],
        key="change_use_existing_building",
    )
    if existing_building == "건축물대장에 등재된 기존 건축물":
        st.success("🟢 건축물대장에 등재된 기존 건축물입니다. 다음 단계로 진행합니다.")

    elif existing_building == "건축물대장 등재 여부를 확인해야 함":
        st.warning("🟡 먼저 건축물대장에서 건축물의 등재 여부와 현재 용도를 확인하세요.")
    st.markdown("#### ② 현재 용도와 변경하려는 용도 확인")

    current_use = st.text_input(
        "현재 건축물의 용도를 입력하세요.",
        key="change_use_current",
    )

    target_use = st.text_input(
        "변경하려는 용도를 입력하세요.",
        key="change_use_target",
    )
    if current_use and target_use:
        st.info(
            f"📋 현재 용도: {current_use} → 변경하려는 용도: {target_use}"
        )
        st.warning(
            "🟡 용도변경 가능 여부는 변경하려는 용도가 개발제한구역에서 "
            "허용되는 용도인지 추가 확인해야 합니다."
        )
    st.markdown("#### ③ 용도변경 허용기준 확인")

    use_change_check = st.radio(
        "변경하려는 용도가 개발제한구역에서 허용되는 용도인지 확인했나요?",
        [
            "선택하세요",
            "허용되는 용도임을 확인함",
            "아직 확인하지 못함",
        ],
        key="change_use_allowed",
    )
    if use_change_check == "허용되는 용도임을 확인함":
        st.success("🟢 개발제한구역에서 허용되는 용도임을 확인했습니다.")

    elif use_change_check == "아직 확인하지 못함":
        st.warning("🟡 관련 법령과 허가기준을 추가로 확인해야 합니다.")
    st.markdown("#### ④ 최종 검토사항")

    st.checkbox(
        "건축물대장의 현재 용도 확인",
        key="change_use_final_1",
    )
    st.checkbox(
        "변경하려는 용도의 개발제한구역 허용 여부 확인",
        key="change_use_final_2",
    )
    st.checkbox(
        "관련 허가기준 및 제한사항 확인",
        key="change_use_final_3",
    )
    st.checkbox(
        "현장 여건 및 다른 법령 저촉 여부 확인",
        key="change_use_final_4",
    )
    if (
        existing_building == "건축물대장에 등재된 기존 건축물"
        and current_use
        and target_use
        and use_change_check == "허용되는 용도임을 확인함"
    ):
        st.success(
            "🟢 1차 검토 결과: 용도변경 검토를 계속 진행할 수 있습니다. "
            "최종 허가 여부는 관련 법령, 허가기준, 현장여건을 함께 확인해야 합니다."
        )
    else:
        st.warning(
            "🟡 1차 검토 결과: 아직 확인되지 않은 사항이 있습니다. "
            "건축물대장, 변경 용도, 허용기준을 추가로 확인하세요."
        )

if (
    "업무가이드" in menu
    and "공작물 설치" in st.session_state.get("permit_type", "")
):

        st.markdown("### 🏗️ 공작물 설치")
        st.info(
            "공작물 설치의 허가 가능 여부와 관련 기준을 단계별로 확인합니다."
        )

        st.markdown("#### ① 설치하려는 공작물 종류")

        structure_type = st.selectbox(  
            "공작물 종류를 선택하세요.",
            [
                "선택하세요",
                "담장·옹벽",
                "철탑·통신탑",
                "광고판·광고탑",
                "태양광 관련 구조물",
                "저장조·탱크",
                "컨테이너·기타 구조물",
                "기타 공작물",
            ],
            key="structure_type",
        )

        if structure_type != "선택하세요":
            st.markdown("#### ② 허가대상 여부 확인")

            permit_check = st.radio(
                "이 공작물이 개발제한구역에서 허가대상인지 확인하셨나요?",
                [
                    "선택하세요",
                    "허가대상임을 확인함",
                    "아직 확인하지 못함",
                ],
                key="structure_permit_check",
            )

            if structure_type != "선택하세요" and permit_check == "허가대상임을 확인함":
                st.success("🟢 허가대상 여부를 확인했습니다. 다음 단계로 진행할 수 있습니다.")
            elif permit_check == "아직 확인하지 못함":
                st.warning("🟡 관련 법령과 허가기준을 먼저 확인해야 합니다.")

        if structure_type != "선택하세요" and permit_check == "허가대상임을 확인함":
            st.markdown("#### ③ 설치 위치·규모 확인")

            location_check = st.radio(
                "설치 위치와 공작물의 규모를 확인하셨나요?",
                [
                    "선택하세요",
                    "확인함",
                    "아직 확인하지 못함",
                ],
                key="structure_location_check",
            )

            if structure_type != "선택하세요" and permit_check == "허가대상임을 확인함" and location_check == "확인함":
                st.success("🟢 설치 위치와 공작물 규모를 확인했습니다. 다음 단계로 진행할 수 있습니다.")
            elif structure_type != "선택하세요" and permit_check == "허가대상임을 확인함" and location_check == "아직 확인하지 못함":
                st.warning("🟡 설치 위치와 공작물 규모를 먼저 확인해야 합니다.")

        if structure_type != "선택하세요" and permit_check == "허가대상임을 확인함" and location_check == "확인함":
            st.markdown("#### ④ 관련 허가기준 확인")

            st.info("📌 아래 허가기준을 먼저 확인한 후 확인 여부를 선택하세요.")

        if structure_type == "담장·옹벽":
            st.write("📋 담장 관련 허가기준")

            st.info("""
            ✅ 담장 허가기준

            • 주택을 관리하기 위한 담장
            - 높이 2m 미만
            - 택지 조성을 위한 경우 제외
            - 허가 또는 신고 없이 설치 가능

            • 주택이 아닌 허가받은 건축물의 담장
            - 높이 2m 미만
            - 추가 설치하는 경우 신고 대상

            • 건축물이 없는 토지
            - 토지 관리를 위한 담장 설치는 위 예외규정 적용 불가
            """)

        if structure_type == "담장·옹벽":
                
                    fence_target = st.radio(
                        "담장 설치 대상은 무엇인가요?",
                        [
                            "선택하세요",
                            "주택",
                            "주택이 아닌 허가받은 건축물",
                            "건축물이 없는 토지"
                        ],
                        key="fence_target"
                    )            

                    if fence_target not in ["선택하세요", "건축물이 없는 토지"]:
                        fence_height = st.radio(
                            "담장 높이가 2m 미만인가요?",
                            [
                                "선택하세요",
                                "예",
                                "아니오"
                            ],
                            key="fence_height"
                        )

                    if fence_target == "주택" and fence_height == "예":
                        st.success("🟢 주택을 관리하기 위한 높이 2m 미만의 담장은 허가 또는 신고 없이 설치할 수 있습니다.")

                    elif fence_target == "건축물이 없는 토지":
                        st.error("🔴 건축물이 없는 토지의 관리를 위한 담장 설치는 위 예외규정을 적용할 수 없습니다.")

                    elif fence_target == "주택이 아닌 허가받은 건축물" and fence_height == "예":
                        st.warning("🟡 허가받은 건축물에 높이 2m 미만의 담장을 추가로 설치하는 경우 신고 대상입니다.")

                    elif fence_target in ["주택", "주택이 아닌 허가받은 건축물"] and fence_height == "아니오":
                        st.warning("🟡 높이 2m 이상인 담장은 2m 미만 담장 기준에 해당하지 않으므로 별도의 허가 가능 여부를 검토해야 합니다.")

                    if structure_type == "담장·옹벽":
                        standard_check = "확인함"
                    else:
                    
                        st.markdown("**허가기준 안내**")            

                        standard_check = st.radio(
                            "공작물의 종류·규모에 따른 관련 허가기준을 확인하셨나요?",
                            [
                                "선택하세요",
                                "확인함",
                                "아직 확인하지 못함",
                            ],
                            key="structure_standard_check",
                        )

                        if standard_check == "확인함":
                            st.success("🟢 관련 허가기준을 확인했습니다. 다음 단계로 진행할 수 있습니다.")
                        elif standard_check == "아직 확인하지 못함":
                            st.warning("🟡 공작물의 종류·규모에 따른 관련 허가기준을 먼저 확인해야 합니다.")

                    document_check = "선택하세요"

                    if structure_type == "담장·옹벽":

                        if fence_target == "주택" and fence_height == "예":
                            st.markdown("##### ⑤ 필요서류 확인")
                            st.info("📄 허가 또는 신고 없이 설치 가능한 경우이므로 별도의 허가·신고 신청서류는 필요하지 않습니다.")
                            document_check = "확인함"

                        elif fence_target == "주택이 아닌 허가받은 건축물" and fence_height == "예":
                            st.markdown("##### ⑤ 필요서류 확인")

                            st.info("""
                            📄 신고 관련 서류

                            • 「건축법 시행규칙」에 따른 해당 신고서
                            • 위치도
                            • 사업계획도서
                            • 그 밖에 신고사항을 증명하는 서류

                            ※ 현장 조건에 따라 추가서류 여부를 확인해야 합니다.
                            """)

                            document_check = st.radio(
                                "위 신고 관련 서류를 확인하셨나요?",
                                [
                                    "선택하세요",
                                    "확인함",
                                    "아직 확인하지 못함"
                                ],
                                key="fence_document_check"
                            )

                            if document_check == "확인함":
                                st.success("🟢 신고 관련 서류를 확인했습니다. 다음 단계로 진행할 수 있습니다.")
                            elif document_check == "아직 확인하지 못함":
                                st.warning("🟡 신고 관련 서류를 먼저 확인해야 합니다.")

                    else:

                        if (
                            structure_type != "선택하세요"
                            and permit_check == "허가대상임을 확인함"
                            and location_check == "확인함"
                            and standard_check == "확인함"
                        ):
                            st.markdown("##### ⑤ 필요서류 확인")

                            document_check = st.radio(
                                "공작물 설치 허가에 필요한 신청서·도면 등 관련 서류를 확인하셨나요?",
                                [
                                    "선택하세요",
                                    "확인함",
                                    "아직 확인하지 못함",
                                ],
                                key="structure_document_check",
                            )

                            if document_check == "확인함":
                                st.success("🟢 필요한 서류를 확인했습니다. 다음 단계로 진행할 수 있습니다.")
                            elif document_check == "아직 확인하지 못함":
                                st.warning("🟡 공작물 설치에 필요한 신청서·도면 등 관련 서류를 먼저 확인해야 합니다.")

                    if (
                        structure_type != "선택하세요"
                        and permit_check == "허가대상임을 확인함"
                        and location_check == "확인함"
                        and standard_check == "확인함"
                        and document_check == "확인함"
                    ):
                        st.markdown("##### ⑥ 최종 검토 결과")

                        if structure_type == "담장·옹벽" and fence_target == "주택" and fence_height == "예":
                            st.success(
                                "🟢 1차 검토 결과: 주택을 관리하기 위한 높이 2m 미만의 담장은 "
                                "허가 또는 신고 없이 설치할 수 있습니다."
                            )

                        elif (
                            structure_type == "담장·옹벽"
                            and fence_target == "주택이 아닌 허가받은 건축물"
                            and fence_height == "예"
                        ):
                            st.warning(
                                "🟡 1차 검토 결과: 신고 대상입니다. "
                                "허가받은 건축물에 높이 2m 미만의 담장을 추가로 설치하는 경우입니다."
                            )

                        else:
                            st.success(
                                "🟢 1차 검토 완료: 공작물 설치에 필요한 기본 확인사항을 모두 확인했습니다."
                            )

                        st.info(
                            "※ 최종 허가 가능 여부는 관련 법령, 허가기준 및 현장여건 등을 "
                            "종합적으로 확인하여 판단해야 합니다."
                        )

        if structure_type == "철탑·통신탑":
            st.write("📡 철탑·통신탑 관련 허가기준")

            st.info("""
            ✅ 철탑·통신탑 관련 확인사항

            • 개발제한구역 내 허용시설에는 전기통신시설이 포함됩니다.
            • 설치는 개발제한구역의 훼손을 최소화할 수 있도록 최소 규모로 검토합니다.
            • 대기·수질·토질·소음·진동 등 환경오염 또는 생태계 피해가 예상되는지 확인합니다.
            • 역사·문화·향토적 가치가 있는 지역을 훼손하는지 확인합니다.
            • 토지 형질변경이나 벌목이 수반되는 경우 주변 도로·배수 등 현장여건도 확인합니다.

            ⚠️ 철탑·중계탑의 높이·규모·배치 및 구체적인 허가 세부기준은
            관련 법령과 해당 지역의 개발제한구역 관리계획 등을 추가 확인해야 합니다.
            """)

            telecom_type_check = st.radio(
                "설치하려는 시설이 전기통신시설에 해당합니까?",
                [
                    "선택하세요",
                    "예",
                    "아니오",
                    "확인이 필요함",
                ],
                key="telecom_type_check",
            )

            if telecom_type_check == "예":
                st.success(
                    "🟢 전기통신시설에 해당합니다. "
                    "다음 단계에서 설치 규모와 현장여건을 확인하세요."
                )

            telecom_location_check = st.radio(
                "설치 위치와 주변 환경에 특별한 제한사항이 없습니까?",
                [
                    "선택하세요",
                    "예",
                    "아니오",
                    "확인이 필요함",
                ],
                key="telecom_location_check",
            )

            if telecom_location_check == "예":
                st.success(
                    "🟢 설치 위치와 주변 환경에 특별한 제한사항이 없는 것으로 확인했습니다."
                )

            elif telecom_location_check == "아니오":
                st.warning(
                    "🟡 설치 위치 또는 주변 환경에 제한사항이 있을 수 있습니다. "
                    "현장여건과 관련 기준을 추가 확인하세요."
                )

            elif telecom_location_check == "확인이 필요함":
                st.info(
                    "🔵 설치 위치와 주변 환경에 대한 추가 확인이 필요합니다."
                )

            if telecom_type_check == "아니오":
                st.warning("🟡 전기통신시설에 해당하지 않는 경우 다른 공작물 유형 또는 관련 허가기준을 확인하세요.")

        if structure_type == "광고판·광고탑":
            st.write("🪧 광고판·광고탑 관련 허가기준")
            st.info("""
            ✅ 광고판·광고탑 관련 확인사항

            • 광고판·광고탑의 설치 목적과 설치 위치를 확인합니다.
            • 설치하려는 광고물의 종류와 규모를 확인합니다.
            • 개발제한구역 관련 허가기준과 옥외광고물 관련 기준을 함께 확인해야 합니다.
            • 도로·주거지역·주변 경관 등에 미치는 영향도 확인합니다.

            ⚠️ 구체적인 설치 가능 여부와 규모·높이 등의 세부기준은
            관련 법령과 해당 지역의 개발제한구역 관리계획 등을 추가 확인해야 합니다.
            """)        

            ad_location_check = st.radio(
                "광고판·광고탑을 설치하려는 위치가 개발제한구역 안인가요?",
                [
                    "선택하세요",
                    "예",
                    "아니오",
                    "확인이 필요함",
                ],
                key="ad_location_check",
            )

            if ad_location_check == "예":
                st.success(
                    "🟢 개발제한구역 안에 해당합니다. "
                    "다음 단계에서 광고판·광고탑의 설치 목적과 규모를 확인하세요."
                )

            elif ad_location_check == "아니오":
                st.warning(
                    "🟡 개발제한구역 밖이라면 이 업무가이드의 적용 대상이 아닐 수 있습니다. "
                    "해당 지역의 옥외광고물 관련 기준을 확인하세요."
                )

            elif ad_location_check == "확인이 필요함":
                st.info(
                    "🔵 토지이용계획확인서 등을 통해 해당 토지가 "
                    "개발제한구역에 포함되는지 먼저 확인하세요."
                )

            if ad_location_check == "예":
                ad_purpose_check = st.radio(
                    "광고판·광고탑의 설치 목적은 무엇인가요?",
                    [
                        "선택하세요",
                        "공공·공익 목적",
                        "영업·상업 광고 목적",
                        "기타",
                    ],
                    key="ad_purpose_check",
                )

                if ad_purpose_check == "공공·공익 목적":
                    st.success(
                        "🟢 공공·공익 목적의 광고판·광고탑입니다. "
                        "다음 단계에서 설치 규모와 허가기준을 확인하세요."
                    )

                elif ad_purpose_check == "영업·상업 광고 목적":
                    st.warning(
                        "🟡 영업·상업 광고 목적입니다. "
                        "개발제한구역에서 설치 가능한 광고물인지 관련 허가기준을 추가 확인해야 합니다."
                    )

                elif ad_purpose_check == "기타":
                    st.info(
                        "🔵 기타 목적입니다. "
                        "구체적인 설치 목적을 확인한 후 해당 허가기준을 검토하세요."
                    )

                ad_size_check = st.radio(
                    "광고판·광고탑의 설치 규모를 확인했나요?",
                    [
                        "선택하세요",
                        "확인함",
                        "아직 확인하지 못함",
                    ],
                    key="ad_size_check",
                )

                if ad_size_check == "확인함":
                    st.success(
                        "🟢 설치 규모를 확인했습니다. "
                        "다음 단계에서 광고판·광고탑의 높이·면적 등 세부사항을 확인하세요."
                    )

                elif ad_size_check == "아직 확인하지 못함":
                    st.warning(
                        "🟡 광고판·광고탑의 설치 규모를 먼저 확인해야 합니다. "
                        "높이·면적 등 기본 규모를 확인한 후 허가기준을 검토하세요."
                    )

                if ad_size_check == "확인함":
                    ad_install_type = st.radio(
                        "광고판·광고탑의 설치 형태를 선택하세요.",
                        [
                            "선택하세요",
                            "지주를 이용하여 지면에 설치",
                            "건물·시설물에 부착하여 설치",
                            "옥상에 설치",
                            "기타",
                        ],
                        key="ad_install_type",
                    )                    
                    ad_height = st.number_input(
                        "광고판·광고탑의 높이(m)를 입력하세요.",
                        min_value=0.0,
                        step=0.1,
                        key="ad_height",
                    )

                    ad_area = st.number_input(
                        "광고판·광고탑의 표시 면적(㎡)을 입력하세요.",
                        min_value=0.0,
                        step=0.1,
                        key="ad_area",
                    )

                    st.info(
                        f"📏 입력한 규모: 높이 {ad_height:.1f}m / "
                        f"표시 면적 {ad_area:.1f}㎡"
                    )

                    if ad_height > 0 and ad_area > 0:
                        if ad_height > 4.0:
                            st.warning(
                                "🟡 광고판·광고탑의 높이가 4m를 초과합니다. "
                                "옥외광고물법상 안전점검 대상에 해당하므로 추가 확인이 필요합니다."
                            )
                        else:
                            st.success(
                                "🟢 높이가 4m 이하입니다. "
                                "다음 단계에서 표시 면적과 광고물 관련 기준을 추가로 확인합니다."
                            )

                if "ad_install_type" in locals() and ad_install_type != "선택하세요":
                    st.info(
                        "🟡 표시 면적은 광고물의 설치 형태와 해당 지역의 옥외광고물 조례에 따라 "
                        "적용 기준이 달라질 수 있으므로 추가 확인이 필요합니다."
                    )

        if structure_type == "태양광 관련 구조물":
            st.write("☀️ 태양광 관련 구조물 허가기준")

            st.info("""
    ✅ 태양광 관련 구조물 확인사항

    • 태양광 설비의 설치 목적과 설치 위치를 확인합니다.
    • 토지 위에 설치하는지, 기존 건축물 위에 설치하는지 확인합니다.
    • 구조물의 높이·면적·규모를 확인합니다.
    • 개발제한구역 관련 허가기준과 다른 관계 법령 적용 여부를 함께 확인합니다.
    • 주변 경관·도로·인접 토지 등에 미치는 영향도 확인합니다.

    ⚠️ 구체적인 허가 가능 여부는 설치 형태, 규모, 토지 현황 및 관계 법령을 종합하여 확인해야 합니다.
            """)

            solar_install_type = st.radio(
                "태양광 관련 구조물을 어디에 설치하려고 합니까?",
                [
                    "선택하세요",
                    "토지 위에 설치",
                    "기존 건축물 위에 설치",
                    "기타",
                    "확인이 필요함",
                ],
                key="solar_install_type",
            )

            if solar_install_type == "토지 위에 설치":
                st.warning(
                    "🟡 토지 위에 설치하는 경우 토지 형질변경 여부, 구조물 규모 및 "
                    "개발제한구역 허가기준을 추가로 확인해야 합니다."
                )

            elif solar_install_type == "기존 건축물 위에 설치":
                st.success(
                    "🟢 기존 건축물 위에 설치하는 형태입니다. "
                    "건축물의 적법 여부와 구조안전, 관련 허가기준을 추가 확인하세요."
                )

            elif solar_install_type == "기타":
                st.warning(
                    "🟡 설치 형태가 일반적인 유형과 다릅니다. "
                    "구체적인 설치 방법과 관계 법령을 추가 확인하세요."
                )

            elif solar_install_type == "확인이 필요함":
                st.info(
                    "🔵 태양광 구조물의 설치 위치와 형태를 먼저 확인해야 합니다."
                )

        if structure_type == "저장조·탱크":
            st.write("🛢️ 저장조·탱크 관련 허가기준")

            st.info("""
    ✅ 저장조·탱크 관련 확인사항

    • 저장조·탱크의 설치 목적과 용도를 확인합니다.
    • 저장하는 물질의 종류와 저장 용량을 확인합니다.
    • 설치에 따른 토지 형질변경 여부를 확인합니다.
    • 주변 토지, 도로 및 배수시설 등에 미치는 영향을 확인합니다.
    • 위험물·유류·가스 등을 저장하는 경우 관계 법령에 따른 별도 허가 여부를 확인합니다.

    ⚠️ 구체적인 허용 여부와 규모는 관련 법령 및 현장여건을 추가로 확인해야 합니다.
    """)

            tank_use_type = st.radio(
                "저장조·탱크의 주된 용도는 무엇입니까?",
                [
                    "선택하세요",
                    "농업용",
                    "상·하수도 관련",
                    "연료·가스 등 저장",
                    "기타",
                    "확인이 필요함",
                ],
                key="tank_use_type",
            )

            if tank_use_type == "농업용":
                st.success(
                    "🟢 농업용 저장시설입니다. "
                    "농업 관련 허용시설에 부수되는 시설인지 추가 확인하세요."
                )

            elif tank_use_type == "상·하수도 관련":
                st.success(
                    "🟢 상·하수도 관련 시설입니다. "
                    "공공시설 또는 허용시설과의 관련성을 추가 확인하세요."
                )

            elif tank_use_type == "연료·가스 등 저장":
                st.warning(
                    "🟡 연료·가스 등을 저장하는 시설입니다. "
                    "위험물 관련 법령과 별도 허가 여부를 추가 확인하세요."
                )

            elif tank_use_type == "기타":
                st.warning(
                    "🟡 일반적인 저장조·탱크 유형과 다릅니다. "
                    "설치 목적과 관계 법령을 추가 확인하세요."
                )

            elif tank_use_type == "확인이 필요함":
                st.info(
                    "🔵 저장 물질과 설치 목적을 먼저 확인해야 합니다."
                )

        if structure_type == "컨테이너·기타 구조물":
            st.write("📦 컨테이너·기타 구조물 관련 허가기준")

            st.info("""
    ✅ 컨테이너·기타 구조물 관련 확인사항

    • 설치 목적과 실제 사용 용도를 확인합니다.
    • 단순 보관용인지, 작업·사무·주거 등 다른 용도로 사용하는지 확인합니다.
    • 기초 설치 여부와 토지 형질변경 수반 여부를 확인합니다.
    • 설치 면적·높이·수량 등 구조물 규모를 확인합니다.
    • 장기간 고정 설치되는 경우 건축물 또는 공작물 해당 여부도 함께 확인합니다.

    ⚠️ 컨테이너의 형태만으로 허용 여부를 판단하지 말고,
    실제 사용 목적과 설치 상태를 기준으로 관계 법령을 추가 확인해야 합니다.
    """)

            container_use_type = st.radio(
                "컨테이너·기타 구조물의 주된 용도는 무엇입니까?",
                [
                    "선택하세요",
                    "물품·농기구 등 보관",
                    "작업·사무용",
                    "주거·숙박용",
                    "기타",
                    "확인이 필요함",
                ],
                key="container_use_type",
            )

            if container_use_type == "물품·농기구 등 보관":
                st.success(
                    "🟢 보관 용도의 구조물입니다. "
                    "허용시설에 부수되는 시설인지와 설치 규모를 추가 확인하세요."
                )

            elif container_use_type == "작업·사무용":
                st.warning(
                    "🟡 작업·사무 용도로 사용하는 구조물입니다. "
                    "건축물 해당 여부와 관계 허가기준을 추가 확인하세요."
                )

            elif container_use_type == "주거·숙박용":
                st.error(
                    "🔴 주거·숙박 용도 사용 가능성이 있습니다. "
                    "무단 용도변경 또는 불법 건축물 해당 여부를 중점 확인하세요."
                )

            elif container_use_type == "기타":
                st.warning(
                    "🟡 일반적인 유형과 다른 구조물입니다. "
                    "실제 설치 목적과 이용 상태를 추가 확인하세요."
                )

            elif container_use_type == "확인이 필요함":
                st.info(
                    "🔵 구조물의 실제 사용 목적과 설치 형태를 먼저 확인해야 합니다."
                )

        if structure_type == "기타 공작물":
            st.write("🧱 기타 공작물 관련 허가기준")

            st.info("""
    ✅ 기타 공작물 관련 확인사항

    • 설치하려는 시설의 명칭과 실제 용도를 먼저 확인합니다.
    • 공작물의 높이·면적·길이·수량 등 규모를 확인합니다.
    • 기초 설치 여부와 토지 형질변경 수반 여부를 확인합니다.
    • 건축물, 가설건축물 또는 다른 공작물 유형에 해당하는지 함께 검토합니다.
    • 주변 도로·배수·안전 및 인접 토지에 미치는 영향을 확인합니다.

    ⚠️ 기타 공작물은 유형이 다양하므로,
    시설의 실제 구조와 용도를 기준으로 관계 법령과 허가기준을 추가 확인해야 합니다.
    """)

            other_structure_type = st.radio(
                "설치하려는 기타 공작물의 상태를 선택하세요.",
                [
                    "선택하세요",
                    "용도와 구조를 확인함",
                    "다른 공작물 유형에 해당할 가능성 있음",
                    "현장 확인이 필요함",
                ],
                key="other_structure_type",
            )

            if other_structure_type == "용도와 구조를 확인함":
                st.success(
                    "🟢 공작물의 용도와 구조를 확인했습니다. "
                    "관련 허가기준과 설치 규모를 최종 확인하세요."
                )

            elif other_structure_type == "다른 공작물 유형에 해당할 가능성 있음":
                st.warning(
                    "🟡 다른 공작물 유형에 해당할 수 있습니다. "
                    "광고판·철탑·저장조·컨테이너 등 기존 유형과 다시 비교해 보세요."
                )

            elif other_structure_type == "현장 확인이 필요함":
                st.info(
                    "🔵 시설의 실제 구조와 사용 상태를 현장에서 먼저 확인해야 합니다."
                )
# ============================================
# 토지 형질변경 상세화면
# ============================================
if (
    "업무가이드" in menu
    and "토지 형질변경" in st.session_state.get("permit_type", "")
):
    st.markdown("### 🌱 토지 형질변경")

    st.info(
        "토지 형질변경의 허가 가능 여부와 관련 기준을 단계별로 확인합니다."
    )

    st.markdown("#### ① 형질변경 내용 확인")

    land_change_type = st.selectbox(
        "토지 형질변경의 종류를 선택하세요.",
        [
            "선택하세요",
            "절토",
            "성토",
            "정지",
            "포장",
            "기타",
        ],
        key="land_change_type",
    )

    if land_change_type != "선택하세요":
        st.success(f"선택한 형질변경 유형: {land_change_type}")

    st.markdown("#### ② 형질변경 규모 확인")

    land_change_area = st.number_input(
        "형질변경하려는 토지 면적(㎡)을 입력하세요.",
        min_value=0.0,
        step=1.0,
        key="land_change_area",
    )

    land_change_height = st.number_input(
        "절토·성토의 최대 높이 또는 깊이(m)를 입력하세요.",
        min_value=0.0,
        step=0.1,
        key="land_change_height",
    )

    st.markdown("#### ③ 관련 허가기준 확인")

    st.info(
        "토지 형질변경은 형질변경의 목적·면적·절토·성토 규모와 "
        "주변 토지 및 환경에 미치는 영향 등을 종합적으로 확인해야 합니다."
    )

    land_standard_check = st.radio(
        "관련 허가기준을 확인했나요?",
        [
            "선택하세요",
            "예",
            "아니오",
            "추가 확인 필요",
        ],
        key="land_standard_check",
    )

    st.markdown("#### ④ 검토결과")

    if land_change_type == "선택하세요":
        st.info("🔵 먼저 토지 형질변경의 종류를 선택하세요.")

    elif land_change_area <= 0:
        st.warning("🟡 형질변경하려는 토지 면적을 입력하세요.")

    elif land_standard_check == "선택하세요":
        st.warning("🟡 관련 허가기준 확인 여부를 선택하세요.")

    elif land_standard_check == "예":
        st.success(
            "🟢 1차 검토 완료: 토지 형질변경 허가기준 검토를 진행할 수 있습니다. "
            "최종 허가 여부는 관계 법령, 세부 허가기준 및 현장여건을 함께 확인해야 합니다."
        )

    elif land_standard_check == "아니오":
        st.error(
            "🔴 관련 허가기준을 먼저 확인해야 합니다."
        )

    else:
        st.warning(
            "🟡 추가 확인이 필요합니다. 관계 법령, 허가기준 및 현장여건을 확인하세요."
        )

# ============================================
# 토석 채취 상세화면
# ============================================
if (
    "업무가이드" in menu
    and "토석 채취" in st.session_state.get("permit_type", "")
):
    st.markdown("### ⛏️ 토석 채취")

    st.info(
        "토석 채취의 허가 가능 여부와 관련 기준을 단계별로 확인합니다."
    )

    st.markdown("#### ① 채취 내용 확인")

    stone_type = st.selectbox(
        "채취하려는 토석의 종류를 선택하세요.",
        [
            "선택하세요",
            "토사",
            "모래·자갈",
            "암석",
            "기타",
        ],
        key="stone_type",
    )

    if stone_type != "선택하세요":
        st.success(f"선택한 토석 종류: {stone_type}")

    st.markdown("#### ② 채취 규모 확인")

    stone_area = st.number_input(
        "토석을 채취하려는 면적(㎡)을 입력하세요.",
        min_value=0.0,
        step=1.0,
        key="stone_area",
    )

    stone_volume = st.number_input(
        "채취하려는 토석의 양(㎥)을 입력하세요.",
        min_value=0.0,
        step=1.0,
        key="stone_volume",
    )

    st.markdown("#### ③ 관련 허가기준 확인")

    st.info(
        "토석 채취는 채취 목적·위치·면적·채취량과 "
        "주변 토지 및 환경에 미치는 영향 등을 종합적으로 확인해야 합니다."
    )

    stone_standard_check = st.radio(
        "관련 허가기준을 확인했나요?",
        [
            "선택하세요",
            "예",
            "아니오",
            "추가 확인 필요",
        ],
        key="stone_standard_check",
    )

    st.markdown("#### ④ 검토결과")

    if stone_type == "선택하세요":
        st.info("🔵 먼저 채취하려는 토석의 종류를 선택하세요.")

    elif stone_area <= 0:
        st.warning("🟡 토석을 채취하려는 면적을 입력하세요.")

    elif stone_volume <= 0:
        st.warning("🟡 채취하려는 토석의 양을 입력하세요.")

    elif stone_standard_check == "선택하세요":
        st.warning("🟡 관련 허가기준 확인 여부를 선택하세요.")

    elif stone_standard_check == "예":
        st.success(
            "🟢 1차 검토 완료: 토석 채취 허가기준 검토를 진행할 수 있습니다. "
            "최종 허가 여부는 관계 법령, 세부 허가기준 및 현장여건을 함께 확인해야 합니다."
        )

    elif stone_standard_check == "아니오":
        st.error(
            "🔴 관련 허가기준을 먼저 확인해야 합니다."
        )

    else:
        st.warning(
            "🟡 추가 확인이 필요합니다. 관계 법령, 허가기준 및 현장여건을 확인하세요."
        )

# ============================================
# 죽목 벌채 상세화면
# ============================================
if (
    "업무가이드" in menu
    and "죽목 벌채" in st.session_state.get("permit_type", "")
):
    st.markdown("### 🌳 죽목 벌채")

    st.info(
        "죽목 벌채의 허가 가능 여부와 관련 기준을 단계별로 확인합니다."
    )

    st.markdown("#### ① 벌채 내용 확인")

    tree_cut_type = st.selectbox(
        "벌채하려는 죽목의 유형을 선택하세요.",
        [
            "선택하세요",
            "입목 벌채",
            "대나무 벌채",
            "고사목·위험목 제거",
            "기타",
        ],
        key="tree_cut_type",
    )

    if tree_cut_type != "선택하세요":
        st.success(f"선택한 벌채 유형: {tree_cut_type}")

    st.markdown("#### ② 벌채 규모 확인")

    tree_cut_area = st.number_input(
        "벌채하려는 면적(㎡)을 입력하세요.",
        min_value=0.0,
        step=1.0,
        key="tree_cut_area",
    )

    tree_cut_count = st.number_input(
        "벌채하려는 수량(본)을 입력하세요.",
        min_value=0,
        step=1,
        key="tree_cut_count",
    )

    st.markdown("#### ③ 관련 허가기준 확인")

    st.info(
        "죽목 벌채는 벌채 목적·위치·면적·수량과 "
        "주변 산림 및 환경에 미치는 영향 등을 종합적으로 확인해야 합니다."
    )

    tree_standard_check = st.radio(
        "관련 허가기준을 확인했나요?",
        [
            "선택하세요",
            "예",
            "아니오",
            "추가 확인 필요",
        ],
        key="tree_standard_check",
    )

    st.markdown("#### ④ 검토결과")

    if tree_cut_type == "선택하세요":
        st.info("🔵 먼저 벌채하려는 죽목의 유형을 선택하세요.")

    elif tree_cut_area <= 0:
        st.warning("🟡 벌채하려는 면적을 입력하세요.")

    elif tree_cut_count <= 0:
        st.warning("🟡 벌채하려는 수량을 입력하세요.")

    elif tree_standard_check == "선택하세요":
        st.warning("🟡 관련 허가기준 확인 여부를 선택하세요.")

    elif tree_standard_check == "예":
        st.success(
            "🟢 1차 검토 완료: 죽목 벌채 허가기준 검토를 진행할 수 있습니다. "
            "최종 허가 여부는 관계 법령, 세부 허가기준 및 현장여건을 함께 확인해야 합니다."
        )

    elif tree_standard_check == "아니오":
        st.error(
            "🔴 관련 허가기준을 먼저 확인해야 합니다."
        )

    else:
        st.warning(
            "🟡 추가 확인이 필요합니다. 관계 법령, 허가기준 및 현장여건을 확인하세요."
        )

# ============================================
# 토지 분할 상세화면
# ============================================
if (
    "업무가이드" in menu
    and "토지 분할" in st.session_state.get("permit_type", "")
):
    st.markdown("### 📐 토지 분할")

    st.info(
        "토지 분할의 허가 가능 여부와 관련 기준을 단계별로 확인합니다."
    )

    st.markdown("#### ① 분할 내용 확인")

    land_split_type = st.selectbox(
        "토지 분할의 목적을 선택하세요.",
        [
            "선택하세요",
            "소유권 정리",
            "건축 또는 이용 목적",
            "도로·공공시설 관련",
            "기타",
        ],
        key="land_split_type",
    )

    if land_split_type != "선택하세요":
        st.success(f"선택한 분할 목적: {land_split_type}")

    st.markdown("#### ② 분할 규모 확인")

    land_split_area = st.number_input(
        "분할하려는 토지의 전체 면적(㎡)을 입력하세요.",
        min_value=0.0,
        step=1.0,
        key="land_split_area",
    )

    land_split_count = st.number_input(
        "분할 후 필지 수를 입력하세요.",
        min_value=1,
        step=1,
        key="land_split_count",
    )

    st.markdown("#### ③ 관련 허가기준 확인")

    st.info(
        "토지 분할은 분할 목적·분할 면적·분할 후 필지 수와 "
        "분할 후 토지의 이용계획 등을 종합적으로 확인해야 합니다."
    )

    land_split_standard_check = st.radio(
        "관련 허가기준을 확인했나요?",
        [
            "선택하세요",
            "예",
            "아니오",
            "추가 확인 필요",
        ],
        key="land_split_standard_check",
    )

    st.markdown("#### ④ 검토결과")

    if land_split_type == "선택하세요":
        st.info("🔵 먼저 토지 분할의 목적을 선택하세요.")

    elif land_split_area <= 0:
        st.warning("🟡 분할하려는 토지의 전체 면적을 입력하세요.")

    elif land_split_standard_check == "선택하세요":
        st.warning("🟡 관련 허가기준 확인 여부를 선택하세요.")

    elif land_split_standard_check == "예":
        st.success(
            "🟢 1차 검토 완료: 토지 분할 허가기준 검토를 진행할 수 있습니다. "
            "최종 허가 여부는 관계 법령, 세부 허가기준 및 현장여건을 함께 확인해야 합니다."
        )

    elif land_split_standard_check == "아니오":
        st.error(
            "🔴 관련 허가기준을 먼저 확인해야 합니다."
        )

    else:
        st.warning(
            "🟡 추가 확인이 필요합니다. 관계 법령, 허가기준 및 현장여건을 확인하세요."
        )

# ============================================
# 물건 적치 상세화면
# ============================================
if (
    "업무가이드" in menu
    and "물건 적치" in st.session_state.get("permit_type", "")
):
    st.markdown("### 📦 물건 적치")

    st.info(
        "물건 적치의 허가 가능 여부와 관련 기준을 단계별로 확인합니다."
    )

    st.markdown("#### ① 적치 내용 확인")

    storage_type = st.selectbox(
        "적치하려는 물건의 종류를 선택하세요.",
        [
            "선택하세요",
            "건축자재",
            "토사·골재",
            "농림수산업 관련 물품",
            "기계·장비",
            "기타",
        ],
        key="storage_type",
    )

    if storage_type != "선택하세요":
        st.success(f"선택한 적치 물건: {storage_type}")
        
    # ==================================================
    # 2. 행위신고
    # ==================================================
    
if "업무가이드" in menu and guide_type == "📋 행위신고":

    st.subheader("📋 행위신고")

    st.info(
        "신고 대상 행위인지 확인한 뒤 관련 기준과 필요서류를 단계별로 확인합니다."
    )

    report_check = st.radio(
        "① 신고 대상 여부를 확인하셨나요?",
        [
            "선택하세요",
            "신고 대상임을 확인함",
            "신고 대상이 아님",
            "확인이 필요함",
        ],
        key="report_check",
    )

    if report_check == "신고 대상임을 확인함":
        st.success(
            "🟢 신고 대상임을 확인했습니다. 다음 단계로 진행할 수 있습니다."
        )

        report_standard = st.radio(
            "② 관련 신고기준을 확인하셨나요?",
            [
                "선택하세요",
                "확인함",
                "아직 확인하지 못함",
            ],
            key="report_standard",
        )

        if report_standard == "확인함":
            st.success(
                "🟢 관련 신고기준을 확인했습니다."
            )

            st.markdown("### ③ 필요서류 확인")
            st.info(
                "📄 신고하려는 행위의 종류와 규모에 따라 필요한 서류를 확인하세요."
            )

        elif report_standard == "아직 확인하지 못함":
            st.warning(
                "🟡 관련 신고기준을 먼저 확인해야 합니다."
            )

    elif report_check == "신고 대상이 아님":
        st.info(
            "🔵 신고 대상이 아닌 것으로 확인했습니다. "
            "허가 대상 또는 허가·신고 없이 가능한 행위인지 추가 확인하세요."
        )

    elif report_check == "확인이 필요함":
        st.warning(
            "🟡 신고 대상 여부를 먼저 확인해야 합니다."
        )

elif "업무가이드" in menu and guide_type == "✅ 허가·신고 없이 가능한 행위":

    st.subheader("✅ 허가·신고 없이 가능한 행위")

    st.info(
        "허가 또는 신고 없이 가능한 행위인지 단계별로 확인합니다."
    )

    free_action_type = st.radio(
        "① 확인하려는 행위 유형을 선택하세요.",
[
    "선택하세요",
    "농림수산업을 하기 위한 행위",
    "주택을 관리하는 행위",
    "마을공동사업",
    "비주택용 건축물에 관련된 행위",
    "건축물의 용도변경",
    "기존 골프장의 통상적인 운영·관리 행위",
    "재해의 긴급한 복구",
    "기존 건축물의 적법한 대지 안에 물건을 쌓아 놓는 행위",
    "국유림·공유림 또는 자연공원 등의 관리 행위",
],
        key="free_action_type",
    )

    if free_action_type == "농림수산업을 하기 위한 행위":

        farm_action = st.selectbox(
            "② 세부 행위를 선택하세요.",
            [
                "선택하세요",
                "논·밭을 갈거나 50cm 이하로 파는 행위",
                "홍수 등으로 논·밭에 쌓인 흙·모래를 제거하는 행위",
                "경작 중인 논·밭에 환토·객토를 하는 행위",
                "밭을 논으로 변경하는 토지의 형질변경",
                "과수원을 논이나 밭으로 변경하는 토지의 형질변경",
                "농경지 땅고르기·수로 정비",
                "농업용 비닐하우스 설치",
                "농업용 분뇨장 설치",
                "과수원·경제작물 보호용 철조망 설치",
                "10㎡ 이하 농업용 원두막 설치",
                "밭 안에 농산물 저장용 토굴 등을 파는 행위",
                "나무를 베지 않고 나무를 심는 행위",
                "축사에 사료배합 기계시설 설치",
                "기존 대지 안에 15㎡ 이하 간이축사 설치",
                            "분뇨장에 취사·난방용 메탄가스 발생시설 설치",
                "33㎡ 이하 화분진열시설 설치",
                "30㎡ 이하 비닐하우스 부속 임시시설 설치",
                "축사에 딸린 가축방목장 설치",
                "영농 목적 50cm 미만 성토",
                "50㎡ 이하 곡식건조기 또는 비가림시설 설치",
                "축사운동장 개방형 비닐하우스 설치",
                "논에서 참게·우렁이·지렁이 등 사육",
                "30㎡ 이하 판매용 야외 좌판 설치",
                "저수지 관리 목적 단순 준설",
                "영농용 지하수 개발·이용시설 설치",
                "토지형질변경 없이 양봉통 설치",
            ],
            key="farm_action"
        )

        farm_action_info = {
            "논·밭을 갈거나 50cm 이하로 파는 행위":
                "농사를 짓기 위하여 논·밭을 갈거나 깊이 50cm 이하로 파는 행위입니다.",

            "홍수 등으로 논·밭에 쌓인 흙·모래를 제거하는 행위":
                "홍수 등으로 논·밭에 쌓인 흙·모래를 제거하는 행위입니다.",

            "경작 중인 논·밭에 환토·객토를 하는 행위":
                "경작 중인 논·밭의 지력을 높이기 위한 환토·객토입니다. 영리 목적의 토사 채취는 제외됩니다.",

            "밭을 논으로 변경하는 토지의 형질변경":
                "밭을 논으로 변경하기 위한 토지의 형질변경입니다.",

            "과수원을 논이나 밭으로 변경하는 토지의 형질변경":
                "과수원을 논이나 밭으로 변경하기 위한 토지의 형질변경입니다.",

            "농경지 땅고르기·수로 정비":
                "농업생산성 증대를 목적으로 농경지를 정지하거나 수로 등을 정비하는 행위입니다.",

            "농업용 비닐하우스 설치":
                "채소·연초·버섯 재배 및 원예용 농업용 비닐하우스입니다. 골조·재료·기초·바닥 등 별표 4의 요건을 모두 충족해야 합니다.",

            "농업용 분뇨장 설치":
                "농업용 분뇨장을 설치하는 행위이며 탱크 설치도 포함됩니다.",

            "과수원·경제작물 보호용 철조망 설치":
                "과수원이나 경제작물을 보호하기 위한 철조망 또는 녹색·연두색 등의 울타리 설치입니다.",

            "10㎡ 이하 농업용 원두막 설치":
                "면적 10㎡ 이하의 농업용 원두막 설치입니다.",

            "밭 안에 농산물 저장용 토굴 등을 파는 행위":
                "밭 안에 야채 등을 저장하기 위하여 토굴 등을 파는 행위입니다.",

            "나무를 베지 않고 나무를 심는 행위":
                "기존 나무를 베지 않고 나무를 심는 행위입니다.",

            "축사에 사료배합 기계시설 설치":
                "축사에 사료배합용 기계시설을 설치하는 행위입니다. 일반인에게 배합사료를 판매하는 경우는 제외됩니다.",

            "기존 대지 안에 15㎡ 이하 간이축사 설치":
                "담장으로 둘러싸인 기존 대지 안에 15㎡ 이하의 간이축사를 설치하는 행위입니다.",
                        "분뇨장에 취사·난방용 메탄가스 발생시설 설치":
                "분뇨장에 취사 또는 난방용 메탄가스 발생시설을 설치하는 행위입니다.",

            "33㎡ 이하 화분진열시설 설치":
                "33㎡ 이하의 화분진열시설을 설치하는 행위입니다. 벽체가 없는 구조 등 세부 요건을 충족해야 합니다.",

            "30㎡ 이하 비닐하우스 부속 임시시설 설치":
                "비닐하우스 안에 30㎡ 이하의 탈의실·농기구보관실·기계실·냉장시설 등 임시시설을 설치하는 행위입니다.",

            "축사에 딸린 가축방목장 설치":
                "축사에 딸린 가축방목장을 설치하는 행위입니다. 토지의 형질변경이나 지목변경을 수반하지 않아야 합니다.",

            "영농 목적 50cm 미만 성토":
                "영농을 목적으로 하는 성토로서 최근 1년간 합산 높이가 50cm 미만인 경우입니다.",

            "50㎡ 이하 곡식건조기 또는 비가림시설 설치":
                "50㎡ 이하의 곡식건조기 또는 비가림시설을 설치하는 행위입니다.",

            "축사운동장 개방형 비닐하우스 설치":
                "축사운동장에 개방형 비닐하우스를 설치하는 행위입니다.",

            "논에서 참게·우렁이·지렁이 등 사육":
                "논 등에서 참게·우렁이·지렁이 등을 농업적으로 사육하는 행위입니다.",

            "30㎡ 이하 판매용 야외 좌판 설치":
                "30㎡ 이하의 판매용 야외 좌판을 설치하는 행위입니다. 별표 4의 설치요건을 충족해야 합니다.",

            "저수지 관리 목적 단순 준설":
                "저수지의 유지·관리 등을 위한 단순 준설 행위입니다.",

            "영농용 지하수 개발·이용시설 설치":
                "영농을 위한 지하수 개발·이용시설을 설치하는 행위입니다.",

            "토지형질변경 없이 양봉통 설치":
                "토지의 형질변경 없이 양봉통을 설치하는 행위입니다. 별도의 그늘막 등 공작물 설치 여부는 별도 확인이 필요합니다.",
        }

        if farm_action != "선택하세요":
            if farm_action in farm_action_info:
                st.success(
                    "✅ 허가·신고 없이 가능한 행위입니다.\n\n"
                    + farm_action_info[farm_action]
                )

                st.caption(
                    "※ 시행규칙 별표 4의 세부 요건을 충족하는 경우에 한합니다. "
                    "규모·재료·설치방법·토지형질변경 등이 기준을 벗어나면 "
                    "허가 또는 신고 대상 여부를 다시 확인해야 합니다."
                )

    elif free_action_type == "주택을 관리하는 행위":

        house_action = st.selectbox(
            "② 세부 행위를 선택하세요.",
            [
                "선택하세요",
                "가옥 내부 개조·수리",
                "지붕 개량 또는 기둥·벽 수선",
                "외장 변경·도색·장식",
                "내벽 또는 외벽에 창문 설치",
                "외벽 기둥에 차양 설치·수리",
                "외벽과 담장 사이에 차양을 달아 헛간으로 사용",
                "높이 2m 미만 담장·축대 설치",
                "우물 또는 장독대 설치",
                "재래식 변소를 수세식 변소로 개량",
            ],
            key="house_action"
        )

        house_action_info = {
            "가옥 내부 개조·수리":
                "사용 중인 방을 나누거나 합치거나 부엌·목욕탕으로 바꾸는 등 가옥 내부를 개조하거나 수리하는 행위입니다.",

            "지붕 개량 또는 기둥·벽 수선":
                "지붕을 개량하거나 기둥·벽을 수선하는 행위입니다.",

            "외장 변경·도색·장식":
                "주택의 외장을 변경하거나 칠하거나 꾸미는 행위입니다.",

            "내벽 또는 외벽에 창문 설치":
                "내벽 또는 외벽에 창문을 설치하는 행위입니다.",

            "외벽 기둥에 차양 설치·수리":
                "외벽 기둥에 차양을 달거나 기존 차양을 수리하는 행위입니다.",

            "외벽과 담장 사이에 차양을 달아 헛간으로 사용":
                "외벽과 담장 사이에 차양을 달아 헛간으로 사용하는 행위입니다.",

            "높이 2m 미만 담장·축대 설치":
                "높이 2미터 미만의 담장 또는 축대(옹벽 포함)를 설치하는 행위입니다. 다만 택지 조성을 위한 경우는 제외됩니다.",

            "우물 또는 장독대 설치":
                "우물을 파거나 장독대를 설치하는 행위입니다. 광을 함께 설치하는 경우는 제외됩니다.",

            "재래식 변소를 수세식 변소로 개량":
                "재래식 변소를 수세식 변소로 개량하는 행위입니다.",
        }

        if house_action != "선택하세요":
            st.success(
                "✅ 허가·신고 없이 가능한 행위입니다.\n\n"
                + house_action_info[house_action]
            )

            st.caption(
                "※ 개발제한구역법 시행규칙 별표 4의 해당 요건을 충족하는 경우에 한합니다."
            )

    elif free_action_type == "마을공동사업":

        village_action = st.selectbox(
            "② 세부 행위를 선택하세요.",
            [
                "선택하세요",
                "공동우물 또는 빨래터 설치",
                "마을도로·구거 정비 또는 석축 개수·보수",
                "농로 개수·보수",
                "나지 녹화사업",
                "토관 매설",
            ],
            key="village_action"
        )

        village_action_info = {
            "공동우물 또는 빨래터 설치":
                "공동우물을 파거나 빨래터를 설치하는 행위입니다. 공동우물에는 「지하수법」에 따른 먹는물용 지하수가 포함됩니다.",

            "마을도로·구거 정비 또는 석축 개수·보수":
                "마을도로(진입로 포함) 및 구거를 정비하거나 석축을 개수·보수하는 행위입니다.",

            "농로 개수·보수":
                "기존 농로를 개수하거나 보수하는 행위입니다.",

            "나지 녹화사업":
                "나지에 녹화사업을 하는 행위입니다.",

            "토관 매설":
                "마을공동사업으로 토관을 매설하는 행위입니다.",
        }

        if village_action != "선택하세요":
            st.success(
                "✅ 허가·신고 없이 가능한 행위입니다.\n\n"
                + village_action_info[village_action]
            )

            st.caption(
                "※ 개발제한구역법 시행규칙 별표 4의 마을공동사업에 해당하는 경우에 한합니다."
            )

    elif free_action_type == "비주택용 건축물에 관련된 행위":

        nonhouse_action = st.selectbox(
            "② 세부 행위를 선택하세요.",
            [
                "선택하세요",
                "지붕 개량·벽 수선·미화작업 또는 창문 설치",
                "기존 종교시설 경내에 종각·불상·석탑·예수상 또는 기념비석 설치",
                "기존 묘역 안에 분묘 설치",
                "종교시설 경내에 일주문 설치",
                "임업시험장 내 육림 연구·시험을 위한 임목 식재 또는 벌채",
            ],
            key="nonhouse_action"
        )

        nonhouse_action_info = {
            "지붕 개량·벽 수선·미화작업 또는 창문 설치":
                "비주택용 건축물에 대하여 주택의 경우와 같이 지붕을 개량하거나 벽을 수선하고, 미화작업 또는 창문을 설치하는 행위입니다.",

            "기존 종교시설 경내에 종각·불상·석탑·예수상 또는 기념비석 설치":
                "기존 종교시설의 경내(공지)에 종각·불상·석탑·예수상 또는 기념비석을 설치하는 행위입니다.",

            "기존 묘역 안에 분묘 설치":
                "기존의 묘역 안에 분묘를 설치하는 행위입니다.",

            "종교시설 경내에 일주문 설치":
                "종교시설의 경내에 일주문을 설치하는 행위입니다.",

            "임업시험장 내 육림 연구·시험을 위한 임목 식재 또는 벌채":
                "임업시험장 안에서 육림 연구·시험을 위하여 임목을 식재하거나 벌채하는 행위입니다.",
        }

        if nonhouse_action != "선택하세요":
            st.success(
                "✅ 허가·신고 없이 가능한 행위입니다.\n\n"
                + nonhouse_action_info[nonhouse_action]
            )

            st.caption(
                "※ 개발제한구역법 시행규칙 별표 4의 해당 요건을 충족하는 경우에 한합니다."
            )

    elif free_action_type == "건축물의 용도변경":

        use_change_action = st.selectbox(
            "② 세부 행위를 선택하세요.",
    [
        "선택하세요",
        "기존 축사·잠실 등을 저장소 또는 농가부업 작업장으로 일시 사용",
        "주택 일부를 부업 범위의 상점 등으로 사용",
        "주택의 일부 부속건축물을 다용도시설·농산물건조실로 사용",
        "새마을회관 일부를 경로당으로 사용",
    ],
            key="use_change_action"
        )

        use_change_info = {
            "기존 축사·잠실 등을 저장소 또는 농가부업 작업장으로 일시 사용":
                "축사·잠실 등의 기존 건축물을 일상 생업에 필요한 물품·생산물의 저장소나 새끼·가마니 등을 만드는 농가부업용 작업장으로 일시적으로 사용하는 경우입니다.",

            "주택 일부를 부업 범위의 상점 등으로 사용":
                "주택의 일부를 부업의 범위에서 상점 등으로 사용하는 경우입니다. 관계 법령에 따른 허가 또는 신고 대상이 아닌 경우만 해당합니다.",

            "주택의 일부 부속건축물을 다용도시설·농산물건조실로 사용":
                "주택의 일부인 종전 부속건축물을 다용도시설 또는 농산물건조실로 사용하는 경우입니다. 건조를 위한 공작물 설치도 포함됩니다.",

            "새마을회관 일부를 경로당으로 사용":
                "새마을회관의 일부를 경로당으로 사용하는 경우입니다.",
        }

        if use_change_action != "선택하세요":
            st.success(
                "✅ 허가·신고 없이 가능한 용도변경입니다.\n\n"
                + use_change_info[use_change_action]
            )

            st.caption(
                "※ 개발제한구역법 시행규칙 별표 4 제5호의 요건을 충족하는 경우에 한합니다."
            )

    elif free_action_type == "기존 골프장의 통상적인 운영·관리 행위":

        golf_action = st.selectbox(
            "② 세부 행위를 선택하세요.",
            [
                "선택하세요",
                "차량정비고·부품보관창고 부지 바닥 포장",
                "잔디 배토용 부엽토·토사를 일시적으로 쌓아 놓는 행위",
                "골프장 배수로 정비",
                "잔디를 심고 가꾸는 행위",
                "티 그라운드 모양·크기 변경",
                "벙커 위치·모양·크기 변경",
                "코스 배수 향상을 위한 부분적 절토·성토",
                "염해를 입은 잔디 생육을 위한 통상적인 성토",
                "작업도로 변경 및 포장",
            ],
            key="golf_action"
        )

        golf_action_info = {
            "차량정비고·부품보관창고 부지 바닥 포장":
                "차량정비고나 부품보관창고 부지의 바닥을 포장하는 행위입니다.",

            "잔디 배토용 부엽토·토사를 일시적으로 쌓아 놓는 행위":
                "잔디의 배토작업에 필요한 부엽토와 토사를 일시적으로 쌓아 놓는 행위입니다.",

            "골프장 배수로 정비":
                "기존 골프장의 배수로를 정비하는 행위입니다.",

            "잔디를 심고 가꾸는 행위":
                "기존 골프장 안에서 잔디를 심고 가꾸는 행위입니다.",

            "티 그라운드 모양·크기 변경":
                "티 그라운드의 모양이나 크기를 변경하는 행위입니다.",

            "벙커 위치·모양·크기 변경":
                "벙커의 위치·모양 또는 크기를 변경하는 행위입니다.",

            "코스 배수 향상을 위한 부분적 절토·성토":
                "코스 안의 배수를 개선하기 위하여 부분적으로 절토하거나 성토하는 행위입니다.",

            "염해를 입은 잔디 생육을 위한 통상적인 성토":
                "염해를 입은 잔디가 생육할 수 있도록 하기 위한 통상적인 성토입니다.",

            "작업도로 변경 및 포장":
                "기존 골프장의 작업도로를 변경하거나 포장하는 행위입니다.",
        }

        if golf_action != "선택하세요":
            st.success(
                "✅ 허가·신고 없이 가능한 행위입니다.\n\n"
                + golf_action_info[golf_action]
            )

            st.caption(
                "※ 기존 골프장을 통상적으로 운영·관리하기 위한 유지·보수 행위에 한합니다."
            )

    elif free_action_type == "재해의 긴급한 복구":

        disaster_action = st.selectbox(
            "② 세부 행위를 선택하세요.",
            [
                "선택하세요",
                "벌채면적 500㎡ 미만의 죽목 베기",
                "벌채수량 5㎥ 미만의 죽목 베기",
            ],
            key="disaster_action"
        )

        disaster_action_info = {
            "벌채면적 500㎡ 미만의 죽목 베기":
                "재해의 긴급한 복구를 위하여 벌채면적 500㎡ 미만으로 죽목을 베는 행위입니다. 연간 벌채면적은 1,000㎡를 초과할 수 없습니다.",

            "벌채수량 5㎥ 미만의 죽목 베기":
                "재해의 긴급한 복구를 위하여 벌채수량 5㎥ 미만으로 죽목을 베는 행위입니다. 연간 벌채수량은 10㎥를 초과할 수 없습니다.",
        }

        if disaster_action != "선택하세요":
            st.success(
                "✅ 허가·신고 없이 가능한 행위입니다.\n\n"
                + disaster_action_info[disaster_action]
            )

            st.caption(
                "※ 재해의 긴급한 복구를 위한 경우에 한하며, 시행규칙 별표 4 제7호의 연간 한도를 함께 충족해야 합니다."
            )

    elif free_action_type == "기존 건축물의 적법한 대지 안에 물건을 쌓아 놓는 행위":

        st.success(
            "✅ 허가·신고 없이 가능한 행위입니다.\n\n"
            "기존 건축물의 대지 안에 물건을 쌓아 놓는 행위입니다."
        )

        st.warning(
            "⚠️ 해당 대지는 관계 법령에 따라 적법하게 조성된 대지인 경우에 한합니다."
        )

        st.caption(
            "※ 개발제한구역법 시행규칙 별표 4 제8호에 해당하는 경우에 한합니다. "
            "다른 법령에 따른 제한이나 허가·신고 대상 여부는 별도로 확인해야 합니다."
        )

    elif free_action_type == "국유림·공유림 또는 자연공원 등의 관리 행위":

        st.warning(
            "⚠️ 모든 국유림·공유림 또는 자연공원에 적용되는 것은 아닙니다.\n\n"
            "국가산업단지 조성사업 등을 위해 광역도시계획에 따라 개발제한구역에서 "
            "해제된 지역을 대체하여 새로 개발제한구역으로 지정된 국유림·공유림 "
            "또는 자연공원 등을 효율적으로 관리하기 위한 행위에 해당해야 합니다."
        )

        forest_park_action = st.selectbox(
            "② 세부 행위를 선택하세요.",
            [
                "선택하세요",

                "국유림경영계획·산림경영계획에 따른 조림·숲가꾸기 및 벌채",
                "산림사업을 위한 임도·산불예방 및 진화시설 등 설치",
                "산림사업을 위한 산림복원",
                "사방사업을 위한 시설·복구 및 토지형질변경",
                "소나무재선충병 방제사업을 위한 벌채",

                "공원계획에 따른 공원시설 설치·건축물 철거·이전 등",
                "공원별 보전·관리계획에 따른 보전·관리 행위",
                "자연공원의 재난·재해 예방 및 복구",
                "자연공원 내 소나무재선충병 방제를 위한 벌채",
            ],
            key="forest_park_action"
        )

        forest_park_action_info = {
            "국유림경영계획·산림경영계획에 따른 조림·숲가꾸기 및 벌채":
                "산림 관할 행정청이 국유림경영계획 또는 산림경영계획에 따라 조림·숲가꾸기 및 벌채를 하는 행위입니다.",

            "산림사업을 위한 임도·산불예방 및 진화시설 등 설치":
                "산림 관할 행정청이 산림사업을 위하여 임도, 산불예방·진화시설 등 산림관리 기반시설을 설치하는 행위입니다.",

            "산림사업을 위한 산림복원":
                "산림 관할 행정청이 산림사업을 위하여 산림을 복원하는 행위입니다.",

            "사방사업을 위한 시설·복구 및 토지형질변경":
                "사방사업을 위하여 사방시설을 유지·관리하거나 인공구조물 설치, 파종·식재 및 이에 수반되는 토지형질변경을 하는 행위입니다.",

            "소나무재선충병 방제사업을 위한 벌채":
                "산림 관할 행정청이 소나무재선충병 방제사업을 위하여 벌채하는 행위입니다.",

            "공원계획에 따른 공원시설 설치·건축물 철거·이전 등":
                "공원관리청이 공원계획에 따라 공원시설을 설치하거나 건축물을 철거·이전하고 이에 수반되는 토지이용을 하는 행위입니다.",

            "공원별 보전·관리계획에 따른 보전·관리 행위":
                "공원관리청이 공원별 보전·관리계획에 따라 동식물 보호, 훼손지 복원, 탐방객 안전 및 오염 예방 등을 위하여 하는 보전·관리 행위입니다.",

            "자연공원의 재난·재해 예방 및 복구":
                "공원관리청이 공원사업을 위하여 자연공원의 재난·재해를 예방하거나 복구하는 행위입니다.",

            "자연공원 내 소나무재선충병 방제를 위한 벌채":
                "공원관리청이 소나무재선충병 방제를 위하여 벌채하는 행위입니다.",
        }

        if forest_park_action != "선택하세요":
            st.success(
                "✅ 별표 4의 적용대상 및 세부 요건을 모두 충족하는 경우 "
                "허가·신고 없이 가능한 행위입니다.\n\n"
                + forest_park_action_info[forest_park_action]
            )

            st.caption(
                "※ 개발제한구역법 시행규칙 별표 4 제9호의 적용대상에 해당하는지 "
                "먼저 확인해야 하며, 다른 법령에 따른 절차는 별도로 확인해야 합니다."
            )

elif menu == "🔍 법령·사례 검색":

    st.markdown(
        '<div class="main-title">🔍 법령·사례 검색</div>',
        unsafe_allow_html=True,
    )

    question = st.text_input(
        "질문을 입력하세요.",
        placeholder="예: 개발제한구역에서 농막 설치가 가능한가요?",
    )

    if st.button("검색하기"):
        if question.strip():
            answer, sources = search_and_answer(question)

            st.subheader("AI 답변")
            st.write(answer)

            if sources:
                st.subheader("📚 근거자료")

                for i, source in enumerate(sources, 1):
                    file_name = source.get("file_name", "자료명 없음")
                    page = source.get("page", "페이지 정보 없음")
                    text = source.get("text", "")

                    with st.expander(f"📄 근거자료 {i} | {file_name} | {page}페이지"):
                        st.write(text)

        else:
            st.warning("질문을 입력해 주세요.")

# --------------------------------------------------
# 행정처분 절차
# --------------------------------------------------
elif menu == "📋 행정처분 절차":

    st.markdown(
        '<div class="main-title">📋 행정처분 절차</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "개발제한구역 불법행위에 대한 기본적인 처리 흐름입니다."
    )

    st.info(
        "※ 절차 진행 중 시정 등 수시 확인\n\n"
        "• 각 단계에서 시정이 완료된 경우 → 시정완료 처리\n"
        "• 소유권 변동 등 종결사유가 발생한 경우 → 종결사유 확인 후 행정처분 종결 여부 검토\n"
        "• 2차 시정촉구 후에도 미시정인 경우 → 이행강제금 부과예고 → 이행강제금 부과 절차 진행"
    )
    st.warning(
        "※ 이행강제금 부과 횟수\n\n"
        "• 시정완료 시까지 매년 2회 이내"
    )
    
    steps = [
        "① 위반행위 적발",
        "② 현장계도 및 현장조사·증거자료 확보",
        "③ 행정처분의 사전통지",
        "④ 의견제출 (선택)",
        "⑤-1 시정명령-1차",
        "⑤-2 시정명령-2차(촉구)",

        "⑥ 이행강제금 부과예고",
        "⑦ 이행강제금 부과·징수",
    ]

    for step in steps:
        st.success(step)

        if step == "① 위반행위 적발":
            st.warning(
                "※ 위반행위 적발 시 고발 검토\n\n"
                "• 개발제한구역의 과도한 훼손\n"
                "• 중대한 위법행위\n"
                "• 상습적·고의적인 위반행위\n"
                "→ 해당하는 경우 시정명령 절차와 별도로 즉시 고발 여부 검토"
            )

        if step == "⑥ 이행강제금 부과예고":
            st.markdown("　↳ **필요 시 불법행위 고발 검토 및 고발**")
# --------------------------------------------------
# 이행강제금 계산
# --------------------------------------------------
elif menu == "🧮 이행강제금 계산":

    st.markdown(
        '<div class="main-title">🧮 이행강제금 계산</div>',
        unsafe_allow_html=True,
    )
    violation_category = st.selectbox(
        "① 위반 구분 선택",
        [
            "허가사항 위반",
            "신고사항 위반",
        ],
        key="enforcement_violation_category",
    )
    
    violation_type = st.selectbox(
        "② 위반행위 유형 선택",
        [
            "건축물의 건축",
            "건축물의 용도변경",
            "공작물의 설치",
            "토지의 형질변경",
            "물건을 쌓아놓는 행위",
            "죽목 벌채",
        ],
        key="enforcement_violation_type",
    )

    if violation_type in ["건축물의 건축", "건축물의 용도변경"]:
        st.info(
            "건축물의 건축·용도변경은 해당 연도의 지방세 시가표준액 조사·산정 기준에 따라 "
            "시가표준액을 산정한 후 개발제한구역법 시행령 별표 5의 기준을 적용합니다."
        )
    else:
        st.info(
            "토지 관련 위반행위는 해당 토지의 개별공시지가를 기준으로 "
            "개발제한구역법 시행령 별표 5의 기준을 적용합니다."
        )

    if violation_type in ["건축물의 건축", "건축물의 용도변경"]:
        standard_value = st.number_input(
            "③ 건물시가표준액(원/㎡)",
            min_value=0.0,
            step=1000.0,
        )

    else:
        standard_value = st.number_input(
            "③ 개별공시지가(원/㎡)",
            min_value=0.0,
            step=1000.0,
        )

    col1, col2 = st.columns(2)

    with col1:

        area = st.number_input(
            "위반 면적(㎡)",
            min_value=0.0,
            step=1.0,
        )


    if violation_category == "허가사항 위반":
        rate_map = {
            "건축물의 건축": 0.50,
            "건축물의 용도변경": 0.30,
            "공작물의 설치": 0.50,
            "토지의 형질변경": 0.30,
            "물건을 쌓아놓는 행위": 0.30,
            "죽목 벌채": 0.30,
        }
    else:
        rate_map = {
            "건축물의 건축": 0.25,
            "건축물의 용도변경": 0.15,
            "공작물의 설치": 0.25,
            "토지의 형질변경": 0.15,
            "물건을 쌓아놓는 행위": 0.15,
            "죽목 벌채": 0.15,
        }

    rate = rate_map[violation_type]

    adjustment_type = st.selectbox(
        "④ 가중·감경 선택",
        [
            "해당 없음",
            "가중",
            "감경",
        ],
        key="enforcement_adjustment_type",
    )

    if adjustment_type != "해당 없음":
        adjustment_rate = st.number_input(
            "가중·감경률(%)",
            min_value=0.0,
            max_value=50.0,
            step=1.0,
        )
    else:
        adjustment_rate = 0.0

    if st.button("계산하기"):
        base_result = standard_value * area * rate

        if adjustment_type == "가중":
            result = base_result * (1 + adjustment_rate / 100)
        elif adjustment_type == "감경":
            result = base_result * (1 - adjustment_rate / 100)
        else:
            result = base_result
            
        st.write(f"📌 별표 5 적용률: {rate * 100:.0f}%")
        st.write(f"💰 기본 산정액: {base_result:,.0f}원")

        if adjustment_type == "가중":
            st.write(f"⬆️ 가중률: {adjustment_rate:.0f}%")
        elif adjustment_type == "감경":
            st.write(f"⬇️ 감경률: {adjustment_rate:.0f}%")

        st.success(
            f"최종 예상 이행강제금: {result:,.0f}원"
        )

        st.caption(
            "※ 실제 금액은 위반 유형과 최신 산정기준을 확인해야 합니다."
        )


# --------------------------------------------------
# 자료실
# --------------------------------------------------
elif menu == "📁 자료실":

    st.markdown(
        '<div class="main-title">📁 자료실</div>',
        unsafe_allow_html=True,
    )

    st.write("현재 RAG 검색에 활용 중인 주요 자료입니다.")

    st.info("📄 개발제한구역 관리 매뉴얼")
    st.info("📄 개발제한구역 관리계획 절차")
    st.info("📄 개발제한구역 제도 안내")
    st.info("📄 개발제한구역 길라잡이")


# --------------------------------------------------
# 즐겨찾기
# --------------------------------------------------
elif menu == "⭐ 즐겨찾기":

    st.markdown(
        '<div class="main-title">⭐ 즐겨찾기</div>',
        unsafe_allow_html=True,
    )

    st.write("자주 확인하는 업무자료를 저장하는 메뉴입니다.")

    st.write("• 농막 설치 관련 사례")
    st.write("• 토지형질변경(성토) 기준")
    st.write("• 컨테이너 설치 사례")


# --------------------------------------------------
# 공지사항
# --------------------------------------------------
elif menu == "📢 공지사항":

    st.markdown(
        '<div class="main-title">📢 공지사항</div>',
        unsafe_allow_html=True,
    )

    st.write("• 개발제한구역법 시행령 개정사항")
    st.write("• 이행강제금 산정기준 개선 안내")
    st.write("• 업무가이드 업데이트")


# --------------------------------------------------
# 설정
# --------------------------------------------------
elif menu == "⚙️ 설정":

    st.markdown(
        '<div class="main-title">⚙️ 설정</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "향후 AI 모델, 관리자 기능, 데이터 업데이트 설정을 추가합니다."
    )