#!/usr/bin/env bash
# Downloads the FREE books, guides and papers referenced in this repo into library/.
# - Paid books (💲) are never downloaded.
# - Large documentation sites (MDN, React, Python, etc.) are kept as links only.
# - Re-running skips anything already downloaded.
# - Every source URL is listed in library/SOURCES.md. Check the licence in each copy.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LIB="$ROOT/library"
LOG="$LIB/fetch.log"
mkdir -p "$LIB/books" "$LIB/papers"
: > "$LOG"

say() { echo "$1" | tee -a "$LOG"; }

# clone NAME URL — open-source book repos, shallow copy without history
clone() {
  local dest="$LIB/books/$1"
  if [ -d "$dest" ]; then say "skip  $1 (exists)"; return; fi
  if git clone -q --depth 1 "$2" "$dest" 2>>"$LOG"; then
    rm -rf "$dest/.git"; say "ok    $1 (git clone) $2"
  else
    rm -rf "$dest"; say "FAIL  $1 $2"
  fi
}

# mirror NAME URL DEPTH QUOTA_MB — free web books, limited depth and size
mirror() {
  local dest="$LIB/books/$1"
  if [ -d "$dest" ] && [ -n "$(ls -A "$dest" 2>/dev/null)" ]; then say "skip  $1 (exists)"; return; fi
  mkdir -p "$dest"
  python3 "$ROOT/scripts/mirror_site.py" "$2" "$dest" "$3" "$4" 2>>"$LOG"
  if [ -n "$(ls -A "$dest" 2>/dev/null)" ]; then say "ok    $1 (mirror depth $3) $2"; else say "FAIL  $1 $2"; fi
}

# pdf NAME URL — a single PDF (books or papers)
pdf() {
  local out="$LIB/$3/$1.pdf"
  if [ -s "$out" ]; then say "skip  $1 (exists)"; return; fi
  if curl -sL --fail --max-time 180 -A "Mozilla/5.0 learning-library-fetch" -o "$out" "$2" && [ -s "$out" ]; then
    say "ok    $1 $2"
  else
    rm -f "$out"; say "FAIL  $1 $2"
  fi
}

echo "== Open-source books (git)"
clone rust-book            https://github.com/rust-lang/book
clone rust-by-example      https://github.com/rust-lang/rust-by-example
clone rust-reference       https://github.com/rust-lang/reference
clone comprehensive-rust   https://github.com/google/comprehensive-rust
clone crafting-interpreters https://github.com/munificent/craftinginterpreters
clone progit               https://github.com/progit/progit2
clone dive-into-deep-learning https://github.com/d2l-ai/d2l-en
clone eloquent-javascript  https://github.com/marijnh/Eloquent-JavaScript
clone missing-semester     https://github.com/missing-semester/missing-semester

echo "== Free web books (mirrored, depth-limited)"
mirror ostep                  https://pages.cs.wisc.edu/~remzi/OSTEP/          1 50
mirror think-java             https://greenteapress.com/wp/think-java/          1 50
mirror deep-learning-book     https://www.deeplearningbook.org/                 2 80
mirror high-performance-browser-networking https://hpbn.co/                     2 80
mirror systems-approach-networking https://book.systemsapproach.org/           2 120
mirror sre-book               https://sre.google/sre-book/table-of-contents/    2 80
mirror openintro-statistics   https://www.openintro.org/book/os/                1 80
mirror islr                   https://www.statlearning.com/                    1 80
mirror fpp3                   https://otexts.com/fpp3/                          2 120
mirror r4ds                   https://r4ds.hadley.nz/                           2 120
mirror speech-and-language-processing https://web.stanford.edu/~jurafsky/slp3/  2 120
mirror princeton-bitcoin-book https://bitcoinbook.cs.princeton.edu/            2 120
mirror fairness-and-ml        https://fairmlbook.org/                           2 120
mirror perfbook               https://mirrors.edge.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html 1 80
mirror distributed-systems-tanenbaum https://www.distributed-systems.net/index.php/books/ds3/ 1 80
mirror beej-bgnet             https://beej.us/guide/bgnet/                      1 40
mirror beej-bgc               https://beej.us/guide/bgc/                        1 40
mirror automate-the-boring-stuff https://automatetheboringstuff.com/            2 80
mirror rust-atomics-and-locks https://marabos.nl/atomics/                       2 50
mirror software-engineering-at-google https://abseil.io/resources/swe-book      2 80
mirror aosa                   https://aosabook.org/en/                          2 80
mirror cses-handbook          https://cses.fi/book/                             1 80
mirror quantum-country        https://quantum.country/                          1 40
mirror esl-elements-stat-learning https://hastie.su.domains/ElemStatLearn/      1 80

echo "== Direct PDFs"
pdf mathematics-for-machine-learning https://mml-book.github.io/book/mml-book.pdf books
pdf mathematics-for-computer-science-6042 https://courses.csail.mit.edu/6.042/spring18/mcs.pdf books
pdf elements-of-statistical-learning https://hastie.su.domains/ElemStatLearn/printings/ESLII_print12.pdf books
pdf bitcoin-whitepaper       https://bitcoin.org/bitcoin.pdf papers

echo "== arXiv papers referenced in the repo"
cd "$ROOT" || exit 1
grep -rhoE 'arxiv\.org/abs/[^ )>"`]+' --include=*.md . | sed -E 's#arxiv\.org/abs/##; s/[.,;:]+$//' | sort -u | while read -r id; do
  safe="$(echo "$id" | tr '/' '_')"
  out="$LIB/papers/arxiv-$safe.pdf"
  if [ -s "$out" ]; then say "skip  arxiv $id (exists)"; continue; fi
  if curl -sL --fail --max-time 180 -A "learning-library-fetch" -o "$out" "https://arxiv.org/pdf/$id" && [ -s "$out" ]; then
    say "ok    arxiv $id"
  else
    rm -f "$out"; say "FAIL  arxiv $id"
  fi
  sleep 3   # arXiv asks for a pause between requests
done

echo "done. Log: $LOG"
du -sh "$LIB" 2>/dev/null
