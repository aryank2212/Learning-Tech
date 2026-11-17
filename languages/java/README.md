# Java

An object-oriented language that runs on the Java Virtual Machine (JVM). It is widely used for enterprise backends, large-scale data systems (Spark and Kafka run on the JVM), and Android-related tooling. Spring Boot is one of the most common ways to build web APIs.

## Install
```bash
sudo pacman -S --needed jdk-openjdk maven gradle
java -version && javac -version
mvn -v | head -1
```
Use the latest LTS release (Java 21 or newer).

Editors:
- VS Code: install the Extension Pack for Java (`vscjava.vscode-java-pack`)
- IntelliJ IDEA Community, free from [jetbrains.com](https://www.jetbrains.com/idea/)

Your first program:
```bash
mkdir -p ~/java-learning/hello && cd ~/java-learning/hello
cat > Hello.java <<'EOF'
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
EOF
javac Hello.java && java Hello
```

## Syllabus

### Level 1 – Basics
- [ ] `javac` and `java`; the `main` method
- [ ] Primitive types and reference types; `String` is immutable
- [ ] Operators, `if`, `switch`, loops
- [ ] Arrays; methods; `var` (Java 10+)

### Level 2 – Object-oriented programming
- [ ] Classes, constructors, encapsulation, access modifiers
- [ ] Inheritance, interfaces, abstract classes, polymorphism
- [ ] `equals`, `hashCode`, `toString`
- [ ] Enums; records (Java 16+); sealed classes (Java 17+)
- [ ] Pattern matching for `instanceof` and `switch` (Java 21)

### Level 3 – Standard library
- [ ] Collections: `List`, `Set`, `Map`, `Deque`
- [ ] Generics and bounded types
- [ ] `Comparable` and `Comparator`
- [ ] Lambdas, method references, streams, `Optional`
- [ ] Exceptions: checked vs unchecked; try-with-resources
- [ ] File I/O with `java.nio.file`; dates with `java.time`

### Level 4 – Concurrency
- [ ] Threads; `ExecutorService`; `CompletableFuture`
- [ ] `synchronized`, locks, atomic variables
- [ ] Concurrent collections
- [ ] Virtual threads (Java 21)

### Level 5 – Ecosystem
- [ ] Maven and Gradle; dependency management
- [ ] Testing with JUnit 5 and Mockito
- [ ] JDBC, then JPA and Hibernate
- [ ] Spring Boot: REST controllers, dependency injection, Spring Data
- [ ] Logging with SLF4J
- [ ] Profiling with Java Flight Recorder and VisualVM

## Projects
1. 🛠️ **Bank account CLI** with OOP design and JUnit tests
2. 🛠️ **Library system** with collections and file persistence
3. 🛠️ **Parallel web crawler** with an `ExecutorService`
4. 🛠️ **REST API** with Spring Boot and PostgreSQL
5. 🛠️ **Desktop app** with JavaFX (optional)

## Resources
| | Resource | Notes |
|---|---|---|
| ⭐🆓 | [Java tutorials (dev.java)](https://dev.java/learn/) | Official learning path |
| ⭐🆓 | [Oracle Java Tutorials](https://docs.oracle.com/javase/tutorial/) | Classic reference tutorials |
| 🆓 | [Think Java](https://greenteapress.com/wp/think-java/) — Allen Downey | Free textbook |
| 🆓 | [Baeldung](https://www.baeldung.com/) | Practical articles for the Java ecosystem |
| 🆓 | [Spring guides](https://spring.io/guides) | Short, working Spring Boot projects |
| 🆓 | [Exercism Java track](https://exercism.org/tracks/java) | Practice with mentor feedback |
| 🆓 | [Java 21 API docs](https://docs.oracle.com/en/java/javase/21/docs/api/) | Standard library reference |
| 💲 | *Head First Java* — Kathy Sierra & Bert Bates | Beginner-friendly book |
| 💲 | *Effective Java* — Joshua Bloch | Best practices, essential |
| 💲 | *Core Java, Volume I* — Horstmann & Cornell | Thorough reference |
| 💲 | *Java: The Complete Reference* — Herbert Schildt | Broad reference |
| 💲 | *Java Concurrency in Practice* — Brian Goetz | Concurrency, essential for Level 4 |

## Common pitfalls
- Comparing strings with `==` instead of `equals`
- Forgetting to override `hashCode` when you override `equals`
- Catching exceptions and doing nothing with them
- Using raw types instead of generics
- Mutating a collection while iterating over it

## Where Java is used
Banks and large enterprises, Android app tooling, big-data platforms (Spark, Kafka, Hadoop), and Minecraft (Java Edition).
