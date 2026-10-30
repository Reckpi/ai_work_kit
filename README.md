# Generic AI-Native Work Kit (개인용 범용 작업 템플릿)

개인용 범용 작업 템플릿 (SK하이닉스 AI 해커톤 2026 2차 예선 대비로 작성). 과제별 코드·도메인 로직 없음. 결과 통지 전까지 공개 유지.

이 저장소는 특정 과제의 해답 코드를 포함하지 않는 **범용 작업 절차 템플릿**입니다.
내용: 작업 규칙(AGENTS.md), 절차 스킬(.agents/skills), 검토용 서브에이전트 정의(.codex/agents),
빈 Streamlit 스캐폴딩(starter/). 도메인 로직·과제별 코드 없음.

## 당일 반입 (외울 것은 이 한 줄)

```bash
git clone --depth 1 https://github.com/Reckpi/ai_work_kit.git /tmp/kit && bash /tmp/kit/setup.sh
```

`setup.sh`가 복사·임시폴더 삭제·커밋까지 한다. 기본 대상은 홈(~). README가 하위 폴더에 있으면 `bash /tmp/kit/setup.sh ~/<폴더>`.
끝나면 `ls -a`에 `.agents .codex AGENTS.md app tests`가 보여야 한다. 그 다음 `codex` → `/status` → `/model`.

수동 버전(스크립트가 안 될 때):
```bash
cd ~/workspace
cp -r /tmp/kit/AGENTS.md /tmp/kit/.agents /tmp/kit/.codex /tmp/kit/INTERVIEW.md /tmp/kit/AGREEMENT.md /tmp/kit/HANDOFF.md /tmp/kit/STATE.md /tmp/kit/SCENARIOS.md .
cp -r /tmp/kit/starter/* . && rm -rf /tmp/kit
git add -A && git commit -m "chore: add generic work templates"
```

## 스킬 호출 순서 (180분)

| 시각 | 호출 | 산출물 |
|---|---|---|
| 0:05 | SCENARIOS.md로 유형 판별 | — |
| 0:10 | `$interview` | INTERVIEW.md 채움 → 커밋 |
| 0:30 | `$agreement` | AGREEMENT.md → 담당자 DM 확인 → 커밋 |
| 0:40~2:15 | (빌드) | 15~20분마다 커밋 |
| 2:15 | `$verify` | VERIFY.md → 수정 → 커밋 |
| 2:40 | `$handoff` | HANDOFF.md, README 실행법 → 최종 커밋 |
| 2:50 | 제출 | 미리보기에서 파일 목록 확인 |

## clone이 안 될 때

각 문서는 10줄 안쪽이므로 손으로 친다. `codex` 안에서 `/init`으로 AGENTS.md 뼈대 생성.
