import streamlit as st

st.set_page_config(page_title="내신 계산기 - 학업 설계서", page_icon=None, layout="wide")

# ============================================================================
# 데이터: 학업 설계서 (사진 속 표를 기반으로 정리했습니다.
# 표의 괄호 구성(택n)이 사진에서 다소 불명확한 부분은 최대한 그대로 옮기되,
# 실제 학교 자료와 다르면 아래 CURRICULA 딕셔너리 값만 고쳐서 쓰시면 됩니다.)
# ============================================================================

CURRICULA = {
    "2025년 신입생": {
        "학교 지정 과목": {
            "2학년 1학기 (2026년)": [("문학", 4), ("대수", 4), ("영어Ⅰ", 4), ("스포츠 생활1", 2)],
            "2학년 2학기 (2026년)": [("화법과 언어", 4), ("미적분Ⅰ", 4), ("영어Ⅱ", 4), ("스포츠 생활2", 2)],
            "3학년 1학기 (2027년)": [("독서와 작문", 4), ("확률과 통계", 4), ("스포츠 문화", 1), ("음악·미술 감상과 비평(교차)", 2)],
            "3학년 2학기 (2027년)": [("주제 탐구 독서", 4), ("실용 통계", 4), ("스포츠 과학", 1), ("음악·미술 감상과 비평(교차)", 2)],
        },
        "학교 선택 과목": {
            "2학년 1학기 (2026년)": {
                "단일 선택": [("국어", "언어생활 탐구", 3), ("수학", "기하", 3), ("영어", "영어 독해와 작문", 3)],
                "그룹": [
                    {
                        "label": "사회·과학 (택4)",
                        "pick": 4,
                        "courses": [
                            ("세계 시민과 지리", 3), ("세계사", 3), ("사회와 문화", 3), ("현대사회와 윤리", 3),
                            ("물리학", 3), ("생명과학", 3), ("기후변화와 환경생태", 3),
                        ],
                    },
                    {
                        "label": "제2외국어/한문 (택1)",
                        "pick": 1,
                        "courses": [("일본어", 3), ("중국어", 3), ("한문", 3)],
                    },
                ],
            },
            "2학년 2학기 (2026년)": {
                "단일 선택": [("국어", "문학과 영상", 3), ("수학", "경제 수학", 3), ("영어", "심화 영어", 3)],
                "그룹": [
                    {
                        "label": "사회·과학 (택4)",
                        "pick": 4,
                        "courses": [
                            ("한국지리 탐구", 3), ("동아시아 역사 기행", 3), ("경제", 3), ("윤리와 사상", 3),
                            ("화학", 3), ("지구과학", 3), ("역학과 에너지", 3), ("세포와 물질대사", 3),
                        ],
                    },
                    {
                        "label": "제2외국어/한문 (택1)",
                        "pick": 1,
                        "courses": [("언어생활과 한자", 3), ("중국 문화", 3), ("일본 문화", 3)],
                    },
                ],
            },
            "3학년 1학기 (2027년)": {
                "단일 선택": [("국어", "매체 의사소통", 3), ("수학", "미적분Ⅱ", 3), ("영어", "심화 영어 독해와 작문", 3)],
                "그룹": [
                    {
                        "label": "사회·과학 (택4)",
                        "pick": 4,
                        "courses": [
                            ("도시의 미래 탐구", 3), ("정치", 3), ("인문학과 윤리", 3), ("국제 관계의 이해", 3), ("사회문제 탐구", 3),
                            ("전자기와 양자", 3), ("물질과 에너지", 3), ("화학 반응의 세계", 3), ("생물의 유전", 3),
                            ("행성우주과학", 3), ("지구시스템과학", 3),
                        ],
                    },
                    {
                        "label": "기술가정/정보·교양 (택2)",
                        "pick": 2,
                        "courses": [("정보", 3), ("생태와 환경", 3), ("교육의 이해", 3)],
                    },
                ],
            },
            "3학년 2학기 (2027년)": {
                "단일 선택": [("국어", "직무 의사소통", 3), ("수학", "인공지능 수학", 3), ("영어", "세계 문화와 영어", 3)],
                "그룹": [
                    {
                        "label": "사회·과학 (택4)",
                        "pick": 4,
                        "courses": [
                            ("여행지리", 3), ("역사로 탐구하는 현대 세계", 3), ("기후변화와 지속가능한 세계", 3), ("윤리문제 탐구", 3),
                            ("과학의 역사와 문화", 3), ("융합과학 탐구", 3),
                        ],
                    },
                    {
                        "label": "교양·기술가정/정보 (택2)",
                        "pick": 2,
                        "courses": [("논술", 3), ("진로와 직업", 3), ("인공지능 기초", 3)],
                    },
                ],
            },
        },
    },
    "2026년 신입생": {
        "학교 지정 과목": {
            "2학년 1학기 (2027년)": [("문학", 4), ("대수", 4), ("영어Ⅰ", 4), ("스포츠 생활1", 2)],
            "2학년 2학기 (2027년)": [("화법과 언어", 4), ("미적분Ⅰ", 4), ("영어Ⅱ", 4), ("스포츠 생활2", 2)],
            "3학년 1학기 (2028년)": [("독서와 작문", 4), ("확률과 통계", 4), ("스포츠 문화", 1), ("음악·미술 감상과 비평(교차)", 2)],
            "3학년 2학기 (2028년)": [("주제 탐구 독서", 4), ("실용 통계", 4), ("스포츠 과학", 1), ("음악·미술 감상과 비평(교차)", 2)],
        },
        "학교 선택 과목": {
            "2학년 1학기 (2027년)": {
                "단일 선택": [("국어", "언어생활 탐구", 3), ("수학", "기하", 3), ("영어", "영어 독해와 작문", 3)],
                "그룹": [
                    {
                        "label": "사회·과학 (택4)",
                        "pick": 4,
                        "courses": [
                            ("세계 시민과 지리", 3), ("세계사", 3), ("사회와 문화", 3), ("현대사회와 윤리", 3),
                            ("물리학", 3), ("생명과학", 3), ("기후변화와 환경생태", 3),
                        ],
                    },
                    {
                        "label": "제2외국어/한문·정보 (택1)",
                        "pick": 1,
                        "courses": [("일본어", 3), ("중국어", 3), ("정보", 3)],
                    },
                ],
            },
            "2학년 2학기 (2027년)": {
                "단일 선택": [("국어", "문학과 영상", 3), ("수학", "경제 수학", 3), ("영어", "심화 영어", 3)],
                "그룹": [
                    {
                        "label": "사회·과학 (택4)",
                        "pick": 4,
                        "courses": [
                            ("한국지리 탐구", 3), ("동아시아 역사 기행", 3), ("경제", 3), ("윤리와 사상", 3),
                            ("화학", 3), ("지구과학", 3), ("역학과 에너지", 3), ("세포와 물질대사", 3),
                        ],
                    },
                    {
                        "label": "제2외국어/한문·정보 (택1)",
                        "pick": 1,
                        "courses": [("일본 문화", 3), ("중국 문화", 3), ("인공지능 기초", 3)],
                    },
                ],
            },
            "3학년 1학기 (2028년)": {
                "단일 선택": [("국어", "매체 의사소통", 3), ("수학", "미적분Ⅱ", 3), ("영어", "심화 영어 독해와 작문", 3)],
                "그룹": [
                    {
                        "label": "사회·과학 (택4)",
                        "pick": 4,
                        "courses": [
                            ("도시의 미래 탐구", 3), ("정치", 3), ("인문학과 윤리", 3), ("국제 관계의 이해", 3), ("사회문제 탐구", 3),
                            ("전자기와 양자", 3), ("물질과 에너지", 3), ("화학 반응의 세계", 3), ("생물의 유전", 3),
                            ("행성우주과학", 3), ("지구시스템과학", 3),
                        ],
                    },
                    {
                        "label": "교양 (택2)",
                        "pick": 2,
                        "courses": [("생태와 환경", 3), ("교육의 이해", 3), ("논리와 사고", 3)],
                    },
                ],
            },
            "3학년 2학기 (2028년)": {
                "단일 선택": [("국어", "직무 의사소통", 3), ("수학", "인공지능 수학", 3), ("영어", "세계 문화와 영어", 3)],
                "그룹": [
                    {
                        "label": "사회·과학 (택4)",
                        "pick": 4,
                        "courses": [
                            ("여행지리", 3), ("역사로 탐구하는 현대 세계", 3), ("기후변화와 지속가능한 세계", 3), ("윤리문제 탐구", 3),
                            ("과학의 역사와 문화", 3), ("융합과학 탐구", 3),
                        ],
                    },
                    {
                        "label": "교양 (택2)",
                        "pick": 2,
                        "courses": [("논술", 3), ("진로와 직업", 3), ("인간과 심리", 3)],
                    },
                ],
            },
        },
    },
}

