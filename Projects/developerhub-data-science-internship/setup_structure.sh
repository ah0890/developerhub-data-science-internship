#!/usr/bin/env bash
# =============================================================
#  Data Science Internship — Folder Structure Setup
#  Usage:  bash setup_structure.sh
#  Run from inside your Data_Science_Internship directory,
#  or from anywhere — it creates the structure next to this file.
# =============================================================

set -euo pipefail

# ── Colours ───────────────────────────────────────────────
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RESET='\033[0m'

# ── Root = directory where this script lives ──────────────
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ""
echo -e "${CYAN}  =====================================================${RESET}"
echo -e "${CYAN}   Data Science Internship — Structure Generator       ${RESET}"
echo -e "${CYAN}  =====================================================${RESET}"
echo -e "  Root : ${YELLOW}${ROOT}${RESET}"
echo ""

# ── Helper function ────────────────────────────────────────
make_dir() {
    local path="$1"
    if [ ! -d "$path" ]; then
        mkdir -p "$path"
        echo -e "  ${GREEN}[+] Created${RESET}  ${path#$ROOT/}"
    else
        echo -e "  [=] Exists   ${path#$ROOT/}"
    fi
}

# ── Top-level assignment folders ──────────────────────────
for assignment in Assignment_1 Assignment_2 Assignment_3 Assignment_4 Assignment_5; do
    make_dir "${ROOT}/${assignment}"
done

# ── Assignment_4 sub-structure (Medical Insurance Project) ─
A4="${ROOT}/Assignment_4"
for subdir in data notebooks charts models; do
    make_dir "${A4}/${subdir}"
done

# ── Placeholder README for empty assignments ──────────────
for assignment in Assignment_1 Assignment_2 Assignment_3 Assignment_5; do
    readme="${ROOT}/${assignment}/README.md"
    if [ ! -f "$readme" ]; then
        cat > "$readme" <<EOF
# ${assignment}
Add your project files here.
EOF
        echo -e "  ${GREEN}[+] Created${RESET}  ${assignment}/README.md"
    fi
done

# ── Assignment_4 README (if missing) ──────────────────────
A4_README="${A4}/README.md"
if [ ! -f "$A4_README" ]; then
    cat > "$A4_README" <<'EOF'
# Assignment_4 — Medical Insurance Claim Prediction

A Machine Learning project using Linear Regression to predict annual
medical insurance charges from personal health and demographic data.

## Quick Start
1. Place `medical_cost.csv` in the `data/` folder
2. Run `python run_pipeline.py`

## Structure
```
Assignment_4/
├── data/           ← Drop medical_cost.csv here
├── notebooks/      ← Jupyter notebook
├── charts/         ← Auto-generated visualisations
├── models/         ← Saved trained model (.pkl)
└── README.md
```
EOF
    echo -e "  ${GREEN}[+] Created${RESET}  Assignment_4/README.md"
fi

# ── Print final tree ───────────────────────────────────────
echo ""
echo -e "${CYAN}  =====================================================${RESET}"
echo -e "${CYAN}   Setup complete. Final structure:                    ${RESET}"
echo -e "${CYAN}  =====================================================${RESET}"
echo ""

if command -v tree &>/dev/null; then
    tree "${ROOT}" --dirsfirst -L 3
else
    # Fallback if tree is not installed
    find "${ROOT}" -maxdepth 3 -not -path '*/\.*' | sort | \
    awk -v root="${ROOT}" '{
        gsub(root"/", "")
        depth = gsub("/", "/")
        indent = ""
        for(i=0;i<depth;i++) indent = indent "    "
        if(depth==0) print "Data_Science_Internship/"
        else {
            n = split($0, a, "/")
            print indent "├── " a[n] (system("test -d \"" $0 "\"") == 0 ? "/" : "")
        }
    }'
fi

echo ""
echo -e "  📁 Drop your CSV into:"
echo -e "  ${YELLOW}${A4}/data/${RESET}"
echo ""
