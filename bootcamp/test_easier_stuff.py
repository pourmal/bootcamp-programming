#import easier_stuff


def experiment(exp_file):
    experiments = {}

    with open(exp_file, 'r') as f:
        for line in f.readlines()[1:]:
            fields = line.split('\t')

            for exp_index in range(0, len(fields) - 1):
                if exp_index not in experiments:
                    experiments[exp_index] = []
                experiments[exp_index].append((fields[0], float(fields[exp_index + 1])))

    return experiments


def test_experiment():
    values = experiment("test_data/test_experiments.txt")
    assert(len(values) == 3)
    assert(values[0] == [("gene1", 0.0), ("gene2", 1.0)])
    assert(values[1] == [("gene1", 0.1), ("gene2", 2.0)])
    assert(values[2] == [("gene1", 0.2), ("gene2", 3.0)])


test_experiment()