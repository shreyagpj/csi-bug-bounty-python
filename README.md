# Bug Bounty: Library Management System

Welcome to Bug Bounty! You've inherited a small **Library Management
System** written in Python. It mostly works... but it's hiding **9 bugs**
across three difficulty levels:

| Level  | Count | Points each |
|--------|-------|-------------|
| Easy   | 3     | 10          |
| Medium | 3     | 20          |
| Hard   | 3     | 30          |

**Total possible score: 180**

## The codebase

```
models.py        -> Book and Member data classes
inventory.py      -> Library: add/remove/search books, check availability
members.py        -> MembershipManager: register members, calculate fines
transactions.py   -> TransactionManager: borrow/return books, reports
main.py            -> a demo script that runs the whole system
```

The system models a simple real-world workflow:

1. A `Library` stocks `Book`s.
2. A `MembershipManager` registers `Member`s.
3. A `TransactionManager` lets members borrow and return books, and
   charges a fine for late returns.

## How to play

1. Run the demo:
   ```
   python main.py
   ```
   Read the output carefully. Several lines print what the value
   **should** be right next to what it **actually** is — if they
   don't match, you've found a symptom of a bug.
2. Read the source code. Some bugs don't show up in the default demo
   run at all — you'll only catch them by reasoning about the code
   (or by writing your own test scenario).
3. For each bug you find, submit:
   - The file and line(s) where it lives
   - A one-line description of what's wrong
   - A one-line fix (a code suggestion is enough, you don't need to
     submit a patch)

## Scoring guidance for judges

- **Easy**: bug is visible just by reading a function, or shows up
  directly in the demo output.
- **Medium**: bug requires tracing how a value flows between two or
  more functions/objects, or noticing a subtly wrong result.
- **Hard**: bug depends on a Python-specific gotcha (mutability,
  aliasing, shared state, class vs. instance attributes) and requires
  understanding *why*, not just *that*, something is wrong.

Good luck, and happy hunting!
