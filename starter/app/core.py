"""결정론 코어 — 판정·계산 로직은 전부 여기. 순수 함수만. 같은 입력 → 같은 출력.

과제에 맞게 함수를 교체한다. 아래는 '이벤트 로그 집계' 형태의 범용 예시.
"""
from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS: list[str] = []  # 과제 데이터에 맞게 채운다. 예: ["timestamp", "equipment_id", "code"]


def validate(df: pd.DataFrame, required: list[str] | None = None) -> list[str]:
    """필수 컬럼·빈 데이터 검사. 문제 목록을 반환(비어 있으면 정상)."""
    required = REQUIRED_COLUMNS if required is None else required
    problems: list[str] = []
    if df is None or df.empty:
        problems.append("데이터가 비어 있습니다.")
        return problems
    missing = [c for c in required if c not in df.columns]
    if missing:
        problems.append(f"필수 컬럼 누락: {missing}")
    return problems


def summarize_by(df: pd.DataFrame, key: str, value: str | None = None) -> pd.DataFrame:
    """key별 건수(및 value 합계)를 내림차순으로 집계."""
    if key not in df.columns:
        raise KeyError(f"컬럼 없음: {key}")
    g = df.groupby(key, dropna=False)
    out = g.size().rename("count").to_frame()
    if value and value in df.columns:
        out["sum"] = g[value].sum(min_count=1)
        out = out.sort_values(["sum", "count"], ascending=False)
    else:
        out = out.sort_values("count", ascending=False)
    return out.reset_index()


def top_n(summary: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """상위 n개만."""
    return summary.head(max(0, int(n))).reset_index(drop=True)
