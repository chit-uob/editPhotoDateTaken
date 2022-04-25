import configparser
from pathlib import Path
import re

config = configparser.ConfigParser()
config.read('config.ini')
SOURCE_FOLDER = Path(config['MAIN']['sourceFolder'])

#regexs
regexs = {"^IMG-[0-9]{8}-WA[0-9]{4}": "IMG-20211202-WA0002.jpg",
"^Screenshot_[0-9]{8}-[0-9]{6}": "Screenshot_20200917-150424_FD.jpg",
"^RDT_[0-9]{8}_": "RDT_20210529_1139097980871380979846723.jpg"}


regex = "IMG-[0-9]{8}-WA[0-9]{4}"
regex_compiled = re.compile(regex)

for file in SOURCE_FOLDER.iterdir():
    if regex_compiled.match(file.name):
        print(file.name)