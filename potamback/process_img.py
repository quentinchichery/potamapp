from PIL import Image
import os

def create_thumbnails(input_folder, output_folder, thumbnail_size=(800, 600)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        print(filename)
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            # Open the image
            with Image.open(input_path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                # Create a thumbnail (resized) image
                img.thumbnail(thumbnail_size)
                # Save the thumbnail image to the output folder
                img.save(output_path)

if __name__ == "__main__":
    input_folder = "potamback/pictures"
    output_folder = "potamfront/public"
    thumbnail_size = (600, 600)

    create_thumbnails(input_folder, output_folder, thumbnail_size)
