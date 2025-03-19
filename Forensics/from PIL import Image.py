import cv2
import os
import numpy as np
from PIL import Image

def extract_coordinates_from_metadata(image_path):
    """
    Extract the (x, y) coordinates from the metadata of the PNG file.

    :param image_path: Path to the PNG file.
    :return: Tuple of (x, y) coordinates extracted from the metadata.
    """
    image_pil = Image.open(image_path)
    metadata = image_pil.text  # Get metadata from PNG file

    # Extract the coordinate from the metadata
    coordinate_str = metadata.get('Coordinate', '')
    if coordinate_str:
        # Parse the coordinate string (e.g., "(1, 1)") into a tuple (1, 1)
        coordinates = tuple(map(int, coordinate_str.strip('()').split(', ')))
        return coordinates
    return None

def reconstruct_image_from_grid(grid_dir, grid_size=(30, 40), output_path="reconstructed_image.png"):
    """
    Reconstruct the original image from the grid images by using the metadata coordinates.

    :param grid_dir: Directory containing the grid PNG images.
    :param grid_size: Tuple indicating the grid size (rows, columns).
    :param output_path: Path to save the reconstructed image.
    """
    # Get the grid dimensions
    rows, cols = grid_size

    # Load the first image to get the height and width of each grid cell
    first_image_path = None
    for file_name in os.listdir(grid_dir):
        if file_name.lower().endswith(".png"):
            first_image_path = os.path.join(grid_dir, file_name)
            break

    if first_image_path is None:
        print("Error: No grid images found in the directory.")
        return

    grid_image = cv2.imread(first_image_path, cv2.IMREAD_UNCHANGED)
    if grid_image is None:
        print(f"Error: Unable to load image at {first_image_path}")
        return

    # Get the dimensions of each grid segment (assuming all are the same)
    cell_height, cell_width, _ = grid_image.shape
    reconstructed_image = np.zeros((rows * cell_height, cols * cell_width, 3), dtype=np.uint8)

    # Iterate over each file in the directory and reconstruct the image based on coordinates
    for file_name in os.listdir(grid_dir):
        if file_name.lower().endswith(".png"):
            # Get the coordinates from the metadata of the PNG
            grid_image_path = os.path.join(grid_dir, file_name)
            coordinates = extract_coordinates_from_metadata(grid_image_path)
            if coordinates:
                x, y = coordinates
                # Read the grid image
                grid_image = cv2.imread(grid_image_path, cv2.IMREAD_UNCHANGED)

                # Place the grid image in the correct position of the reconstructed image
                start_y = (y - 1) * cell_height
                start_x = (x - 1) * cell_width
                reconstructed_image[start_y:start_y + cell_height, start_x:start_x + cell_width] = grid_image

    # Save the reconstructed image
    cv2.imwrite(output_path, reconstructed_image)
    print(f"Reconstructed image saved to {output_path}")

if __name__ == "__main__":
    grid_directory = "/home/cha0s/Downloads/tazerman-into_the_dtuverse/output_grid"  # Replace with your grid directory path
    reconstruct_image_from_grid(grid_directory)
