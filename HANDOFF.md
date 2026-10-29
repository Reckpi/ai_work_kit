# HANDOFF — 인수인계 (다음 사람·다음 세션용)

## 1. 한 줄 요약
- 무엇을 위해 무엇을 만들었나:

## 2. 현재 상태
- 동작하는 것:
- 동작하지 않거나 미완인 것:
- 테스트: `pytest -q` 결과 → passed / failed

## 3. 실행 방법
```bash
pip install -r requirements.txt
streamlit run app/main.py --server.address 0.0.0.0 --server.port 8501 --server.headless true
# Browser 미리보기: PORT 8501, 경로 /
```
- 샘플 데이터: `data/`

## 4. 주요 결정과 이유
| 결정 | 이유 | 대안(버린 것) |
|---|---|---|
|  |  |  |

## 5. 알려진 약점 (서술형 대비 — 지점 / 왜 위험 / 다음 검증)
1.
2.
3.

## 6. 다음에 할 일 (우선순위 순)
1.
2.

## 7. 담당자와 합의한 범위 밖 요청 (받았지만 안 한 것)
-

## 8. 파일 지도
- `app/core.py` — 판정·계산 로직(순수 함수)
- `app/main.py` — Streamlit UI
- `app/io.py` — 파일 입출력·검증
- `tests/test_core.py` — 핵심 로직 테스트
- `INTERVIEW.md` / `AGREEMENT.md` / `VERIFY.md` — 과정 기록
