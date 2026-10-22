# Basics of Mathematics
## Student Workbook · 2026

Your fork is your workbook. Prepare notes you can read, understand and explain in class.

[Open Student Workbook](https://github.com/aliev-ibra/Basics_of_Mathematics_Student_Workbook_2026)

Course guide: what a good mathematical note looks like — https://student-introduction-229985.gitlab.io/#notes-quality

## Course at a glance

| Group | Topic sets | Folder |
|---|---|---|
| Algebra | Matrices and operations · Determinants · Matrix inversion · Systems of equations | `exercises/1_Algebra/` |
| Geometry | Vectors · Lines and planes · Second-degree curves and surfaces | `exercises/2_Geometry/` |
| Calculus | Limits · Derivatives · Function analysis · Integrals · Applications | `exercises/3_Calculus/` |

There are 12 topic sets. Exercises live in `exercises/<group>/<set>_en.md`; each exercise has one answer file `solutions/<group>/<set>/problem_XX_solution.md`.

## How this course works

1. Open an exercise (read the task in `exercises/`).
2. Prepare the solution (mathematics, books, AI and course tools).
3. Write a readable note (complete the matching file in `solutions/`).
4. Read it yourself (if you do not understand your own note, it is not finished).
5. Commit and sync.
6. Present and discuss.

> NOT THIS: `exercise → AI → copy → paste → submit`
> THIS: `exercise → tools → understandable note → read → learn → explain`

## Step 1 — Fork the workbook

Minimum requirement: you must own your own fork of the workbook; you never edit the instructor's repository.

1. Open the instructor's repository and click Fork: [dchorazkiewicz/Basics_of_Mathematics_Student_Workbook_2026](https://github.com/dchorazkiewicz/Basics_of_Mathematics_Student_Workbook_2026)
2. Choose your account, leave the repository name unchanged, keep the "Copy the main branch" option selected and click Create fork.
3. Check that the owner at the top is now your GitHub username.
4. Enable Issues: Settings → General → Features → Issues.

Issues are used by the instructor for comments about your work (what needs completing, correcting or improving) and are NOT used for grades — grades come in class or by email. Do not create Pull Requests to the original repository unless the instructor explicitly requests it.

## The quality rule — what makes a note acceptable

| # | Version | Verdict |
|---|---|---|
| 01 | Result only | RETURNED — not accepted |
| 02 | Some calculations, almost no reading | RETURNED — not accepted |
| 03 | Readable complete solution | ACCEPTED |
| 04 | Study note: explanation, meaning, check, and presentation | STRONG / PREFERRED |

Why 01 and 02 fail: the original question is missing, there is no explanation of where the result came from, the reader cannot tell why the excluded cases were excluded, and there is nothing the student could explain in class.

Notes 01 and 02 come back for rewriting; notes 03 and 04 are acceptable. A solution does not have to be extremely long — it does have to contain enough language that a human reader can follow the reasoning.

What "accepted" means: the mathematics is correct, the reasoning is understandable, the note contains enough explanation, and you can read it yourself and explain it in class.

## The required structure of every solution note

1. the original problem
2. a short explanation of what we are trying to find
3. the idea or theorem needed before the calculation
4. a step-by-step solution
5. one or two sentences explaining WHY each important step is valid
6. the final answer in words
7. a quick verification
8. common mistakes
9. a short 3-sentence explanation I could say aloud in class

```markdown
# Problem NN

## The original problem

## What we are looking for

## The idea we need

## Step-by-step solution

## Why each step is valid

## Final answer (in words)

## Verification

## Common mistakes

## How I would explain it in class
```

## Rules for writing a note

- No unexplained chains of formulas; if you use a symbol, the surrounding text must tell the reader what it means.
- Every important step carries one or two sentences of justification.
- The final answer is stated in words as well as in symbols.
- Write for a first-year reader with short sentences and defined terms.
- Before you commit, read your note once and rewrite any line you could not explain aloud.

## Markdown and mathematics

| Syntax | Result |
|---|---|
| `#` | heading |
| `##` | section |
| `**bold**` | bold |
| `*italic*` | italic |
| `-` | list |
| `[text](url)` | link |
| `` `code` `` | inline code |
| `\|` | table |
| `$...$` | inline math |
| `$$...$$` | display math |

Example:

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

Markdown itself has no maths; platforms render with KaTeX or MathJax, so support differs between systems.

## Using AI — ask for a note, not for an answer

Do not prompt "give me the answer to problem 11". Ask for a readable study note instead.

```
Prepare a readable Markdown study note for a first-year student.

Include:
1. the original problem,
2. a short explanation of what we are trying to find,
3. the idea or theorem needed before the calculation,
4. a step-by-step solution,
5. one or two sentences explaining WHY each important step is valid,
6. the final answer in words,
7. a quick verification,
8. common mistakes,
9. a short 3-sentence explanation I could say aloud in class.

Do not give me unexplained chains of formulas.
If you use a symbol, make sure the surrounding text tells me what it means.

Before you commit:
Read your own note from top to bottom once. If there is a line you could not explain aloud, ask the AI to rewrite that part more simply.
```

AI output is a draft: read it, revise anything you do not understand, and you are responsible for the note.

## Tools

### GitHub in the browser (github.dev)

Press `.` on a repository page, or change the URL from github.com to github.dev, to open the repository in the browser editor. In the Explorer, open the matching file under `solutions/` and edit the Markdown. Then open the Source Control view, write a commit message and press Commit & Push. Work that is not committed in the browser is easy to lose.

### Desktop VS Code

Use Source Control → Clone Repository, paste the URL to clone your own fork: <https://github.com/aliev-ibra/Basics_of_Mathematics_Student_Workbook_2026>, and choose a local folder. Edit the Markdown file in that folder. Use the Markdown preview (Ctrl+K, then V) to check how the note renders. Then use Source Control → Commit Changes → Sync Changes.

In the web editor you may see "Commit & Push" while desktop VS Code shows "Sync Changes"; the goal is the same — committed work reaching your fork.

### VS Code agents (GitHub Copilot, OpenAI Codex, Claude Code, Google Antigravity)

Clone the repository as described above, install ONE agent from Extensions and sign in. Paste the exercise in normal language and let the agent prepare the note, then read it and improve what you could not explain yourself. The agent must not commit or sync the changes until you ask it to. Do not paste passwords, API keys, bank data, or other secrets into the agent.

## Commit and sync

Commit regularly (uncommitted work in the browser is easy to lose), write a short meaningful message, push to your own fork, and never commit into the instructor's repository.

## Before you commit — checklist

- [ ] The original question is visible in the note.
- [ ] Every formula is surrounded by explanation.
- [ ] You know what the final conclusion means.
- [ ] You could explain every line aloud.
- [ ] You read the note from top to bottom once.

## Course credit

1. All workbook exercises are completed in your fork.
2. The solutions are accepted — a note is readable enough to learn from and explain.
3. You understand your own work — if you cannot read or explain your own note, it needs improvement.

By the end of the course, your fork should contain notes that you created, improved, read, discussed and can return to later. Your repository should become your own mathematics textbook.
