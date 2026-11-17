# Blockchain

Distributed ledgers: how many computers agree on one shared history without a central authority. It covers hashing, Merkle trees, consensus (proof of work and proof of stake), smart contracts, and the security problems that come with them.

## Safety first (read before installing anything)
- **Learn on testnets** (test networks such as Sepolia) using test coins that have no value.
- **Never** type a real seed phrase or private key into a lab project, a website or a tutorial.
- A course or tutorial is not financial advice. Don't put money into anything because of a learning project.
- Fake tokens and fake "airdrops" target learners. Check every address and link against an official source.
- Use a separate browser profile or wallet for development, with no real funds in it.

## Prerequisites
- [Cryptography](../cryptography/README.md): hashes and signatures
- JavaScript or Python
- [Data structures](../dsa/README.md): trees, hash maps

## Install (developer tools)
```bash
sudo pacman -S --needed nodejs npm go
```
Foundry, the Solidity toolkit: follow the official installation page at [book.getfoundry.sh](https://book.getfoundry.sh/getting-started/installation). Then check with:
```bash
forge --version
anvil --version
```
Hardhat is an alternative: `npm install --save-dev hardhat` inside a project folder.

Browser wallet (for testnets only): [MetaMask](https://metamask.io/). Create a new test wallet with no real funds in it.

## Weekly rhythm
- Each week, one concept (hashing, consensus, a contract pattern) and one small program that demonstrates it.
- Read one postmortem from [Rekt News](https://rekt.news/) and say how the bug could have been prevented.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — primary sources, learning material, security resources
