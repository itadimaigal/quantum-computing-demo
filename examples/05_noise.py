"""Why error correction matters: the Bell state on a noisy simulated chip.

Real qubits make mistakes. Adding depolarizing noise (a small chance of a random error
after every gate) makes the "impossible" results 01 and 10 start to appear.
"""
import cirq

from importlib import import_module

bell_circuit = import_module("02_bell").bell_circuit


def run(noise_level, repetitions=2000):
    circuit = bell_circuit()
    if noise_level:
        circuit = circuit.with_noise(cirq.depolarize(p=noise_level))
    result = cirq.DensityMatrixSimulator(seed=7).run(circuit, repetitions=repetitions)
    return result.histogram(key="result")


if __name__ == "__main__":
    for p in (0.0, 0.01, 0.05, 0.15):
        counts = run(p)
        wrong = counts[1] + counts[2]   # 01 and 10 should never happen
        print(f"noise {p:>4}: {dict(sorted(counts.items()))}  wrong answers: {wrong / 2000:.1%}")
