import os
from PIL import Image

# =====================================
# IMAGE RESIZER TOOL - SAFE FINAL
# =====================================

# Get script directory (works from anywhere)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define folders
input_folder = os.path.join(base_dir, "input_images")
output_folder = os.path.join(base_dir, "resized_images")

# Resize settings
max_width = 800
max_height = 600
convert_format = "JPEG"   # Set to None to keep original format
quality = 90              # JPEG quality (1-100)

# -------------------------------------
# Validate input folder
# -------------------------------------
if not os.path.exists(input_folder):
    print("❌ Input folder does not exist.")
    print(f"Create this folder and add images:\n{input_folder}")
    exit()

# -------------------------------------
# Ensure output folder is correct
# -------------------------------------
if os.path.exists(output_folder):
    if not os.path.isdir(output_folder):
        print("⚠ A file named 'resized_images' exists.")
        print("Deleting the file and creating a folder...")

        os.remove(output_folder)
        os.makedirs(output_folder)
else:
    os.makedirs(output_folder)

# -------------------------------------
# Supported formats
# -------------------------------------
supported_formats = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp")

print("🚀 Starting batch image processing...\n")

processed_count = 0
skipped_count = 0

# -------------------------------------
# Process Images
# -------------------------------------
for filename in os.listdir(input_folder):

    if not filename.lower().endswith(supported_formats):
        skipped_count += 1
        continue

    input_path = os.path.join(input_folder, filename)

    try:
        with Image.open(input_path) as img:

            # Keep aspect ratio (no stretching)
            img.thumbnail((max_width, max_height), Image.LANCZOS)

            name, ext = os.path.splitext(filename)

            if convert_format:
                output_filename = f"{name}.{convert_format.lower()}"
                output_path = os.path.join(output_folder, output_filename)

                img.convert("RGB").save(
                    output_path,
                    convert_format,
                    quality=quality
                )
            else:
                output_filename = filename
                output_path = os.path.join(output_folder, output_filename)
                img.save(output_path)

            processed_count += 1
            print(f"✅ Processed: {filename}")

    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

# -------------------------------------
# Summary
# -------------------------------------
print("\n==============================")
print(f"🎉 Finished!")
print(f"✅ Images processed: {processed_count}")
print(f"⏭ Files skipped: {skipped_count}")
print(f"📁 Output folder: {output_folder}")
print("==============================")