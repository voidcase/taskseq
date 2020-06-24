#!/usr/bin/env python3
"""
Use like this:
    taskseq 1,2,3>4,5>6
"""

import taskw
import argparse

if __name__ == '__main__':

    DELIMETER_PARALLELL = ','
    DELIMETER_SEQUENTIAL = '--'

    # Setup
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
    args = argparser.parse_args()
    tw = taskw.TaskWarriorShellout(**(dict(config_filename=args.config) if args.config else {}))

    # Parsing
    seqstr: str = args.sequence
    ast = [s.split(DELIMETER_PARALLELL) for s in seqstr.split(DELIMETER_SEQUENTIAL)]

    # Executing
    pairs = zip(ast[:-1], ast[1:]) # [ (group 1, group 2), (group 2, group 3), and so on... ]
    for dependencies, dependers in pairs:
        depends_uuids: str = ','.join([tw.get_task(id=task)[1]['uuid'] for task in dependencies])
        for depender_id in dependers:
            _, depender = tw.get_task(id=depender_id)
            depender['depends'] = depends_uuids
            tw.task_update(depender)
            print(f'updated {depender_id}')
