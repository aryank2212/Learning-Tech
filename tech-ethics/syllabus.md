# Tech ethics syllabus

Tick items in [progress/TRACKER.md](../progress/TRACKER.md).

### Phase 1 – Ethical frameworks
- [ ] Consequentialism (utilitarianism)
- [ ] Deontology: duties and rights
- [ ] Virtue ethics and care ethics
- [ ] Justice (John Rawls)

🛠️ Project: apply each framework to the same product decision. Write how the answer changes.

### Phase 2 – Professional responsibility
- [ ] Professional codes: ACM and IEEE
- [ ] Conflicts of interest
- [ ] Raising concerns and whistle-blowing

🛠️ Project: write your own five-line code of conduct for engineering work, and justify each line.

### Phase 3 – Privacy and data protection
- [ ] Personal data, consent, data minimisation
- [ ] Purpose limitation
- [ ] Why "anonymised" data often isn't
- [ ] GDPR principles; privacy by design

🛠️ Project: audit a web app you built. List every piece of data it collects, and what you would remove.

### Phase 4 – Fairness and bias
- [ ] Where bias comes from: data, labels, measurement, deployment
- [ ] Fairness definitions: demographic parity, equalised odds, calibration
- [ ] Why these definitions can't all be satisfied together

🛠️ Project: compute fairness metrics on a public dataset (for example, Adult or COMPAS) and explain the trade-off you found.

### Phase 5 – Accountability and transparency
- [ ] Model cards and datasheets
- [ ] Audits, appeals and redress
- [ ] Explaining decisions to the people affected

🛠️ Project: write a model card for a model you trained in the [AI/ML](../ai-ml/README.md) section.

### Phase 6 – Safety and harms from AI
- [ ] Misuse, hallucination and dual-use risks
- [ ] Red-teaming
- [ ] Staged rollouts and responsible release

🛠️ Project: red-team a chatbot for two hours and write a harms report with severity ratings.

### Phase 7 – Surveillance, security and power
- [ ] Facial recognition debates
- [ ] Data brokers
- [ ] Dark patterns in interfaces
- [ ] Responsible disclosure of security bugs

🛠️ Project: find five dark patterns in apps you use, and design an ethical alternative for each.

### Phase 8 – Misinformation and platforms
- [ ] Recommender systems and engagement optimisation
- [ ] Content moderation trade-offs
- [ ] Free expression vs harm

🛠️ Project: design a feed ranking that includes a wellbeing objective. Explain the trade-offs.

### Phase 9 – Labour, environment and access
- [ ] Data labelling work and its conditions
- [ ] Energy and water use of training and data centres
- [ ] The digital divide
- [ ] Accessibility (WCAG)

🛠️ Project: estimate the energy of training a model and of running it for a year. Write down every assumption.

### Phase 10 – Open source, licences and intellectual property
- [ ] Copyright for code and data
- [ ] Licences: MIT, Apache 2.0, GPL
- [ ] Training-data licensing debates
- [ ] Attribution

🛠️ Project: choose a licence for each of your repos and explain why.

### Phase 11 – Case studies
Read, discuss, and write one page per case:
- [ ] Therac-25 (radiation machine failures)
- [ ] Boeing 737 MAX (MCAS)
- [ ] Cambridge Analytica
- [ ] COMPAS recidivism scores
- [ ] Gender Shades (facial analysis accuracy)
- [ ] Dutch childcare benefits scandal
- [ ] Google Photos image-labelling error

🛠️ Project: write a one-page analysis of two cases, each using two frameworks from Phase 1.

### Phase 12 – Your ethics checklist
Before you ship anything, answer:
- [ ] Who is affected, including people who never use the product?
- [ ] What data is collected, and is each item necessary?
- [ ] Who can be harmed, and how badly?
- [ ] What happens when it fails?
- [ ] How can someone appeal or correct a decision?
- [ ] Who is accountable?

🛠️ Project: apply the checklist to a project from any section of this repo.
