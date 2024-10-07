import argparse
import logging
import json
import re
from pathlib import Path


HANGUL_ENG_LANG_PACK="[\uAC00-\uD7A3|\u0021-\u007E|1-9|\n]+"

def main(args):

    unique_mark_symbols = set()

    for file in args.dir.glob('**/text'):
        with open(file, 'r') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            remains = re.sub(HANGUL_ENG_LANG_PACK, '', line)
            unique_mark_symbols.update(list(remains))

    logging.info(unique_mark_symbols)

    json.dump(list(unique_mark_symbols), 'unique_mark_symbols.json', ensure_ascii=False, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir',
                        type=Path)
    args = parser.parse_args()

    if not isinstance(args.dir, Path):
        args.dir = Path(args.dir)

    main(args)
