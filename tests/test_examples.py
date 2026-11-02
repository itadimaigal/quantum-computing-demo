import sys
from importlib import import_module
from pathlib import Path

import cirq

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "examples"))
coin = import_module("01_coin")
bell = import_module("02_bell")
interference = import_module("03_interference")
grover = import_module("04_grover")
noise = import_module("05_noise")

SIM = cirq.Simulator(seed=42)


def test_coin_is_roughly_fifty_fifty():
    counts = SIM.run(coin.coin_circuit(), repetitions=2000).histogram(key="m")
    assert 800 < counts[0] < 1200 and counts[0] + counts[1] == 2000


def test_bell_only_gives_00_or_11():
    counts = SIM.run(bell.bell_circuit(), repetitions=2000).histogram(key="result")
    assert set(counts) <= {0, 3} and min(counts[0], counts[3]) > 800


def test_two_hadamards_always_give_zero():
    counts = SIM.run(interference.twice(), repetitions=1000).histogram(key="m")
    assert counts == {0: 1000}


def test_grover_finds_every_marked_answer():
    for marked in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        counts = SIM.run(grover.grover_circuit(marked), repetitions=200).histogram(key="found")
        assert counts == {marked[0] * 2 + marked[1]: 200}


def test_noise_creates_impossible_results():
    assert noise.run(0.0)[1] + noise.run(0.0)[2] == 0
    noisy = noise.run(0.1)
    assert noisy[1] + noisy[2] > 0
