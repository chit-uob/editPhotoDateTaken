from pathlib import Path
from exif import Image as ExifImage
from PIL import Image as PilImage

target_image = Path(r"D:\All photos\PhotoOrganizer\UnknownDateTaken\Screenshot_20200229-010435.jpg")

pil_image = PilImage.open(target_image)
pil_image = pil_image.convert("RGB")

print(target_image.suffix == ".jpg")

with open(target_image, "wb") as test_file:
    pil_image.save(test_file)

with open("test.jpg", "rb") as image_file:
    data = ExifImage(image_file)
    data.list_all()
#
# with open(target_image, "rb") as image_file:
#     data = ExifImage(image_file)
