from pytest import fixture

from tachyon_manifolds import TachyonManifolds


@fixture
def tachyon_manifolds():
    tm = TachyonManifolds()
    tm.load_diagram('test_input.raw')
    return tm


def test_tachyon_manifolds(tachyon_manifolds: TachyonManifolds):
    tachyon_manifolds.turn_beam_on()
    assert tachyon_manifolds.beam_splits == 21
    assert tachyon_manifolds.timelines == 1


def test_tachyon_manifolds_with_quantum_physics(tachyon_manifolds: TachyonManifolds):
    tachyon_manifolds.quantum_physics = True
    tachyon_manifolds.turn_beam_on()
    assert tachyon_manifolds.beam_splits == 21
    assert tachyon_manifolds.timelines == 40
    