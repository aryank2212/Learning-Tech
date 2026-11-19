# Practice: Computer Networking

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Find the network address and broadcast address of 192.168.10.37/26.
- [ ] Draw the TCP three-way handshake.
- [ ] Use `dig` to find a domain's MX records.

## Level 2 — Medium (apply it)

- [ ] Split 10.0.0.0/16 into four equal subnets and list them.
- [ ] Write a TCP echo server and client in Python.
- [ ] Explain why DNS usually uses UDP.

## Level 3 — Hard (build and explain)

- [ ] Design routing for six routers using shortest paths.
- [ ] Set up a WireGuard tunnel between two virtual machines.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. How many usable host addresses does an IPv4 /24 have?

   <details><summary>Show answer</summary>

   254: 256 addresses minus the network and broadcast addresses.

   </details>

2. What is the TCP three-way handshake?

   <details><summary>Show answer</summary>

   SYN, SYN-ACK, ACK. It sets up a connection and agrees initial sequence numbers.

   </details>

3. What does DNS do?

   <details><summary>Show answer</summary>

   It translates names into IP addresses (and other records) using a hierarchy of resolvers and authoritative servers.

   </details>

4. Why does TCP use AIMD congestion control?

   <details><summary>Show answer</summary>

   To avoid overloading the network: it grows the window additively and cuts it multiplicatively on loss, so flows converge to a fair share.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
