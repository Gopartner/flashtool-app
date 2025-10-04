# utils/test_boot.py
import subprocess
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()


def pilih_folder_extracted():
    base_dir = Path("extracted")
    if not base_dir.exists():
        console.print("[bold red]❌ Folder 'extracted/' tidak ditemukan![/bold red]")
        return None

    folders = [f for f in sorted(base_dir.iterdir()) if f.is_dir()]
    if not folders:
        console.print("[bold red]❌ Tidak ada folder di extracted/[/bold red]")
        return None

    console.print("\n[bold cyan]📁 Daftar Folder Firmware[/bold cyan]\n")
    table = Table(show_lines=True)
    table.add_column("No", justify="center", style="yellow")
    table.add_column("Nama Folder", style="green")
    for i, folder in enumerate(folders, start=1):
        table.add_row(str(i), folder.name)
    console.print(table)
    console.print("[bold yellow]0. Kembali ke menu utama[/bold yellow]")

    while True:
        choice = input("\n👉 Pilih folder [0 untuk kembali]: ").strip()
        if not choice.isdigit():
            console.print("[red]Masukkan angka yang valid![/red]")
            continue
        choice = int(choice)

        if choice == 0:
            return None
        elif 1 <= choice <= len(folders):
            return folders[choice - 1]
        else:
            console.print("[red]Nomor tidak valid![/red]")


def pilih_file_img(folder: Path):
    images_dir = folder / "images"
    if not images_dir.exists():
        console.print(
            f"[bold red]❌ Folder 'images/' tidak ditemukan di {folder.name}[/bold red]"
        )
        return None

    img_files = sorted(images_dir.glob("*.img"))
    if not img_files:
        console.print(f"[bold red]❌ Tidak ada file .img di {images_dir}[/bold red]")
        return None

    console.print(f"\n[bold cyan]🧩 File IMG di {folder.name}/images/[/bold cyan]\n")
    table = Table(show_lines=True)
    table.add_column("No", justify="center", style="yellow")
    table.add_column("Nama File IMG", style="green")

    for i, img in enumerate(img_files, start=1):
        table.add_row(str(i), img.name)
    console.print(table)
    console.print("[bold yellow]0. Kembali ke daftar folder[/bold yellow]")

    while True:
        choice = input("\n👉 Pilih file img [0 untuk kembali]: ").strip()
        if not choice.isdigit():
            console.print("[red]Masukkan angka yang valid![/red]")
            continue
        choice = int(choice)

        if choice == 0:
            return None
        elif 1 <= choice <= len(img_files):
            return img_files[choice - 1]
        else:
            console.print("[red]Nomor tidak valid![/red]")


def test_boot_img():
    """Fungsi utama: pilih folder → pilih img → fastboot boot"""
    folder = pilih_folder_extracted()
    if not folder:
        console.print("[yellow]🔙 Kembali ke menu utama...[/yellow]")
        return

    img_path = pilih_file_img(folder)
    if not img_path:
        console.print("[yellow]🔙 Kembali ke daftar folder...[/yellow]")
        return test_boot_img()

    console.print(f"[cyan]📤 Tes boot dengan:[/cyan] {img_path}")

    try:
        result = subprocess.run(
            ["fastboot", "boot", str(img_path.resolve())],
            text=True,
            capture_output=True,
            check=True,
        )
        console.print(f"[green]✅ Berhasil perintah fastboot boot[/green]")
        console.print(result.stdout)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]❌ Gagal tes boot![/bold red]\n{e.stderr}")
    except FileNotFoundError:
        console.print("[bold red]❌ fastboot tidak ditemukan di PATH[/bold red]")
