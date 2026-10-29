"""Streamlit UI — 화면만. 판정·계산은 core.py 함수를 호출한다.

실행: streamlit run app/main.py --server.address 0.0.0.0 --server.port 8501 --server.headless true
"""
from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import core, io  # noqa: E402

st.set_page_config(page_title="작업 도구", layout="wide")
st.title("작업 도구")  # 과제에 맞게 제목·설명 교체

# --- 입력 --------------------------------------------------------------
with st.sidebar:
    st.header("데이터")
    uploaded = st.file_uploader("CSV / XLSX 업로드", type=["csv", "xlsx", "xls"])
    samples = io.list_sample_files("data")
    sample = st.selectbox("또는 샘플 선택", ["(없음)"] + [s.name for s in samples])

df = None
if uploaded is not None:
    df = io.load_table(uploaded)
elif sample != "(없음)":
    df = io.load_table(next(s for s in samples if s.name == sample))

if df is None:
    st.info("왼쪽에서 데이터를 올리거나 샘플을 선택하세요.")
    st.stop()

problems = core.validate(df)
if problems:
    for p in problems:
        st.error(p)
    st.stop()

# --- 미리보기 ----------------------------------------------------------
st.subheader("데이터 미리보기")
st.caption(f"{len(df):,} 행 × {len(df.columns)} 열")
st.dataframe(df.head(50), use_container_width=True)

# --- 핵심 기능 (AGREEMENT '만들 것' 1개를 여기에) ------------------------
st.subheader("집계")
cols = list(df.columns)
c1, c2, c3 = st.columns(3)
key = c1.selectbox("기준 컬럼", cols)
value = c2.selectbox("합계 컬럼(선택)", ["(없음)"] + cols)
n = c3.number_input("상위 N", min_value=1, max_value=100, value=5)

summary = core.summarize_by(df, key, None if value == "(없음)" else value)
st.dataframe(core.top_n(summary, int(n)), use_container_width=True)
st.bar_chart(core.top_n(summary, int(n)).set_index(key)["count"])

# --- 근거/한계 표시 (인지 축: 화면에 판단 근거를 남긴다) --------------------
with st.expander("이 화면이 계산하는 방식"):
    st.markdown(
        "- 집계는 `app/core.py`의 고정 로직으로 계산합니다(확률적 요소 없음).\n"
        "- 필수 컬럼이 없거나 데이터가 비면 중단하고 알립니다.\n"
        "- 알려진 한계: HANDOFF.md 참조."
    )
