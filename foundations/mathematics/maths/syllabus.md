# Engineering maths syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md). Discrete maths has its own syllabus in [discrete-maths.md](discrete-maths.md).

### Phase 1 – Linear algebra I
- [ ] Vectors; dot and cross products
- [ ] Matrices and matrix multiplication
- [ ] Systems of linear equations; Gaussian elimination
- [ ] Rank, inverse, null space

🛠️ Project: solve a 5×5 system by hand, then with NumPy. Check the answer with a residual.

### Phase 2 – Linear algebra II
- [ ] Determinants
- [ ] Eigenvalues and eigenvectors; diagonalisation
- [ ] Orthogonality, projections, least squares
- [ ] Singular value decomposition (SVD)

🛠️ Project: principal component analysis (PCA) on a small image dataset. Reconstruct each image from k components and compare.

### Phase 3 – Single-variable calculus
- [ ] Limits; derivatives; chain, product and quotient rules
- [ ] Maxima and minima
- [ ] Integrals and the fundamental theorem of calculus
- [ ] Taylor series

🛠️ Project: use SymPy to find the critical points of a function, then check them numerically.

### Phase 4 – Multivariable calculus
- [ ] Partial derivatives; gradients; directional derivatives
- [ ] Jacobians and Hessians
- [ ] Multiple integrals (introduction)

🛠️ Project: visualise gradient descent on a two-variable loss surface.

### Phase 5 – Vector calculus and differential equations
- [ ] Divergence and curl; the ideas behind Green's and Stokes' theorems
- [ ] First- and second-order ODEs
- [ ] Euler's method and Runge–Kutta

🛠️ Project: simulate a damped pendulum with RK4 and plot its energy over time.

### Phase 6 – Probability
- [ ] Sample spaces; conditional probability; Bayes' rule
- [ ] Random variables; expectation and variance
- [ ] Binomial, Poisson, normal and exponential distributions
- [ ] Law of large numbers; central limit theorem

🛠️ Project: simulate the Monty Hall problem and confirm the answer. Show the central limit theorem with sums of dice.

### Phase 7 – Numerical methods
- [ ] IEEE 754 floating point; rounding and machine epsilon
- [ ] Root finding: bisection, Newton's method
- [ ] Numerical integration: trapezoid, Simpson's rule
- [ ] Interpolation
- [ ] Conditioning and numerical stability

🛠️ Project: show catastrophic cancellation in a formula, then fix it with a stable version.

### Phase 8 – Optimisation
- [ ] Convex sets and convex functions
- [ ] Gradient methods and their step sizes
- [ ] Lagrange multipliers
- [ ] Linear programming and the simplex idea

🛠️ Project: solve a small linear program with SciPy's `linprog`, then verify the solution by hand.

### Phase 9 – Information theory (optional, links to AI and cryptography)
- [ ] Entropy; joint and conditional entropy
- [ ] KL divergence and cross-entropy (the ML loss function)
- [ ] Mutual information

🛠️ Project: compute the entropy of text files in different languages and explain what the numbers mean.
