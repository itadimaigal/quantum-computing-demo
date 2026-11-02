"""Superposition: one qubit as a spinning coin.

An H (Hadamard) gate turns |0> into a 50/50 blend of 0 and 1.
Measuring it many times gives roughly half 0s and half 1s.
"""
import cirq


def coin_circuit():
    q = cirq.LineQubit(0)
    return cirq.Circuit(
        cirq.H(q),                    # spin the coin
        cirq.measure(q, key="m"),     # look at it: the blend becomes 0 or 1
    )


if __name__ == "__main__":
    circuit = coin_circuit()
    print(circuit)
    result = cirq.Simulator().run(circuit, repetitions=1000)
    print(result.histogram(key="m"))   # e.g. Counter({1: 506, 0: 494})
