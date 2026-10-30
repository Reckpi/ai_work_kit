#!/usr/bin/env bash
# 당일 반입 스크립트. 사용: git clone --depth 1 <레포> /tmp/kit && bash /tmp/kit/setup.sh
# 과제 README.md가 있는 폴더(기본 ~/workspace)에 템플릿·스킬·스타터를 복사하고 커밋한다.
set -e
KIT="$(cd "$(dirname "$0")" && pwd)"
DEST="${1:-$HOME}"

cd "$DEST" || { echo "작업 폴더 없음: $DEST  (예: bash /tmp/kit/setup.sh ~ 또는 bash /tmp/kit/setup.sh ~/프로젝트폴더)"; exit 1; }
[ -f README.md ] || echo "주의: 여기에 README.md가 없음. 과제 루트가 맞는지 확인 ($DEST)"

# 문서·규칙 (과제 README.md는 건드리지 않음)
for f in AGENTS.md INTERVIEW.md AGREEMENT.md HANDOFF.md STATE.md SCENARIOS.md; do
  [ -e "$f" ] && echo "건너뜀(이미 있음): $f" || cp "$KIT/$f" .
done
cp -rn "$KIT/.agents" "$KIT/.codex" . 2>/dev/null || cp -r "$KIT/.agents" "$KIT/.codex" .

# 스타터 (기존 파일은 덮어쓰지 않음)
cp -rn "$KIT/starter/." . 2>/dev/null || true

# 임시 clone 제거
case "$KIT" in /tmp/*) rm -rf "$KIT" ;; esac

# 저장소 확인 후 커밋
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || git init -q
git add -A
git commit -q -m "chore: add generic work templates, skills and starter scaffold from public repo" || true

echo
echo "반입 완료: $DEST"
ls -a | tr '\n' ' '; echo
echo "다음: 터미널에 codex 입력 → /status → /model → \$interview"
