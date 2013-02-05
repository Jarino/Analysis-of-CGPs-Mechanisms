import sys
from subprocess import call


def generator():
    for problem in ['encode', 'decode', 'multiply', 'parity']:
        for ordering in ['normal', 'reorder', 'dag']:
            for nodes in [50, 100, 200, 500, 1000, 2000, 5000, 10000]:
                yield problem, 'single', ordering, nodes, 1
                for duplicate in ['skip', 'accumulate']:
                    for mut in [0.05, 0.02, 0.01, 0.005,
                                0.002, 0.001, 0.0005, 0.0002]:
                        yield problem, duplicate, ordering, nodes, mut

seed = sys.argv[1]
to_add = int(sys.argv[2])
complete = int(sys.argv[3])
added = 0

for index, config in enumerate(generator()):
    if index >= complete:
        command = ['./runone.sh'] + map(str, config) + [seed]
        if call(command):
            print "NON ZERO!"
        added += 1
        if added >= to_add:
            break
print index + 1