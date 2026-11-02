"""Grover's search on 2 qubits: find the one "marked" answer out of 4 in a single step.

1. H on both qubits: an equal blend of 00, 01, 10, 11.
2. Oracle: flips the phase (the sign) of the marked answer only.
3. Diffusion: interference boosts the marked answer and cancels the rest.
With 2 qubits, one round is enough: the marked answer comes out 100% of the time.
"""
import cirq

MARKED = (1, 0)   # the answer we are searching for; try changing it


def grover_circuit(marked=MARKED):
    a, b = qubits = cirq.LineQubit.range(2)
    flip = [cirq.X(q) for q, bit in zip(qubits, marked) if bit == 0]
    return cirq.Circuit(
        cirq.H.on_each(qubits),                      # 1. equal blend
        flip, cirq.CZ(a, b), flip,                   # 2. oracle: mark the answer with a minus sign
        cirq.H.on_each(qubits), cirq.X.on_each(qubits),
        cirq.CZ(a, b),
        cirq.X.on_each(qubits), cirq.H.on_each(qubits),  # 3. diffusion: amplify the marked answer
        cirq.measure(a, b, key="found"),
    )


if __name__ == "__main__":
    circuit = grover_circuit()
    print(circuit)
    result = cirq.Simulator().run(circuit, repetitions=1000)
    found = result.histogram(key="found", fold_func=lambda bits: "".join(map(str, bits)))
    print(found)   # Counter({'10': 1000})
