import os

from PIL import Image, ImageOps

def pad_to_square(image):
    """Pads the given image with white bars to make it square."""
    width, height = image.size
    max_dimension = max(width, height)

    # Ensure the image has an alpha channel for transparency
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    # Calculate padding for each side
    pad_left = (max_dimension - width) // 2
    pad_right = max_dimension - width - pad_left
    pad_top = (max_dimension - height) // 2
    pad_bottom = max_dimension - height - pad_top

    # Pad the image with transparent padding
    padding = (pad_left, pad_top, pad_right, pad_bottom)
    return ImageOps.expand(image, padding, fill=(0, 0, 0, 0)) 


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
                    cropped_img = pad_to_square(img)
                    cropped_img.save(file_path)  # Overwrite the original image
                    print(f"Processed: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    folder_path = "./"
    process_images_in_folder(folder_path)
