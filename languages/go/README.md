# Go *(suggested)*

Simple, fast, garbage-collected language built for servers, networking and cloud tools. Docker, Kubernetes and Terraform are written in Go. It is one of the easiest compiled languages to learn.

## Install

```bash
sudo pacman -S --needed go
go version
go env GOPATH
```

Start a project: `mkdir hello-go && cd hello-go && go mod init example.com/hello`

## Syllabus

### Level 1 – Basics
- [ ] Packages, `main`, `go run`, `go build`
- [ ] Variables, types, `:=`, constants
- [ ] Slices, maps, structs
- [ ] Control flow: `if`, `for` (Go has only `for`), `switch`
- [ ] Functions, multiple return values, errors as values

### Level 2 – Intermediate
- [ ] Methods and interfaces
- [ ] Pointers (simpler than C)
- [ ] Error handling patterns, `errors.Is`, `errors.As`
- [ ] Testing with `go test`, table-driven tests
- [ ] Modules and dependencies

### Level 3 – Concurrency and servers
- [ ] Goroutines and channels
- [ ] `select`, `context`, timeouts
- [ ] `sync.Mutex`, `sync.WaitGroup`
- [ ] `net/http` server and client
- [ ] JSON, file I/O

### Level 4 – Real projects
- [ ] REST API with a database (`database/sql` + SQLite or Postgres)
- [ ] Logging, configuration, graceful shutdown
- [ ] Profiling with `pprof`
- [ ] Docker container for your app

## Resources

| | Resource | Notes |
|---|---|---|
| ⭐🆓 | [A Tour of Go](https://go.dev/tour/) | Official interactive intro |
| ⭐🆓 | [Go by Example](https://gobyexample.com/) | Short runnable examples |
| 🆓 | [Effective Go](https://go.dev/doc/effective_go) | Idioms, official |
| 🆓 | [Go documentation](https://go.dev/doc/) | Reference |
| 🆓 | [Exercism Go track](https://exercism.org/tracks/go) | Practice |
| 💲 | *The Go Programming Language* – Donovan & Kernighan | The classic |
| 💲 | *Learning Go* – Jon Bodner | Modern and practical |

## Projects

1. 🛠️ **URL shortener** with an HTTP server
2. 🛠️ **Concurrent web-status checker** using goroutines
3. 🛠️ **Chat server** with channels
4. 🛠️ **Todo REST API** with SQLite
