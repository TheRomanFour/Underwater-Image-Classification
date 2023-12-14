import os

def compare_images(image_folder, txt_file_path):
    with open(txt_file_path, 'r') as file:
        image_names = [line.strip() for line in file]
        

    classified_images = os.listdir(image_folder)
    print("Image Names from Text File:", image_names)
    print("Classified Images in Folder:", classified_images)
    common_images = set(image_names) & set(classified_images)
    
   

    return common_images

# Paths to folders and files
good_images_folder = r'D:\Ivan Faksic\Rijeka faks\Realizator\1. pitanje tim Grancigule\Projekt 2\data\Dobre'
bad_images_folder = r'D:\Ivan Faksic\Rijeka faks\Realizator\1. pitanje tim Grancigule\Projekt 2\data\Lose'
good_images_txt = r'D:\Ivan Faksic\Rijeka faks\Realizator\1. pitanje tim Grancigule\good_images.txt'
bad_images_txt = r'D:\Ivan Faksic\Rijeka faks\Realizator\1. pitanje tim Grancigule\bad_images.txt'

# Compare good images
common_good_images = compare_images(good_images_folder, good_images_txt)
print(f"Correctly classified good images: {len(common_good_images)}")

# Compare bad images
common_bad_images = compare_images(bad_images_folder, bad_images_txt)
print(f"Correctly classified bad images: {len(common_bad_images)}")
