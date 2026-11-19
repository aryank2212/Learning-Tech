# Library: offline copies of the free books and papers

Learning-Tech links to many free books and papers. If you want offline copies, one script downloads them to a `library/` folder on your own machine.

## Why they aren't in the repository
Most of these works are copyrighted. The authors let you read them for free, but that doesn't give anyone the right to republish them. So the repository holds only the script and this list. The `library/` folder is git-ignored, and `scripts/check_repo.py` fails if a PDF or a library file is ever committed.

## How to use it
```bash
./scripts/fetch-library.sh
```
- Needs `git`, `curl` and Python 3. It downloads about 0.8 to 1 GB.
- It's polite: it obeys `robots.txt`, pauses between requests, and caps the pages and size per site.
- Re-running skips anything already downloaded. A progress log is written to `library/fetch.log`.
- If a site blocks scripts, the entry shows `FAIL` in the log. Open the link in your browser instead.
- Paid books (💲) are never downloaded. Buy them if you want them.
- Each copy keeps its own licence. Read it before you share anything.

## Open-source books (cloned from GitHub)

| Folder in `library/books/` | Source |
|---|---|
| `rust-book` | <https://github.com/rust-lang/book> |
| `rust-by-example` | <https://github.com/rust-lang/rust-by-example> |
| `rust-reference` | <https://github.com/rust-lang/reference> |
| `comprehensive-rust` | <https://github.com/google/comprehensive-rust> |
| `crafting-interpreters` | <https://github.com/munificent/craftinginterpreters> |
| `progit` | <https://github.com/progit/progit2> |
| `dive-into-deep-learning` | <https://github.com/d2l-ai/d2l-en> |
| `eloquent-javascript` | <https://github.com/marijnh/Eloquent-JavaScript> |
| `missing-semester` | <https://github.com/missing-semester/missing-semester> |

## Free web books (copied page by page)

| Folder in `library/books/` | Source |
|---|---|
| `ostep` | <https://pages.cs.wisc.edu/~remzi/OSTEP/> |
| `think-java` | <https://greenteapress.com/wp/think-java/> |
| `deep-learning-book` | <https://www.deeplearningbook.org/> |
| `high-performance-browser-networking` | <https://hpbn.co/> |
| `systems-approach-networking` | <https://book.systemsapproach.org/> |
| `sre-book` | <https://sre.google/sre-book/table-of-contents/> |
| `openintro-statistics` | <https://www.openintro.org/book/os/> |
| `islr` | <https://www.statlearning.com/> |
| `fpp3` | <https://otexts.com/fpp3/> |
| `r4ds` | <https://r4ds.hadley.nz/> |
| `speech-and-language-processing` | <https://web.stanford.edu/~jurafsky/slp3/> |
| `princeton-bitcoin-book` | <https://bitcoinbook.cs.princeton.edu/> |
| `fairness-and-ml` | <https://fairmlbook.org/> |
| `perfbook` | <https://mirrors.edge.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html> |
| `distributed-systems-tanenbaum` | <https://www.distributed-systems.net/index.php/books/ds3/> |
| `beej-bgnet` | <https://beej.us/guide/bgnet/> |
| `beej-bgc` | <https://beej.us/guide/bgc/> |
| `automate-the-boring-stuff` | <https://automatetheboringstuff.com/> |
| `rust-atomics-and-locks` | <https://marabos.nl/atomics/> |
| `software-engineering-at-google` | <https://abseil.io/resources/swe-book> |
| `aosa` | <https://aosabook.org/en/> |
| `cses-handbook` | <https://cses.fi/book/> |
| `quantum-country` | <https://quantum.country/> |
| `esl-elements-stat-learning` | <https://hastie.su.domains/ElemStatLearn/> |

## Direct PDFs

| File | Source |
|---|---|
| `library/books/mathematics-for-machine-learning.pdf` | <https://mml-book.github.io/book/mml-book.pdf> |
| `library/books/mathematics-for-computer-science-6042.pdf` | <https://courses.csail.mit.edu/6.042/spring18/mcs.pdf> |
| `library/papers/bitcoin-whitepaper.pdf` | <https://bitcoin.org/bitcoin.pdf> |

## arXiv papers
The script finds every `arxiv.org/abs/...` link in the Markdown files and saves the PDF to `library/papers/` as `arxiv-<id>.pdf`, pausing three seconds between downloads as arXiv requests.

## Adding something
Edit `scripts/fetch-library.sh`: add a `clone`, `mirror` or `pdf` line for a free, legally available source, and open a pull request. Don't add links to pirated copies.
