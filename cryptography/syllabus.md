# Cryptography syllabus

Tick items in [progress/TRACKER.md](../progress/TRACKER.md).

### Phase 1 – Foundations
- [ ] Classical ciphers: Caesar, Vigenère
- [ ] Frequency analysis
- [ ] One-time pad and perfect secrecy
- [ ] Kerckhoffs' principle: security must not depend on secrecy of the design

🛠️ Project: break a Vigenère cipher using frequency analysis.

### Phase 2 – Number theory for crypto
- [ ] Greatest common divisor; modular inverses
- [ ] Fermat's and Euler's theorems
- [ ] Primality testing (Miller–Rabin)
- [ ] Discrete logarithms: why they're hard

🛠️ Project: implement Miller–Rabin and the extended Euclidean algorithm.

### Phase 3 – Symmetric encryption
- [ ] Block ciphers and AES
- [ ] Modes: ECB (why it fails), CBC, CTR, GCM
- [ ] Padding; IVs and nonces

🛠️ Project: encrypt an image with ECB, then with GCM. Compare the outputs (the "ECB penguin" shows the leak clearly).

### Phase 4 – Hash functions and MACs
- [ ] Preimage and collision resistance
- [ ] SHA-2 and SHA-3
- [ ] HMAC
- [ ] Password hashing: bcrypt, scrypt, Argon2; salts

🛠️ Project: a password store using Argon2, then measure how long a dictionary attack takes against it.

### Phase 5 – Key exchange
- [ ] Diffie–Hellman
- [ ] Elliptic-curve Diffie–Hellman (X25519)
- [ ] Forward secrecy

🛠️ Project: a toy Diffie–Hellman with small numbers, then X25519 from a library.

### Phase 6 – Public-key cryptography
- [ ] RSA: key generation, encryption, signatures
- [ ] Padding: OAEP and PSS
- [ ] Elliptic-curve basics; Ed25519 signatures

🛠️ Project: sign and verify a message with Ed25519. Show that a tampered message fails verification.

### Phase 7 – Certificates and PKI
- [ ] Certificate authorities and trust chains
- [ ] X.509 certificates
- [ ] Revocation: CRLs and OCSP
- [ ] Certificate Transparency

🛠️ Project: inspect a website's certificate chain with `openssl s_client -connect host:443` and explain each step.

### Phase 8 – Protocols
- [ ] TLS 1.3 handshake, at a high level
- [ ] SSH keys and key-only login
- [ ] GnuPG basics
- [ ] Double ratchet (Signal) at a conceptual level

🛠️ Project: set up SSH key-only login on a virtual machine and explain each step of the handshake.

### Phase 9 – Attacks
- [ ] Padding oracle attacks
- [ ] Timing side channels
- [ ] Nonce reuse in GCM
- [ ] Weak randomness
- [ ] Downgrade attacks

🛠️ Project: complete Cryptopals sets 1–3.

### Phase 10 – Advanced topics
- [ ] Zero-knowledge proofs: Schnorr identification
- [ ] Secure multi-party computation (concepts)
- [ ] Homomorphic encryption (concepts)
- [ ] Post-quantum standards: FIPS 203, 204 and 205

🛠️ Project: implement a Schnorr identification protocol and explain why it is zero-knowledge.
