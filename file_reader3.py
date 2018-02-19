#!/usr/bin/env python

import re
import json
import argparse

from pprint import pprint

"""
AARON     Jewish, English
From the given name AARON.
ABBEY     English
Indicated a person who lived near an abbey or worked in an abbey, from Middle English abbeye.
ABBOTT     English
"""


# "Aaron ['Jewish', 'English']
example = {
    "name": "Aaron",
    "origins": ['Jewish', 'English']
}


def surnames_extractor(filename):
    unique_origin = set()

    with open(filename, 'r') as a:
        data = []
        while True:
            line = a.readline()
            if line:
                words = (re.findall(r"[\w']+", line))
                if (words[0] == words[0].upper()):
                    roots = words[1:]
                    if len(roots[0]) < 3:
                        roots.remove(roots[0])
                        pass
                    data.append({
                        'name': words[0].capitalize(),
                        "origins": roots
                    })

                for i in range(0, len(roots)):
                    unique_origin.add(roots[i])

            if not line:
                break
    return data


def compose_result_name(entered_name):
    index = entered_name.find('.')
    new_str = entered_name[:index] + '.json'
    return new_str


def run(filename):
    data = surnames_extractor(filename)
    data_as_json = json.dumps(data, indent=2)

    with open(compose_result_name(entered_name), 'w') as b:
        b.write(data_as_json)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="exact file name")
    args = parser.parse_args()
    entered_name = args.filename

    filename = entered_name
    run(filename)
    #print(__name__)
