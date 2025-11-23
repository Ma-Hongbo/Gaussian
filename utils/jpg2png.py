import os
from PIL import Image

def convert_jpg_to_png_overwrite(input_dir):
    """
    Convert all .jpg/.jpeg images in input_dir to .png format,
    and delete the original .jpg/.jpeg files.
    """

    for file in os.listdir(input_dir):
        if file.lower().endswith((".jpg", ".jpeg")):
            src_path = os.path.join(input_dir, file)
            png_name = os.path.splitext(file)[0] + ".png"
            dst_path = os.path.join(input_dir, png_name)

            try:
                img = Image.open(src_path).convert("RGB")
                img.save(dst_path, "PNG")
                print(f"[OK] {file} → {png_name}")

                os.remove(src_path)
                print(f"[DEL] Removed original: {file}")

            except Exception as e:
                print(f"[ERROR] Failed to convert {file}: {e}")

    print("\n🎉 Overwrite conversion completed!")


if __name__ == "__main__":
    input_folder = r"C:\\Users\\TSingSV\\Desktop\\datas\\Supermarket\\516_process_no_mask\\images"
    convert_jpg_to_png_overwrite(input_folder)
