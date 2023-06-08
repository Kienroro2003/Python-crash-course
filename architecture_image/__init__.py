from PIL import Image
import os
import shutil
FOLDER_HORIZONTAL = "/Users/kienroro2003/Downloads/Hinh horizontal/"
FOLDER_VERIZONTAL = "/Users/kienroro2003/Downloads/Hinh verizontal/"
folder_path = "/Users/kienroro2003/Downloads/20230607 MJ Collection2"
file_list = os.listdir(folder_path)
print(file_list)
count = 1;
for file in file_list[1:]:
    original_path = f"{folder_path}/{file}"
    print(f"{count}/{len(file_list)} with path: {original_path}")
    count = count + 1
    image = Image.open(original_path)
    width, height = image.size
    ratio = width / height
    if ratio > 1:
        shutil.move(original_path, f"{FOLDER_HORIZONTAL}{file}")
    else:
        shutil.move(original_path, f"{FOLDER_VERIZONTAL}{file}")

print("Finished!!!")


