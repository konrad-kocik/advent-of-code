from tachyon_manifolds import TachyonManifolds, QuantumTachyonManifolds


def test_tachyon_manifolds():
    tachyon_manifolds = TachyonManifolds()
    tachyon_manifolds.load_diagram('test_input.raw')
    tachyon_manifolds.turn_beam_on()
    assert tachyon_manifolds.beam_splits == 21



def test_quantum_tachyon_manifolds():
    quantum_tachyon_manifolds = QuantumTachyonManifolds()
    quantum_tachyon_manifolds.load_diagram('test_input.raw')
    quantum_tachyon_manifolds.turn_beam_on()
    assert quantum_tachyon_manifolds.timelines == 40
