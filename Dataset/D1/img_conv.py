# pip install --upgrade Pillow pillow-heif

import os
from PIL import Image
from pillow_heif import register_heif_opener

def convert_heic_to_png(input_heic_paths):

    try:
        register_heif_opener()
        print("Pillow HEIF opener registered successfully.")
    except Exception as e:
        print(f"Error registering HEIF opener: {e}")
        print("Make sure 'libheif' is installed on your system.")
        return

    for heic_path in input_heic_paths:
        if not os.path.exists(heic_path):
            print(f"Error: Input file not found: {heic_path}")
            continue

        try:
            base_name = os.path.basename(heic_path)
            file_name_without_ext = os.path.splitext(base_name)[0]
            output_png_path = os.path.join(os.path.dirname(heic_path), f"{file_name_without_ext}.png")

            # Open the HEIC image. Pillow can now handle it thanks to pillow-heif.
            with Image.open(heic_path) as img:
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')

                img.save(output_png_path, format="PNG")
                print(f"Successfully converted '{heic_path}' to '{output_png_path}'")

        except Exception as e:
            print(f"Failed to convert '{heic_path}': {e}")

if __name__ == "__main__":
    heic_files_to_convert = [
        "Clean_Handwriting.heic",
        "Fast_Writing.heic", 
        "Ruled_Paper.heic", 
    ]

    for i, dummy_path in enumerate(heic_files_to_convert):
        if not os.path.isabs(dummy_path) and not os.path.exists(os.path.dirname(dummy_path)) and os.path.dirname(dummy_path):
            os.makedirs(os.path.dirname(dummy_path), exist_ok=True)
        
       
        if not os.path.exists(dummy_path):
            try:
                temp_img = Image.new('RGB', (200, 150), color = (i*50, 100+i*20, 200-i*30))
                temp_img.save(dummy_path.replace(".heic", ".jpeg")) 
                print(f"Created dummy JPEG (acting as HEIC) at: {dummy_path.replace('.heic', '.jpeg')}")
                
            except Exception as e:
                print(f"Could not create dummy file {dummy_path.replace('.heic', '.jpeg')}: {e}")


    convert_heic_to_png(heic_files_to_convert)

    print("\nConversion process finished.")
    print("Check the directories where your original HEIC files are located for the new PNG files.")
    print("Remember that for this script to work with actual HEIC files, you must have 'libheif' installed on your system.")
