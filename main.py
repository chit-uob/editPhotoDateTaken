import configparser
import traceback
from pathlib import Path
import re
from exif import Image as ExifImage
from PIL import Image as PilImage


import logging
from datetime import datetime

logging.basicConfig(filename=f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log", level=logging.DEBUG)


# Get the source and destination folder
# todo when use rename sample_config.ini to config.ini
config = configparser.ConfigParser()
config.read('config.ini')
try:
    SOURCE_FOLDER = Path(config['MAIN']['sourceFolder'])
    DESTINATION_FOLDER = Path(config['MAIN']['destinationFolder'])
except Exception:
    logging.warning("Faced exception when parsing the config:")
    logging.warning(traceback.format_exc())
    raise SystemExit(-1)



def date_finder(filename):
    if re.match("^IMG-[0-9]{8}-WA[0-9]{4}", filename):
        year = filename[4:8]
        month = filename[8:10]
        day = filename[10:12]
    elif re.match("^Screenshot_[0-9]{8}-[0-9]{6}_", filename):
        year = filename[11:15]
        month = filename[15:17]
        day = filename[17:19]
    elif re.match("^RDT_[0-9]{8}_", filename):
        year = filename[4:8]
        month = filename[8:10]
        day = filename[10:12]
    else:
        year = "0000"
        month = "00"
        day = "00"
    return year, month, day


def handle_file(file, year, month, day):
    logging.debug(f"handling {file}")
    try:
        with open(file, "rb") as image_file:
            data = ExifImage(image_file)
            logging.debug(f"successfully copied image data")
        data.datetime_original = f"{year}:{month}:{day} 00:00:00"
        # print(f"will change {file.name} with {data.datetime_original}")
        with open(file, "wb") as image_file:
            image_file.write(data.get_file())
            logging.debug(f"successfully replaced image file with metadata")

        # Move the file with pathlib
        # print(f'will move to {DESTINATION_FOLDER.joinpath(f"{year}/{month}/{year}_{month}_{day}/{file.name}")}')
        DESTINATION_FOLDER.joinpath(f"{year}/{month}/{year}_{month}_{day}/").mkdir(parents=True, exist_ok=True)
        logging.debug(f'successfully created dir {DESTINATION_FOLDER.joinpath(f"{year}/{month}/{year}_{month}_{day}/")}')
        if not DESTINATION_FOLDER.joinpath(f"{year}/{month}/{year}_{month}_{day}/{file.name}").exists():
            logging.debug("file does not already exist, moving file to target")
            file.rename(DESTINATION_FOLDER.joinpath(f"{year}/{month}/{year}_{month}_{day}/{file.name}"))
        else:
            logging.debug("file already exist, adding suffix and moving file to target")
            file.rename(DESTINATION_FOLDER.joinpath(f"{year}/{month}/{year}_{month}_{day}/{file.stem}_dup{file.suffix}"))
    except:
        # logging.warning("faced problem handling file, will try the other method")
        # logging.warning(traceback.format_exc())
        # try:
        #     pil_image = PilImage.open(file)
        #     copied_image = pil_image.copy()
        #     with open(file.parent.joinpath(f"{file.stem}_cpy{file.suffix}"), "wb") as write_file:
        #         copied_image.save(write_file)
        #
        # except:
        #     logging.warning("second method failed too")
        #     logging.warning(traceback.format_exc())
        return


def main():
    logging.debug(f"The source folder is {SOURCE_FOLDER}")
    logging.debug(f"The destination folder is {DESTINATION_FOLDER}")
    input()

    # handle_file(Path(r'D:\All photos\Welcome Scan.jpg'), "2004", "04", "09")

    for file in SOURCE_FOLDER.iterdir():
        year, month, day = date_finder(file.name)
        if year != "0000":
            handle_file(file, year, month, day)



if __name__ == '__main__':
    main()
