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

## Study timeline (about 6 weeks)
| Weeks | Focus | Done when |
|---|---|---|
| 1–2 | Level 1: basics | Small command-line programs with tests |
| 3–4 | Levels 2–3: interfaces and concurrency | A concurrent program that shuts down cleanly |
| 5–6 | Level 4: real projects | A REST API with a database, in a Docker container |

## Common pitfalls
- **Goroutine leaks:** a goroutine waits on a channel nobody closes. Use `context` to cancel work.
- **Ignored errors** (`_ = f()`). Handle them or wrap them with context.
- **Nil interfaces:** an interface holding a nil pointer is not itself nil.
- **Slice aliasing:** `append` can overwrite data another slice shares.
- **Unclosed HTTP response bodies.** Always `defer resp.Body.Close()`.

## Where Go is used
Docker, Kubernetes, Terraform, Prometheus, Hugo and much of the cloud tooling.

## Ecosystem
- **Web:** `net/http` (standard library), chi, gin
- **Database:** `database/sql`, sqlc, GORM
- **CLI:** cobra
- **Testing:** `go test`, testify

## More reading
- *Let's Go* — Alex Edwards (💲)
- *Concurrency in Go* — Katherine Cox-Buday (💲)
- [The Go Blog](https://go.dev/blog/)
- [Go code review comments](https://go.dev/wiki/CodeReviewComments)

## Libraries for data, ML and AI
- **Numerics:** Gonum
- **Deep learning:** Gorgonia, GoMLX
- **Running exported models:** `onnxruntime_go`
- **Classical ML:** golearn (last released in 2022; check it fits your needs)

```bash
go get gonum.org/v1/gonum/mat
```
More in [ML libraries in other languages](../../../ai/frameworks/ml-libraries-other-languages/README.md#go).

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Go is my pick for servers and tooling. It's small enough to learn in weeks, and the standard library is excellent.
- Its simplicity is deliberate, and it sometimes frustrates (error handling is verbose). I think that trade-off is mostly worth it.
- Learn goroutines together with context from the start. Leaks are the usual mistake.
