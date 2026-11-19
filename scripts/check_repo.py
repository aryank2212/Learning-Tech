#!/usr/bin/env python3
"""Checks Learning-Tech's structure and internal links (standard library only).

Run from anywhere:  python scripts/check_repo.py
Exit code 0 = all good, 1 = problems found.

It checks that:
- every subject folder has the required files (README, syllabus, resources, practice, ...)
- every subject README has a "My personal take" section and is linked from the root README
- every practice.md has three levels and a quick quiz
- every relative Markdown link and heading anchor resolves (repeated headings and code blocks handled)
- every Python file (examples and scripts) compiles
- no PDFs, no library/ files and no oversized files are tracked by git
"""
import os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)
errors = []

CATEGORIES = ["foundations", "software", "systems", "web", "data", "ai", "security", "emerging", "languages"]
TOP_LEVEL_SUBJECTS = {"research": ["README.md", "directions.md", "practice.md"]}

def subjects():
    found = []
    for cat in CATEGORIES:
        if not os.path.isdir(cat):
            errors.append(f"missing category folder: {cat}")
            continue
        for group in sorted(os.listdir(cat)):
            gpath = os.path.join(cat, group)
            if not os.path.isdir(gpath):
                continue
            for subj in sorted(os.listdir(gpath)):
                spath = os.path.join(gpath, subj)
                if os.path.isdir(spath):
                    found.append(spath.replace(os.sep, "/"))
    return found

def required_files(path):
    if path.startswith("languages/"):
        return ["README.md", "practice.md"]
    return ["README.md", "syllabus.md", "resources.md", "practice.md"]

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

# ---- structure ----
root_readme = read("README.md")
subject_paths = subjects() + list(TOP_LEVEL_SUBJECTS)
for path in subject_paths:
    need = TOP_LEVEL_SUBJECTS.get(path) or required_files(path)
    for name in need:
        if not os.path.isfile(os.path.join(path, name)):
            errors.append(f"{path}: missing {name}")
    readme = os.path.join(path, "README.md")
    if os.path.isfile(readme):
        text = read(readme)
        if "## My personal take" not in text:
            errors.append(f"{readme}: missing '## My personal take'")
        if f"{path}/README.md" not in root_readme:
            errors.append(f"README.md does not link to {path}/README.md")
    practice = os.path.join(path, "practice.md")
    if os.path.isfile(practice):
        p = read(practice)
        for level in ("Level 1", "Level 2", "Level 3"):
            if level not in p:
                errors.append(f"{practice}: missing {level}")
        if "## Quick quiz" not in p or p.count("<details>") < 3:
            errors.append(f"{practice}: needs a '## Quick quiz' with at least 3 questions")
for cat in CATEGORIES:
    if not os.path.isfile(os.path.join(cat, "README.md")):
        errors.append(f"{cat}/README.md is missing")
for name in ["README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "FAQ.md", "tutorial.md", "practice.md",
             "PATHS.md", "GLOSSARY.md", "ROADMAP.md", "CHANGELOG.md", "LIBRARY.md"]:
    if not os.path.isfile(name):
        errors.append(f"missing top-level file: {name}")

# ---- internal links and anchors ----
def slug(heading):
    h = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return h.replace(" ", "-")

md_files = []
for dirpath, dirnames, filenames in os.walk("."):
    dirnames[:] = [d for d in dirnames if d not in (".git", "library", "node_modules")]
    for fn in filenames:
        if fn.endswith(".md"):
            md_files.append(os.path.normpath(os.path.join(dirpath, fn)))
def heading_anchors(text):
    """GitHub-style anchors: repeated headings get -1, -2, ... and code blocks are ignored."""
    seen, found = {}, set()
    for line in re.sub(r"```.*?```", "", text, flags=re.S).splitlines():
        m = re.match(r"^#{1,6}\s+(.*)", line)
        if m:
            base = slug(m.group(1))
            n = seen.get(base, 0)
            seen[base] = n + 1
            found.add(base if n == 0 else f"{base}-{n}")
    return found

anchors = {f: heading_anchors(read(f)) for f in md_files}
checked = 0
for f in md_files:
    base = os.path.dirname(f)
    text = re.sub(r"```.*?```", "", read(f), flags=re.S)  # ignore code blocks
    for m in re.finditer(r"\]\(([^)\s]+)\)", text):
        link = m.group(1)
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        target, _, anchor = link.partition("#")
        tpath = os.path.normpath(os.path.join(base, target)) if target else f
        checked += 1
        if not os.path.exists(tpath):
            errors.append(f"{f}: broken link -> {link}")
        elif anchor and tpath.endswith(".md") and anchor not in anchors.get(tpath, set()):
            errors.append(f"{f}: missing anchor -> {link}")

# ---- example scripts must at least compile ----
compiled = 0
for dirpath, dirnames, filenames in os.walk("."):
    dirnames[:] = [d for d in dirnames if d not in (".git", "library", "node_modules", "out", "__pycache__")]
    for fn in filenames:
        if fn.endswith(".py"):
            path = os.path.normpath(os.path.join(dirpath, fn))
            try:
                compile(read(path), path, "exec")
                compiled += 1
            except SyntaxError as e:
                errors.append(f"{path}: syntax error: {e}")

# ---- git hygiene ----
try:
    tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.splitlines()
    for t in tracked:
        if t.startswith("library/"):
            errors.append(f"library file is tracked (copyright): {t}")
        elif t.lower().endswith(".pdf"):
            errors.append(f"PDF is tracked (copyright): {t}")
        elif os.path.isfile(t) and os.path.getsize(t) > 2_000_000:
            errors.append(f"file larger than 2 MB: {t}")
except Exception:
    print("note: git not available, skipped git hygiene checks")

print(f"subjects checked: {len(subject_paths)}   markdown files: {len(md_files)}   internal links: {checked}   python files compiled: {compiled}")
if errors:
    print(f"\n{len(errors)} problem(s):")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("all checks passed")
