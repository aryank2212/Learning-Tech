# Cryptography

The mathematics and engineering behind secrecy, integrity and authentication. It explains how passwords are stored safely, how HTTPS works, how signatures prove who sent a message, and why some systems are so hard to break.

> This section is about cryptography, the science. It does not cover trading or investing in crypto-currencies.

## Golden rules for learning
- **Never invent your own cipher or protocol** for real data. Use vetted libraries.
- **Learn by breaking weak designs** (toy RSA, ECB mode, reused nonces). That is how you learn to avoid them.
- **Keep keys out of git.** Use environment variables or a secret manager.
- **Use test keys and throwaway data** in every lab.

## Prerequisites
- Discrete maths: modular arithmetic and number theory (see [discrete maths](../../../foundations/mathematics/maths/discrete-maths.md), Phase 6)
- A programming language: Python, C or Rust

## Install
```bash
sudo pacman -S --needed openssl gnupg age
openssl version
gpg --version | head -1
age --version
mkdir -p ~/crypto-lab && cd ~/crypto-lab
uv init crypto-lab && cd crypto-lab
uv add cryptography pycryptodome pynacl
```
- `openssl` lets you inspect certificates and test TLS.
- `gnupg` and `age` encrypt files; `age` is simpler for everyday use.
- `pynacl` wraps libsodium, a well-reviewed library. Prefer it for real projects.

## Weekly rhythm
- Read one concept, then implement it in a few lines, and then break it.
- Attempt one Cryptopals or CryptoHack challenge a week.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, labs, standards, tools

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Crypto is one of the most useful subjects you can learn, and one of the easiest to get wrong. Use libraries, learn to break weak designs, and never roll your own for real data.
- Cryptopals is the best practical course I know. Do it, even if you only finish the first three sets.
- Post-quantum migration is coming. Learn the new standards now, while the transition is underway.
