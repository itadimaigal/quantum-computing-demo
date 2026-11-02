# Quantum Computing Demo (Python + Cirq)

Code from the itadimaigal video **"Quantum Computing Made Simple + Google's Willow Quantum Chip"**.
Every example runs on a simulator on your own laptop. You don't need a quantum computer.

## Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Examples

| File | Idea | What you'll see |
|---|---|---|
| `examples/01_coin.py` | **Superposition** | One H gate: about 50% 0s, 50% 1s |
| `examples/02_bell.py` | **Entanglement** (shown in the video) | Only 00 and 11 (printed as 0 and 3), never 01 or 10 |
| `examples/03_interference.py` | **Interference** (shown in the video) | One H gives 50/50, but two H gates give 0 every time |
| `examples/04_grover.py` | **Grover's search** | Finds the marked answer out of 4 in one step, 100% of the time |
| `examples/05_noise.py` | **Why error correction matters** | With noise, the "impossible" 01 and 10 start to appear |

Run one:

```bash
python examples/02_bell.py
```

Example output:

```
0: ───H───@───M('result')───
          │   │
1: ───────X───M─────────────
Counter({0: 504, 3: 496})
```

Results are counted as numbers: `0` = `00`, `3` = `11` in binary. Your counts will differ slightly because measurement is random.

## Tests

```bash
pytest -q
```

GitHub Actions (`.github/workflows/ci.yml`) runs the tests and every example on Python 3.11 and 3.13 on every push.

## Try this next

- In `04_grover.py`, change `MARKED = (1, 0)` to another answer and run it again.
- In `05_noise.py`, watch the wrong answers grow as the noise grows. Fixing this is what Google's Willow chip demonstrated with error correction.
- Learn more: [Cirq docs](https://quantumai.google/cirq) · [Google Quantum AI](https://quantumai.google)

---
📺 YouTube: **itadimaigal**, Slaves of IT. Learn. Build. Break free.
