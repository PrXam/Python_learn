import argparse
import os
import tempfile
import json


parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--value', default=None)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), "storage.data")
try:
    with open(storage_path, "r") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = {}
except FileNotFoundError:
    data = {}
with open(storage_path, "w") as f:
    if args.value is None:
        if args.key in data.keys():
            print(', '.join(data[args.key]))
        else:
            print(None)
    elif args.key in data.keys():
        data[args.key].append(args.value)
    else:
        data[args.key] = [args.value]
    json.dump(data, f)