DEFAULT_GRADE = 1.0

# ============================================================================
# 계산 보조 함수
# ============================================================================

def grade_input(key, label, credit):
    """등급 입력창을 그려주고 (학점, 등급) 튜플을 반환"""
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.write(f"{label}  ·  {credit}학점")
    with col_b:
        grade = st.number_input(
            "등급", min_value=0.0, max_value=9.0, step=0.1,
            value=DEFAULT_GRADE, key=key, label_visibility="collapsed",
        )
    return credit, grade


def render_semester(version, semester_label, fixed_courses, elective_data, totals):
    st.subheader(semester_label)

    semester_totals = {"weighted": 0.0, "credit": 0.0}
    selected_rows = []  # (과목명, 학점, 등급) - 이번 학기에 반영된 모든 과목

    st.markdown("**학교 지정 과목**")
    for name, credit in fixed_courses:
        key = f"{version}|{semester_label}|fixed|{name}"
        credit_v, grade = grade_input(key, name, credit)
        semester_totals["weighted"] += credit_v * grade
        semester_totals["credit"] += credit_v
        selected_rows.append((name, credit_v, grade))

    st.markdown("**학교 선택 과목 · 단일 선택**")
    for subject, name, credit in elective_data["단일 선택"]:
        key = f"{version}|{semester_label}|single|{subject}|{name}"
        credit_v, grade = grade_input(key, f"[{subject}] {name}", credit)
        semester_totals["weighted"] += credit_v * grade
        semester_totals["credit"] += credit_v
        selected_rows.append((f"[{subject}] {name}", credit_v, grade))

    for group in elective_data["그룹"]:
        st.markdown(f"**{group['label']}**")
        checked_count = 0
        for name, credit in group["courses"]:
            ck_key = f"{version}|{semester_label}|group|{group['label']}|{name}|check"
            col_ck, col_name, col_grade = st.columns([1, 3, 1])
            with col_ck:
                checked = st.checkbox("선택", key=ck_key, label_visibility="collapsed")
            with col_name:
                st.write(f"{name}  ·  {credit}학점")
            with col_grade:
                grade_key = f"{version}|{semester_label}|group|{group['label']}|{name}|grade"
                if checked:
                    grade = st.number_input(
                        "등급", min_value=0.0, max_value=9.0, step=0.1,
                        value=DEFAULT_GRADE, key=grade_key, label_visibility="collapsed",
                    )
                    semester_totals["weighted"] += credit * grade
                    semester_totals["credit"] += credit
                    checked_count += 1
                    selected_rows.append((name, credit, grade))
                else:
                    st.write("")
        if checked_count != group["pick"]:
            st.caption(f"{group['label']} — 현재 {checked_count}개 선택됨 (기준: {group['pick']}개)")

    st.markdown("**이번 학기 선택 과목 · 내신 요약**")
    if selected_rows:
        st.table(
            {
                "과목": [r[0] for r in selected_rows],
                "학점": [r[1] for r in selected_rows],
                "등급": [r[2] for r in selected_rows],
            }
        )
        semester_gpa = semester_totals["weighted"] / semester_totals["credit"]
        col1, col2 = st.columns(2)
        col1.metric("이번 학기 이수 학점", f"{semester_totals['credit']:.0f}")
        col2.metric("이번 학기 내신", f"{semester_gpa:.2f}")
    else:
        st.info("반영된 과목이 없습니다.")

    totals["weighted"] += semester_totals["weighted"]
    totals["credit"] += semester_totals["credit"]

    st.markdown("---")


# ============================================================================
# 화면 구성
# ============================================================================

st.title("학업 설계서 내신 계산기")

version = st.radio("신입생 연도 선택", list(CURRICULA.keys()), horizontal=True)

st.caption(
    "과목마다 등급(내신) 기본값은 1.0으로 되어 있습니다. "
    "선택 과목은 체크하면 등급 입력창이 나타나고, 학기별로 선택한 과목과 내신이 표로 정리되며, "
    "맨 아래에서 4개 학기를 합산한 총 내신을 계산합니다."
)

data = CURRICULA[version]
totals = {"weighted": 0.0, "credit": 0.0}

for semester_label, fixed_courses in data["학교 지정 과목"].items():
    elective_data = data["학교 선택 과목"][semester_label]
    with st.expander(semester_label, expanded=True):
        render_semester(version, semester_label, fixed_courses, elective_data, totals)

st.header("4개 학기 총 내신")
if totals["credit"] > 0:
    overall = totals["weighted"] / totals["credit"]
    col1, col2 = st.columns(2)
    col1.metric("총 이수 학점", f"{totals['credit']:.0f}")
    col2.metric("총 내신 (학점 가중 평균)", f"{overall:.2f}")
else:
    st.info("아직 반영된 과목이 없습니다.")
