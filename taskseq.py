import argparse
from typing import List, Tuple
import taskw


DELIMETER_PARALLELL = ','
DELIMETER_SEQUENTIAL = '--'


def get_args():
    """ Get commandline arguments """
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        'sequence',
        help='specify the depencency sequence. ' +
        f'2{DELIMETER_SEQUENTIAL}3 means 3 will depend on 2. ' +
        f'1{DELIMETER_PARALLELL}2{DELIMETER_SEQUENTIAL}3{DELIMETER_PARALLELL}4 ' +
        'means 3 and 4 will both depend on 1 and 2.'
    )
    argparser.add_argument(
        '--config',
        help='Used to specify an alternate path for the taskwarrior config file'
    )
    return argparser.parse_args()


def run():
    args = get_args()
    tw = taskw.TaskWarriorShellout(
        **(dict(config_filename=args.config) if args.config else {})
    )

    # Parsing
    sequence: List[List[str]] = [
        s.split(DELIMETER_PARALLELL)
        for s in args.sequence.split(DELIMETER_SEQUENTIAL)
    ]

    # [ (group 1, group 2), (group 2, group 3), and so on... ]
    neighbours: List[Tuple[List[str]]] = zip(sequence[:-1], sequence[1:])
    for dependencies, dependers in neighbours:
        depends_uuids: str = ','.join([
            tw.get_task(id=task)[1]['uuid']
            for task in dependencies
        ])
        for depender_id in dependers:
            _, depender = tw.get_task(id=depender_id)
            depender['depends'] = depends_uuids
            tw.task_update(depender)
            print(f'updated {depender_id}')


if __name__ == '__main__':
    run()
