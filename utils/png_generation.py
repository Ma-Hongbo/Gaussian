import os
import shutil
from PIL import Image
import argparse

def png_gen(image_dir, mask_dir, output_dir):
    """
    Generate RGBA images by applying segmentation masks to original images.
    
    Parameters:
    - image_dir: Directory containing original images.
    - mask_dir: Directory containing segmentation masks.
    - output_dir: Directory to save the output RGBA images.
    """

    # ----------------------------------------------------------------------
    # Move all existing images in `images` to `original_images`
    # ----------------------------------------------------------------------
    print("Moving existing images from 'images' to 'original_images'...")

    os.makedirs(image_dir, exist_ok=True)

    for file in os.listdir(output_dir):
        src_path = os.path.join(output_dir, file)

        # Skip non-image files
        if not file.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        dst_path = os.path.join(image_dir, file)

        shutil.move(src_path, dst_path)
        print(f"[moved] {src_path} → {dst_path}")

    print("Move completed.\n")

    # ----------------------------------------------------------------------
    # Apply mask to images and output RGBA images
    # ----------------------------------------------------------------------
    for img_name in os.listdir(image_dir):
        img_path = os.path.join(image_dir, img_name)

        # Skip non-image files
        if not img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        # Mask filename rule: mask_originalname
        mask_name = f"mask_{img_name}"
        mask_path = os.path.join(mask_dir, mask_name)

        # Check if mask exists
        if not os.path.exists(mask_path):
            print(f"[warning] mask missing: {mask_path}")
            continue

        # Load RGB image
        image = Image.open(img_path).convert("RGB")

        # Load mask as grayscale → alpha channel
        mask = Image.open(mask_path).convert("L")

        # Ensure mask matches image size
        mask = mask.resize(image.size, Image.NEAREST)

        # Combine RGB + Alpha
        rgba = image.copy()
        rgba.putalpha(mask)

        # Output path (force PNG)
        out_path = os.path.join(output_dir, img_name.replace('.jpg', '.png'))
        rgba.save(out_path)

        print(f"[ok] saved: {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=str,
        required=True,
        help="Root directory, e.g., C:\\Users\\TSingSV\\Desktop\\datas\\660_process"
    )

    args = parser.parse_args()

    root = args.root
    image_dir = os.path.join(root, "original_images")
    mask_dir = os.path.join(root, "masks")
    output_dir = os.path.join(root, "images")

    png_gen(image_dir, mask_dir, output_dir)
    print("\nAll images processed and saved with RGBA channels.")
