from tachyon_manifolds import TachyonManifolds

print('Solving first part of puzzle')
tachyon_manifolds = TachyonManifolds()
tachyon_manifolds.load_diagram('input.raw')
tachyon_manifolds.turn_beam_on()
print(f'Answer to first part of puzzle is: {tachyon_manifolds.beam_splits}')
