from tachyon_manifolds import TachyonManifolds


def test_tachyon_manifolds():
    tachyon_manifolds = TachyonManifolds()
    tachyon_manifolds.load_diagram('test_input.raw')
    tachyon_manifolds.turn_beam_on()
    assert tachyon_manifolds.beam_splits == 21
