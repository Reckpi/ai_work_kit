"""입출력 — 파일 읽기와 기본 정규화만. 판정 로직은 core.py에."""
from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_table(source) -> pd.DataFrame:
    """CSV/XLSX 경로 또는 업로드 파일 객체를 DataFrame으로. 실패 시 빈 DataFrame."""
    try:
        name = getattr(source, "name", str(source))
        if name.lower().endswith((".xlsx", ".xls")):
            df = pd.read_excel(source)
        else:
            df = pd.read_csv(source)
    except Exception:
        return pd.DataFrame()
    df.columns = [str(c).strip() for c in df.columns]
    return df


def parse_datetime(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """지정 컬럼을 datetime으로. 파싱 실패 행은 NaT로 두고 제거하지 않는다."""
    if col in df.columns:
        df = df.copy()
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def list_sample_files(data_dir: str | Path = "data") -> list[Path]:
    p = Path(data_dir)
    if not p.exists():
        return []
    return sorted([f for f in p.iterdir() if f.suffix.lower() in (".csv", ".xlsx", ".xls")])
