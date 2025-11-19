from nuclear_reactor import NuclearReactor

print('Solving first part of puzzle')
nuclear_reactor = NuclearReactor()
nuclear_reactor.load_molecule('input.raw')
nuclear_reactor.fuse()
print(f'Answer to first part of puzzle is: {len(nuclear_reactor.output)}')
