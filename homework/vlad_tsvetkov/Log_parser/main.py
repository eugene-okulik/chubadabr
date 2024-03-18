import os
import argparse
import pathlib
import collections

from functions import make_me_dict, date_search, text_search

parser = argparse.ArgumentParser()
parser.add_argument("path", nargs='+', type=pathlib.Path, help="File name")
parser.add_argument("--date", help='''Search date "2022-02-03 00:51:29.616/.." / "../2022-02-03 00:51:29.616"
                    "2022-02-03 00:51:29.616/2022-02-03 01:51:29.616" / "2022-02-03 00:51:29.616" ''')
parser.add_argument("--text", help="Text to search")
parser.add_argument("--notext", help="Should not contain text", action="store_true")
args = parser.parse_args()
path = args.path[-1]
date = args.date
text = args.text
notext = args.notext

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
    date_search(logs, date)
elif text:
    text_search(logs, text, notext)
