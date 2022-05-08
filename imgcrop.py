from PIL import Image
import pathlib
for input_img_path in pathlib.Path("C:\\Users\\Mysm\\Desktop\\images").iterdir():
    output_img_path = str(input_img_path).replace("C:\\Users\\Mysm\\Desktop\\images",r"C:\Users\\Mysm\\Desktop\\cimages")
    with Image.open(input_img_path) as im:
        width, height = im.size   # Get dimensions
        left = 0
        top = 0
        right = width
        bottom = height-110
        cimage=im.crop((left, top, right, bottom))
        cimage.save(output_img_path, "JPEG")
        #cimage.show()
        print(f"processing file {input_img_path} done...")    