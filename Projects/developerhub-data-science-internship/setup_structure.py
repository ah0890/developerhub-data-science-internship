"""
setup_structure.py
==================
Data Science Internship — Automatic Folder Structure Generator

Usage
-----
    python setup_structure.py

Run from inside your Data_Science_Internship directory
OR from anywhere — the structure is always created next to this file.

Works on Windows, Linux, and macOS with zero dependencies.
"""

import os
import sys
import platform

# ── ANSI colours (disabled automatically on Windows cmd) ──
USE_COLOUR = sys.stdout.isatty() and platform.system() != "Windows"

def c(text, code):
    return f"\033[{code}m{text}\033[0m" if USE_COLOUR else text

GREEN  = lambda t: c(t, "0;32")
CYAN   = lambda t: c(t, "0;36")
YELLOW = lambda t: c(t, "1;33")
BOLD   = lambda t: c(t, "1")

# ─────────────────────────────────────────────────────────
# CONFIG — edit ONLY this section if you want to change names
# ─────────────────────────────────────────────────────────

INTERNSHIP_FOLDER = "Data_Science_Internship"   # top-level name

STRUCTURE = {
    "Assignment_1": [],                          # empty — placeholder
    "Assignment_2": [],
    "Assignment_3": [],
    "Assignment_4": [                            # Medical Insurance Project
        "data",
        "notebooks",
        "charts",
        "models",
    ],
    "Assignment_5": [],
}

# README content for each folder
READMES = {
    "Assignment_1": "# Assignment_1\nAdd your project files here.\n",
    "Assignment_2": "# Assignment_2\nAdd your project files here.\n",
    "Assignment_3": "# Assignment_3\nAdd your project files here.\n",
    "Assignment_4": """\
# Assignment_4 — Medical Insurance Claim Prediction

A Machine Learning project using Linear Regression to predict annual
medical insurance charges from personal health and demographic data.

## Quick Start
1. Place `medical_cost.csv` inside the `data/` folder
2. Run:  `python run_pipeline.py`

## Folder Structure
```
Assignment_4/
├── data/           ← Drop medical_cost.csv here
├── notebooks/      ← Jupyter notebook (.ipynb)
├── charts/         ← Auto-generated visualisation PNGs
├── models/         ← Saved trained model (linear_regression.pkl)
└── README.md
```

## Model Performance
| Metric     | Score   |
|------------|---------|
| R² Score   | 0.9880  |
| MAE        | $1,910  |
| RMSE       | $2,449  |
| CV R²      | 0.9875  |
""",
    "Assignment_5": "# Assignment_5\nAdd your project files here.\n",
}

# ─────────────────────────────────────────────────────────


def make_dir(path: str, label: str) -> None:
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
        print(f"  {GREEN('[+] Created')}  {label}")
    else:
        print(f"  [=] Exists   {label}")


def write_readme(path: str, content: str, label: str) -> None:
    if not os.path.isfile(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  {GREEN('[+] Created')}  {label}")
    else:
        print(f"  [=] Exists   {label}")


def print_tree(root: str, prefix: str = "", is_last: bool = True) -> None:
    """Recursively print a visual directory tree."""
    name = os.path.basename(root)
    connector = "└── " if is_last else "├── "
    suffix = "/" if os.path.isdir(root) else ""
    print(prefix + connector + name + suffix)
    if os.path.isdir(root):
        children = sorted(
            [c for c in os.listdir(root) if not c.startswith(".")],
            key=lambda x: (not os.path.isdir(os.path.join(root, x)), x)
        )
        for i, child in enumerate(children):
            child_path = os.path.join(root, child)
            extension = "    " if is_last else "│   "
            print_tree(child_path, prefix + extension, i == len(children) - 1)


def main() -> None:
    # Root = directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # If this script is already inside Data_Science_Internship, use that as root.
    # Otherwise, create Data_Science_Internship next to the script.
    if os.path.basename(script_dir) == INTERNSHIP_FOLDER:
        root = script_dir
    else:
        root = os.path.join(script_dir, INTERNSHIP_FOLDER)

    print()
    print(CYAN("  " + "=" * 53))
    print(CYAN("   Data Science Internship — Structure Generator  "))
    print(CYAN("  " + "=" * 53))
    print(f"  Root : {YELLOW(root)}")
    print()

    # ── Create the top-level internship folder ──────────
    make_dir(root, INTERNSHIP_FOLDER + "/")

    # ── Create each assignment folder + its subfolders ──
    for assignment, subdirs in STRUCTURE.items():
        apath = os.path.join(root, assignment)
        make_dir(apath, f"{assignment}/")

        for sub in subdirs:
            spath = os.path.join(apath, sub)
            make_dir(spath, f"{assignment}/{sub}/")

        # Write README
        if assignment in READMES:
            readme_path = os.path.join(apath, "README.md")
            write_readme(readme_path, READMES[assignment], f"{assignment}/README.md")

    # ── Summary ─────────────────────────────────────────
    print()
    print(CYAN("  " + "=" * 53))
    print(CYAN("   Setup complete. Final structure:               "))
    print(CYAN("  " + "=" * 53))
    print()

    # Print the tree starting from the parent of root so we see the top name
    parent = os.path.dirname(root)
    name   = os.path.basename(root)
    print("  " + BOLD(name + "/"))
    children = sorted(
        [c for c in os.listdir(root) if not c.startswith(".")],
        key=lambda x: (not os.path.isdir(os.path.join(root, x)), x)
    )
    for i, child in enumerate(children):
        child_path = os.path.join(root, child)
        _print_tree_inner(child_path, prefix="  ", is_last=(i == len(children) - 1))

    print()
    print(f"  📁 Drop your CSV here :")
    print(f"  {YELLOW(os.path.join(root, 'Assignment_4', 'data') + os.sep)}")
    print()
    print("  ✅ All done. Happy coding!")
    print()


def _print_tree_inner(path: str, prefix: str = "", is_last: bool = True) -> None:
    name      = os.path.basename(path)
    connector = "└── " if is_last else "├── "
    suffix    = "/" if os.path.isdir(path) else ""
    print(prefix + connector + name + suffix)

    if os.path.isdir(path):
        children = sorted(
            [c for c in os.listdir(path) if not c.startswith(".")],
            key=lambda x: (not os.path.isdir(os.path.join(path, x)), x)
        )
        for i, child in enumerate(children):
            child_path = os.path.join(path, child)
            extension  = "    " if is_last else "│   "
            _print_tree_inner(child_path, prefix + extension, i == len(children) - 1)


if __name__ == "__main__":
    main()
