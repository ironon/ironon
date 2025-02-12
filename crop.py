import os
from PIL import Image

def crop_to_square(image):
    """Crops the given image to a square with the size of the smallest dimension."""
    width, height = image.size
    min_dimension = min(width, height)
    left = (width - min_dimension) // 2
    top = (height - min_dimension) // 2
    right = left + min_dimension
    bottom = top + min_dimension
    return image.crop((left, top, right, bottom))

def process_images_in_folder(folder_path):
    """Processes all images in the given folder by cropping them to squares."""
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    # Supported image formats (you can add more formats if needed)
    supported_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(supported_extensions):
            try:
                with Image.open(file_path) as img:
                    cropped_img = crop_to_square(img)
                    cropped_img.save(file_path)  # Overwrite the original image
                    print(f"Processed: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    folder_path = "./"
    process_images_in_folder(folder_path)
