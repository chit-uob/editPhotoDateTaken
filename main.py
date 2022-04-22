import configparser

# Get the source and destination folder
# todo when use rename sample_config.ini to config.ini
config = configparser.ConfigParser()
config.read('config.ini')
SOURCE_FOLDER = config['MAIN']['sourceFolder']
DESTINATION_FOLDER = config['MAIN']['destinationFolder']


def main():
    print(SOURCE_FOLDER)
    print(DESTINATION_FOLDER)


if __name__ == '__main__':
    main()
