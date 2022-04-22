import configparser
import traceback
from pathlib import Path

# Get the source and destination folder
# todo when use rename sample_config.ini to config.ini
config = configparser.ConfigParser()
config.read('config.ini')
try:
    SOURCE_FOLDER = Path(config['MAIN']['sourceFolder'])
    DESTINATION_FOLDER = Path(config['MAIN']['destinationFolder'])
except Exception:
    print("Faced exception when parsing the config:")
    print(traceback.format_exc())
    raise SystemExit(-1)


def main():
    print(f"The source folder is {SOURCE_FOLDER}")
    print(f"The destination folder is {DESTINATION_FOLDER}")


if __name__ == '__main__':
    main()
