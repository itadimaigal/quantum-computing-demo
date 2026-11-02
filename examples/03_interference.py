"""Interference: one H gives 50/50, but two H gates in a row always give 0.

The second H makes the two paths to 1 cancel out and the two paths to 0 add up.
A normal random coin could never do this.
"""
import cirq

q = cirq.LineQubit(0)


def once():
    return cirq.Circuit(cirq.H(q), cirq.measure(q, key="m"))


def twice():
    return cirq.Circuit(cirq.H(q), cirq.H(q), cirq.measure(q, key="m"))


if __name__ == "__main__":
    sim = cirq.Simulator()
    print(sim.run(once(), repetitions=1000).histogram(key="m"))    # ~50/50
    print(sim.run(twice(), repetitions=1000).histogram(key="m"))   # Counter({0: 1000})
