#!/usr/bin/python3
""" This modules has a script that adds all arguments provided to a\
python list, writes them on a file and svaes them there """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

try:
    args = load_from_json_file(filename)
except Exception:
    args = []
if len(sys.argv) - 1:
    idx = 1
    while idx < len(sys.argv):
        args.append(sys.argv[idx])
        idx += 1
save_to_json_file(args, filename)
