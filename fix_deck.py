import os
import glob

# 1. Peta Perubahan Nama Folder
folder_map = {
    "slide_9_lokasi_jadwal": "slide_4_lokasi_jadwal",
    "slide_4_storyboard": "slide_5_storyboard",
    "slide_13_referensi_video": "slide_6_referensi_video",
    "slide_10_placeholder_kabesha": "slide_7_placeholder_kabesha",
    "slide_11_placeholder_milestone": "slide_8_placeholder_milestone",
    "slide_5_era_trainee_fixed_layout": "slide_10_era_trainee",
    "slide_6_era_cosmos": "slide_11_era_cosmos",
    "slide_7_era_snow": "slide_12_era_snow",
    "slide_8_era_love": "slide_13_era_love",
    "slide_12_outro_wishes": "slide_14_outro_wishes"
}

# 2. Rename Folders
for old_name, new_name in folder_map.items():
    if os.path.exists(old_name) and not os.path.exists(new_name):
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} -> {new_name}")

# 3. Fix Teks dan Link Navigasi di Seluruh File HTML & MD
for filepath in glob.glob("**/*.*", recursive=True):
    if not filepath.endswith((".html", ".md")) or ".git" in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Hapus jejak Y2K & Lanautica
    new_content = content.replace("LANAUTICA", "ForAlana") \
                         .replace("Lanautica", "ForAlana") \
                         .replace("Y2K", "Chapter 20") \
                         .replace("KONSEP CHAPTER - 2026", "KONSEP CHAPTER - 20")

    # Update Link Navigasi href (supaya tidak error 404)
    for old_folder, new_folder in folder_map.items():
        new_content = new_content.replace(f"/{old_folder}/", f"/{new_folder}/")

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated text in: {filepath}")

print("Selesai! Repository sudah sinkron dengan PPT final.")