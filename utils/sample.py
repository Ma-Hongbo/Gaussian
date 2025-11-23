import os
import shutil
import argparse # Library for parsing command-line arguments

def extract_images(source_folder, target_folder, step):
    """
    Extracts one image every 'step' images from the source folder and copies it to the target folder.
    """
    
    # 1. Define supported image formats
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tiff', '.gif')

    # 2. Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"❌ Error: Source folder not found: '{source_folder}'")
        return

    # 3. Create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"📂 Created new directory: {target_folder}")
    else:
        print(f"📂 Target directory already exists: {target_folder}")

    # 4. Get and filter image files
    try:
        all_files = os.listdir(source_folder)
    except Exception as e:
        print(f"❌ Error accessing source folder: {e}")
        return

    image_files = [f for f in all_files if f.lower().endswith(valid_extensions)]
    
    # 5. Sort files (Critical for consistent sampling)
    image_files.sort()
    
    total_images = len(image_files)
    if total_images == 0:
        print("⚠️ No image files found in the source folder.")
        return

    # 6. Core logic: List slicing [start:end:step]
    selected_images = image_files[::step]

    print(f"📊 Found {total_images} images. Extracting {len(selected_images)} images (1 out of every {step})...")

    # 7. Execute Copy
    count = 0
    for filename in selected_images:
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(target_folder, filename)
        
        try:
            shutil.copy2(src_path, dst_path)
            count += 1
        except Exception as e:
            print(f"❌ Failed to copy {filename}: {e}")

    print(f"\n🎉 Done! Successfully copied {count} images to '{target_folder}'")

# ================= Command Line Argument Parsing =================
if __name__ == "__main__":
    # Initialize the parser
    parser = argparse.ArgumentParser(description="Script to sample images from a folder.")

    # Add arguments
    # 'source' and 'target' are positional arguments (required)
    parser.add_argument("source", type=str, help="Path to the source folder containing images.")
    parser.add_argument("target", type=str, help="Path to the target folder to save sampled images.")
    
    # '--step' is an optional argument (default is 5)
    parser.add_argument("--step", type=int, default=5, help="Sampling interval (e.g., 5 means take 1 image every 5 images).")

    # Parse the arguments passed from the command line
    args = parser.parse_args()

    # Run the function with parsed arguments
    extract_images(args.source, args.target, args.step)