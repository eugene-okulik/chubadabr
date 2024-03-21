import os
import argparse
import pathlib
import collections

from functions import make_me_dict, date_search, text_search, printer

parser = argparse.ArgumentParser()
parser.add_argument("path", nargs='+', type=pathlib.Path, help="File name")
parser.add_argument("--date", help='''Search date "2022-02-03 00:51:29.616/.." / "../2022-02-03 00:51:29.616"
                    "2022-02-03 00:51:29.616/2022-02-03 01:51:29.616" / "2022-02-03 00:51:29.616" ''')
parser.add_argument("--text", help="Text to search")
parser.add_argument("--full", help="Get full message for strict date", action="store_true")
parser.add_argument("--notext", help="Should not contain this text")
args = parser.parse_args()
path = args.path[-1]
date = args.date
text = args.text
notext = args.notext
full = args.full
logs = collections.defaultdict()
# собрали словарь
if os.path.isdir(path):
    for file in [f for f in pathlib.Path(path).iterdir()]:
        print("Processing file:", file)
        logs = make_me_dict(file, logs)
else:
    logs = make_me_dict(path, logs)
# запустили поиск
if date:
    logs = date_search(logs, date)
if text or notext:
    logs = text_search(logs, text, notext)

printer(logs, full, text)
