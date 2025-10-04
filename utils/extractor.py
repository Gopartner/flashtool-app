import os
import tarfile
import zipfile
import shutil
from tqdm import tqdm
from utils.terminal_helper import clear_screen


def pilih_file_firmware(ekstensi=None):
    """Pilih file firmware dari folder download_results"""
    folder = "download_results"

    if not os.path.exists(folder):
        print(f"❌ Folder {folder} tidak ditemukan.")
        return None

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if ekstensi:
        files = [f for f in files if f.lower().endswith(tuple(ekstensi))]

    if not files:
        print("❌ Tidak ada file firmware ditemukan di download_results/")
        return None

    print("\n=== Pilih File Firmware ===")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    try:
        idx = int(input("Pilih nomor file: ").strip())
        return os.path.join(folder, files[idx - 1])
    except (ValueError, IndexError):
        print("❌ Pilihan tidak valid.")
        return None


def resolve_output_folder(base_name):
    """Tentukan folder ekstrak, dan jika sudah ada → tanya user"""
    out_dir = os.path.join("extracted", base_name)

    if os.path.exists(out_dir):
        print(f"\n⚠️ Folder hasil ekstrak sudah ada: {out_dir}")
        print("1. Replace (hapus lama, ekstrak ulang)")
        print("2. Gunakan nama baru")
        print("3. Batal")
        pilihan = input("Pilih opsi: ").strip()

        if pilihan == "1":
            shutil.rmtree(out_dir)
            print("🗑 Folder lama dihapus.")
        elif pilihan == "2":
            counter = 1
            new_out_dir = f"{out_dir}_{counter}"
            while os.path.exists(new_out_dir):
                counter += 1
                new_out_dir = f"{out_dir}_{counter}"
            out_dir = new_out_dir
            print(f"📂 Menggunakan folder baru: {out_dir}")
        else:
            print("❌ Operasi dibatalkan.")
            return None

    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def extract_firmware():
    clear_screen()

    fw_file = pilih_file_firmware([".tgz", ".tar", ".zip"])
    if not fw_file:
        return

    base_name = os.path.splitext(os.path.basename(fw_file))[0]
    out_dir = resolve_output_folder(base_name)
    if not out_dir:
        return

    clear_screen()
    print(f"Mengekstrak {fw_file} ke folder '{out_dir}'...\n")

    if fw_file.endswith((".tgz", ".tar")):
        with tarfile.open(fw_file, "r:*") as tar:
            members = tar.getmembers()
            with tqdm(total=len(members), desc="Extracting", unit="file") as bar:
                for member in members:
                    tar.extract(member, path=out_dir)
                    bar.update(1)

    elif fw_file.endswith(".zip"):
        with zipfile.ZipFile(fw_file, "r") as zip_ref:
            members = zip_ref.namelist()
            with tqdm(total=len(members), desc="Extracting", unit="file") as bar:
                for member in members:
                    zip_ref.extract(member, out_dir)
                    bar.update(1)

    else:
        print("❌ Format file tidak didukung untuk ekstrak.")
        return

    clear_screen()
    print(f"✅ Ekstrak selesai! Hasil ada di: {out_dir}")
