import os
from random import Random


class PasswordGenerator:
    DEFAULT_LENGTH = 18
    DEFAULT_SEED = 'MySecretSeed'

    _SYMBOLS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # NOQA
    _SPECIAL_SYMBOLS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    def __init__(self,
                 *code_phrases,
                 length=None,
                 seed=None,
                 use_special_symbols=None):
        self._code_phrases = code_phrases
        self._length = length or os.getenv('PGEN_LENGTH', self.DEFAULT_LENGTH)
        self._seed = seed or os.getenv('PGEN_SEED', self.DEFAULT_SEED)

        if isinstance(use_special_symbols, bool):
            self._use_special_symbols = use_special_symbols
        elif isinstance(use_special_symbols, str):
            self._use_special_symbols = use_special_symbols.lower() in ('1', 'true')
        else:
            self._use_special_symbols = os.getenv('PGEN_USE_SPECIAL_SYMBOLS', True)

        self._random = Random(self.seed)

    @property
    def seed(self):
        """Generate seed based on default seed and code phases"""
        return '-'.join(self._code_phrases) + self._seed * 2 + '-'.join(self._code_phrases)

    @property
    def symbols(self):
        return self._SYMBOLS + self._SPECIAL_SYMBOLS if self._use_special_symbols else self._SYMBOLS

    def generate(self):
        if self._seed == self.DEFAULT_SEED:
            print('\033[93m' + 'Warning: You are using the default SEED.')

        return ''.join(self._random.choice(self.symbols) for _ in range(self._length))


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate the passwords.')

    parser.add_argument('-length', '-len', '-l', type=int,
                        default=PasswordGenerator.DEFAULT_LENGTH,
                        help='length of password')
    parser.add_argument('-seed', '-s', type=str, default=None,
                        help='secret key to generate unique passwords')
    parser.add_argument('-special_symbols', '-ss', choices=('0', '1'), default=None,
                        help='use special symbols like "!#$./:;" etc.')
    parser.add_argument('code_phrases', metavar='CodePhrases', nargs='+', type=str)

    args = parser.parse_args()

    generator = PasswordGenerator(*args.code_phrases,
                                  length=args.length,
                                  seed=args.seed,
                                  use_special_symbols=args.special_symbols)

    print('\033[92m' + 'Your password:' + '\033[0m' + '\033[1m', generator.generate())


if __name__ == '__main__':
    main()
