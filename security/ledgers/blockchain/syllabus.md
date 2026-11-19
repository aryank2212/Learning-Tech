# Blockchain syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md). Use testnets and local chains only.

### Phase 1 – Hashing and Merkle trees
- [ ] SHA-256 and hash chains
- [ ] Merkle trees and inclusion proofs
- [ ] Why light clients use Merkle proofs

🛠️ Project: build a Merkle tree in Python and generate and verify an inclusion proof.

### Phase 2 – Keys and signatures
- [ ] Public and private keys; ECDSA and Ed25519 signatures
- [ ] Deriving addresses from public keys
- [ ] Why lost keys can't be recovered

🛠️ Project: generate a key pair locally, then sign and verify a message. No real funds involved.

### Phase 3 – Consensus basics
- [ ] The double-spend problem
- [ ] Byzantine faults
- [ ] Longest-chain rule; forks and finality

🛠️ Project: simulate a small blockchain with proof of work, and show what a fork looks like.

### Phase 4 – Proof of work vs proof of stake
- [ ] Mining difficulty and target hashes
- [ ] Validators, stake, and slashing
- [ ] Energy trade-offs (see [tech ethics](../../ethics/tech-ethics/README.md))

🛠️ Project: a proof-of-work miner with adjustable difficulty. Measure how difficulty changes the average block time.

### Phase 5 – Transactions and state
- [ ] Bitcoin's UTXO model
- [ ] Ethereum's account model
- [ ] Gas and state transitions

🛠️ Project: model a UTXO ledger and detect a double spend.

### Phase 6 – Smart contracts
- [ ] Solidity basics: types, functions, storage vs memory
- [ ] The EVM at a high level
- [ ] Events
- [ ] ERC-20 tokens (the standard, conceptually)
- [ ] Testing with Foundry

🛠️ Project: write a simple ERC-20-style token and test transfers on a local chain (`anvil`).

### Phase 7 – Smart-contract security
- [ ] Reentrancy
- [ ] Access control mistakes
- [ ] Oracle manipulation; front-running
- [ ] Integer issues and how Solidity 0.8 changed them
- [ ] Audit checklists

🛠️ Project: find and fix the reentrancy bug in a deliberately vulnerable contract, using [Damn Vulnerable DeFi](https://www.damnvulnerabledefi.xyz/) locally.

### Phase 8 – Scaling and layer 2
- [ ] Optimistic and zero-knowledge rollups
- [ ] State channels
- [ ] Data availability

🛠️ Project: write a one-page explanation of how a rollup posts its data to the base chain.

### Phase 9 – Zero-knowledge proofs
- [ ] zk-SNARKs and zk-STARKs at a conceptual level
- [ ] Arithmetic circuits
- [ ] Writing a small circuit with Circom

🛠️ Project: write a small circuit, generate a proof, and verify it.

### Phase 10 – Decentralised applications
- [ ] dApp architecture: front end, wallet, contracts, indexer
- [ ] Reading contract state with `viem` or `ethers`
- [ ] DAOs and governance attacks

🛠️ Project: a read-only dApp that displays on-chain data from a testnet.

### Phase 11 – Responsible building
- [ ] Privacy on public ledgers
- [ ] Scam and phishing patterns
- [ ] Regulation (varies by country)
- [ ] Threat modelling

🛠️ Project: a threat model for the dApp from Phase 10.
