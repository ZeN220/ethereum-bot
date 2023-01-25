from mnemonic import Mnemonic


def validation_seeds(seeds: list[str]) -> list[str]:
    mnemonic = Mnemonic("english")
    valid_seeds = []
    for seed in seeds:
        if mnemonic.check(seed):
            valid_seeds.append(seed)
    return valid_seeds
