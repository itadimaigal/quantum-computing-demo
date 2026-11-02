"""Entanglement: the Bell state, the "two magic coins" from the video.

H puts qubit a in superposition, CNOT links b to a.
Results are 00 or 11 (shown as 0 and 3), never 01 or 10.
"""
import cirq


def bell_circuit():
    a, b = cirq.LineQubit.range(2)    # two qubits, both start at 0
    return cirq.Circuit(
        cirq.H(a),                    # spin the coin: a is 50/50
        cirq.CNOT(a, b),              # entangle b with a
        cirq.measure(a, b, key="result"),
    )


if __name__ == "__main__":
    circuit = bell_circuit()
    print(circuit)
    result = cirq.Simulator().run(circuit, repetitions=1000)
    print(result.histogram(key="result"))   # e.g. Counter({3: 507, 0: 493})  (3 = binary 11)
