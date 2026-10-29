"""core.py 테스트 — 핵심 함수마다 최소 1개. `pytest -q`로 실행."""
import pandas as pd

from app import core


def _df():
    return pd.DataFrame(
        {
            "equipment_id": ["EQ1", "EQ1", "EQ2", "EQ3", "EQ3", "EQ3"],
            "code": ["A", "B", "A", "A", "A", "C"],
            "minutes": [5, 10, 3, 7, 2, 1],
        }
    )


def test_validate_empty():
    assert core.validate(pd.DataFrame()) == ["데이터가 비어 있습니다."]


def test_validate_missing_column():
    problems = core.validate(_df(), required=["equipment_id", "nope"])
    assert problems and "nope" in problems[0]


def test_summarize_by_count():
    s = core.summarize_by(_df(), "equipment_id")
    assert list(s["equipment_id"]) == ["EQ3", "EQ1", "EQ2"]
    assert list(s["count"]) == [3, 2, 1]


def test_summarize_by_sum_sorts_by_sum():
    s = core.summarize_by(_df(), "equipment_id", "minutes")
    assert list(s["equipment_id"]) == ["EQ1", "EQ3", "EQ2"]
    assert list(s["sum"]) == [15, 10, 3]


def test_summarize_by_missing_key():
    import pytest
    with pytest.raises(KeyError):
        core.summarize_by(_df(), "missing")


def test_top_n():
    s = core.summarize_by(_df(), "code")
    assert len(core.top_n(s, 2)) == 2
    assert len(core.top_n(s, 0)) == 0
