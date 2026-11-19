# DSA & Advanced DSA

Data structures and algorithms: how to store data so operations are fast, and how to solve problems efficiently. It is the core of CS degrees, technical interviews and competitive programming (ICPC, Codeforces, AtCoder).

Two parts:
- **Part A – DSA:** the core every software job expects.
- **Part B – Advanced DSA:** competitive programming, research, and systems work.

## Prerequisites
One language at Level 2 or better: Python, Java, C++, C or Rust. Python is quickest to start. C++ or Java is the usual choice for competitive programming.

## Install
```bash
sudo pacman -S --needed gcc python uv
uv init dsa-practice && cd dsa-practice
# C++ with sanitizers, for debugging solutions
g++ -std=c++17 -O2 -Wall -fsanitize=address,undefined sol.cpp -o sol
```
Java: see [Java](../../../languages/general/java/README.md).

Keep a `stress/` folder with a brute-force checker next to each solution. Compare the two on random inputs. This catches most bugs before you submit.

## Practice platforms
| Platform | Best for |
|---|---|
| [NeetCode](https://neetcode.io/) | Structured interview roadmap with videos |
| [LeetCode](https://leetcode.com/) | Interview problems, company tags |
| [CSES](https://cses.fi/problemset/) | Clean, well-graded competitive problems |
| [USACO Guide](https://usaco.guide/) | Step-by-step competitive programming path |
| [Codeforces](https://codeforces.com/) / [AtCoder](https://atcoder.jp/) | Live contests and rating |

## Weekly rhythm
- Three new problems a day, 30–45 minutes each, *before* reading any hint.
- Re-solve one old problem from a blank file each day.
- Once a week, a timed set of three problems.
- Keep a log: problem, pattern, mistake, time taken. Patterns repeat, and the log shows which ones you miss.

## Files
- [syllabus.md](syllabus.md) — topics in order, with projects
- [resources.md](resources.md) — books, courses, practice sites, visualisers

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- DSA is hard to fake and easy to practise. The interview grind is tiring, but the ideas are worth learning properly, not just pattern-matching.
- Solve a problem, then explain it aloud or write it up. Explaining exposes gaps that solving hides.
- Don't chase problem counts. Ten problems you understand beat fifty you've forgotten.
