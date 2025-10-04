# utils/md5_checker.py
import os
import hashlib
import json
from tqdm import tqdm
from termcolor import colored
from utils.terminal_helper import clear_screen


def md5sum(filename):
    """Hitung checksum MD5 dengan progress bar cantik."""
    md5 = hashlib.md5()
    total_size = os.path.getsize(filename)

    print(colored(f"\n📂 File   : {os.path.basename(filename)}", "cyan"))
    print(colored(f"📏 Ukuran : {total_size / (1024*1024*1024):.2f} GB\n", "cyan"))

    with open(filename, "rb") as f, tqdm(
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        desc=colored("🔎 Menghitung MD5", "yellow"),
        ncols=80,
        colour="cyan",
    ) as bar:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
            bar.update(len(chunk))

    return md5.hexdigest()


def pilih_file(folder="download_results"):
    """Tampilkan menu pilih file dari folder download_results dengan opsi kembali."""
    if not os.path.exists(folder):
        print(colored(f"❌ Folder {folder} tidak ditemukan.", "red"))
        return None

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if not files:
        print(colored(f"❌ Tidak ada file di {folder}", "red"))
        return None

    print(colored(f"\n=== Pilih File dari {folder} ===", "cyan", attrs=["bold"]))
    print(colored("0. Kembali", "yellow"))
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    try:
        idx = int(input(colored("Pilih nomor file: ", "green")).strip())
        if idx == 0:
            return None
        return os.path.join(folder, files[idx - 1])
    except (ValueError, IndexError):
        print(colored("❌ Pilihan tidak valid.", "red"))
        return None


def pilih_md5(json_path="checksum/data.json"):
    """Tampilkan menu pilih MD5 dari data.json dengan opsi kembali."""
    if not os.path.exists(json_path):
        print(colored(f"❌ data.json tidak ditemukan di {json_path}", "red"))
        return None

    with open(json_path, "r") as f:
        try:
            md5_list = json.load(f)
        except json.JSONDecodeError:
            print(colored("❌ Format data.json salah (bukan JSON valid).", "red"))
            return None

    if not isinstance(md5_list, list):
        print(
            colored("❌ Format data.json harus berupa list berisi string MD5.", "red")
        )
        return None

    print(colored("\n=== Pilih MD5 dari data.json ===", "cyan", attrs=["bold"]))
    print(colored("0. Kembali", "yellow"))
    for i, md5 in enumerate(md5_list, 1):
        print(f"{i}. {md5}")

    try:
        idx = int(input(colored("Pilih nomor MD5: ", "green")).strip())
        if idx == 0:
            return None
        return md5_list[idx - 1].lower()
    except (ValueError, IndexError):
        print(colored("❌ Pilihan tidak valid.", "red"))
        return None


def cek_md5_from_json():
    """User pilih file dari download_results dan pilih MD5 dari data.json"""
    clear_screen()

    file_path = pilih_file("download_results")
    if not file_path:
        return False  # batal → kembali ke menu utama

    expected_md5 = pilih_md5("checksum/data.json")
    if not expected_md5:
        return False  # batal → kembali ke menu utama

    clear_screen()
    print(
        colored(
            f"🔍 Sedang cek MD5 untuk: {os.path.basename(file_path)}\n",
            "cyan",
            attrs=["bold"],
        )
    )

    # Hitung MD5 (progress tampil sementara)
    file_md5 = md5sum(file_path)

    # 🔹 Bersihkan layar lagi, tampilkan hasil akhir saja
    clear_screen()
    print(colored("=== Hasil Perbandingan MD5 ===\n", "magenta", attrs=["bold"]))
    print(f"👉 MD5 file   : {colored(file_md5, 'yellow')}")
    print(f"🎯 MD5 target : {colored(expected_md5, 'yellow')}")

    if file_md5 == expected_md5:
        print(colored("\n✅ Cocok! File valid.", "green", attrs=["bold"]))
        return True
    else:
        print(
            colored(
                "\n❌ Tidak cocok! File mungkin korup atau salah unduh.",
                "red",
                attrs=["bold"],
            )
        )
        return False
