# Cryptography resources

## Books
| | Book | Notes |
|---|---|---|
| ⭐💲 | *Serious Cryptography* (2nd ed) — Jean-Philippe Aumasson | Modern and clear |
| ⭐💲 | *Introduction to Modern Cryptography* (3rd ed) — Katz & Lindell | The standard university text |
| 💲 | *Cryptography Engineering* — Ferguson, Schneier, Kohno | Practical design |
| 🆓 | *A Graduate Course in Applied Cryptography* — Boneh & Shoup | [Free PDF](https://toc.cryptobook.us/) |
| 💲 | *Understanding Cryptography* — Paar & Pelzl | Accessible, with exercises |
| 💲 | *The Code Book* — Simon Singh | History of codes, for motivation |

## Labs and courses
- ⭐🆓 [Cryptopals challenges](https://cryptopals.com/) — the best hands-on attack course
- ⭐🆓 [CryptoHack](https://cryptohack.org/) — CTF-style cryptography challenges
- 🆓 [Dan Boneh — Cryptography I (Coursera)](https://www.coursera.org/learn/crypto) — free to audit
- 🆓 Stanford CS255 (Boneh) lecture materials — search the course name
- 🆓 [Cryptography Stack Exchange](https://crypto.stackexchange.com/) — questions and expert answers

## Standards and specifications
- [NIST post-quantum cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography) — FIPS 203 (ML-KEM), 204 (ML-DSA), 205 (SLH-DSA)
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [RFC 7748 — X25519 and X448](https://www.rfc-editor.org/rfc/rfc7748)
- [RFC 8032 — Ed25519](https://www.rfc-editor.org/rfc/rfc8032)
- [Mozilla server-side TLS guidance](https://wiki.mozilla.org/Security/Server_Side_TLS)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — password storage and encryption guidance

## Tools and libraries
- [OpenSSL](https://www.openssl.org/), [GnuPG](https://gnupg.org/), [age](https://age-encryption.org/)
- [testssl.sh](https://testssl.sh/) — check a server's TLS configuration
- [libsodium](https://libsodium.org/) and [PyNaCl](https://pynacl.readthedocs.io/)
- [RustCrypto](https://github.com/RustCrypto) — pure-Rust crypto crates
- [Python `cryptography` package](https://cryptography.io/)

## Safety reminder
Test only systems you own, or systems you have written permission to test. Never use a lab key for real data.
