import subprocess
import os


def run_cmd(cmd):
    try:
        result = subprocess.run(
            cmd, shell=True, check=True, text=True, capture_output=True
        )
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {cmd}")
        print(e.stderr.strip())


def adb_devices():
    print("\n=== Cek ADB Devices ===")
    run_cmd("adb devices")


def fastboot_devices():
    print("\n=== Cek Fastboot Devices ===")
    run_cmd("fastboot devices")


def adb_reboot_bootloader():
    print("\n=== Reboot ke Fastboot Mode ===")
    run_cmd("adb reboot bootloader")


def fastboot_reboot_system():
    print("\n=== Reboot dari Fastboot ke System ===")
    run_cmd("fastboot reboot")
    print("⚡ Device reboot ke Android system...")


def fastboot_reboot_recovery():
    print("\n=== Reboot dari Fastboot ke Recovery ===")
    run_cmd("fastboot reboot recovery")
    print("⚡ Device reboot ke Recovery...")


def flash_partition():
    print("\n=== Flash Partition ===")
    base_folder = "extracted"

    if not os.path.isdir(base_folder):
        print(f"❌ Folder '{base_folder}' tidak ditemukan.")
        return

    # list semua subfolder di extracted/
    subfolders = [
        f
        for f in os.listdir(base_folder)
        if os.path.isdir(os.path.join(base_folder, f))
    ]
    if not subfolders:
        print("❌ Tidak ada folder hasil ekstrak di 'extracted/'.")
        return

    print("\n=== Pilih Folder Firmware ===")
    for i, folder in enumerate(subfolders, start=1):
        print(f"{i}. {folder}")

    idx = input("Pilih folder [nomor] (0 untuk batal): ").strip()
    if idx == "0":
        print("↩️ Batal, kembali ke menu utama.")
        return
    if not idx.isdigit() or int(idx) < 1 or int(idx) > len(subfolders):
        print("❌ Pilihan tidak valid.")
        return

    chosen_folder = os.path.join(base_folder, subfolders[int(idx) - 1])

    # kalau ada subfolder images/, gunakan itu
    images_path = os.path.join(chosen_folder, "images")
    if os.path.isdir(images_path):
        chosen_folder = images_path

    # list semua .img di folder terpilih
    img_files = [f for f in os.listdir(chosen_folder) if f.endswith(".img")]
    if not img_files:
        print("❌ Tidak ada file .img di folder ini.")
        return

    print("\n=== Pilih File Partisi ===")
    print("0. Batal / Kembali ke menu utama")
    for i, img in enumerate(img_files, start=1):
        print(f"{i}. {img}")

    idx2 = input("Pilih file partisi [nomor]: ").strip()
    if idx2 == "0":
        print("↩️ Batal, kembali ke menu utama.")
        return
    if not idx2.isdigit() or int(idx2) < 1 or int(idx2) > len(img_files):
        print("❌ Pilihan tidak valid.")
        return

    chosen_img = img_files[int(idx2) - 1]
    partisi = os.path.splitext(chosen_img)[0]  # boot.img -> boot
    file_path = os.path.join(chosen_folder, chosen_img)

    print(f"\n📤 Flashing {partisi} dari {file_path} ...")
    run_cmd(f'fastboot flash {partisi} "{file_path}"')
    print(f"✅ Selesai flash {partisi}.img")
