# menu.py
from utils.md5_checker import cek_md5_from_json
from utils.extractor import extract_firmware
from utils.flash_helper import (
    adb_devices,
    fastboot_devices,
    adb_reboot_bootloader,
    fastboot_reboot_system,
    fastboot_reboot_recovery,
    flash_partition,
)
from utils.adb_helper import get_device_info
from utils.terminal_helper import clear_screen
from utils.test_boot import test_boot_img  # ✅ fitur baru tes boot.img

from rich.console import Console
from rich.table import Table
import time

console = Console()


def tampilkan_menu():
    table = Table(title="📱 MENU UTAMA - Oprek HP", show_lines=True)
    table.add_column("No", justify="center", style="cyan", no_wrap=True)
    table.add_column("Deskripsi", style="bold yellow")

    table.add_row("1", "MD5 Checksum (cek hasil download)")
    table.add_row("2", "Extract Firmware (tgz/zip/tar)")
    table.add_row("3", "Cek adb devices")
    table.add_row("4", "Cek fastboot devices")
    table.add_row("5", "Reboot adb → fastboot (bootloader)")
    table.add_row("6", "Reboot fastboot → system")
    table.add_row("7", "Flash partition (boot/system/vendor)")
    table.add_row("8", "Reboot fastboot → recovery")
    table.add_row("9", "Cek info HP")
    table.add_row(
        "10", "Tes boot.img dari extracted/ (tanpa install permanen)"
    )  # ✅ fitur baru
    table.add_row("11", "Keluar")

    console.print(table)


def menu():
    while True:
        tampilkan_menu()
        pilihan = input("👉 Pilih opsi [1-11]: ").strip()

        if pilihan == "1":
            cek_md5_from_json()

        elif pilihan == "2":
            console.print("[yellow]📦 Extract firmware...[/yellow]")
            extract_firmware()
            console.print("[green]✅ Selesai extract firmware[/green]")

        elif pilihan == "3":
            adb_devices()

        elif pilihan == "4":
            fastboot_devices()

        elif pilihan == "5":
            console.print("[magenta]🔄 Reboot ke fastboot...[/magenta]")
            adb_reboot_bootloader()
            console.print("[green]🚀 Done[/green]")

        elif pilihan == "6":
            fastboot_reboot_system()

        elif pilihan == "7":
            flash_partition()

        elif pilihan == "8":
            fastboot_reboot_recovery()

        elif pilihan == "9":
            device_info = get_device_info()
            console.print("\n[bold green]=== Informasi Device ===[/bold green]")
            console.print(
                f"[cyan]Codename       :[/cyan] {device_info.get('codename', '-')}"
            )
            console.print(
                f"[cyan]Build Product  :[/cyan] {device_info.get('build_product', '-')}"
            )
            console.print(
                f"[cyan]Vendor Device  :[/cyan] {device_info.get('vendor_device', '-')}"
            )
            console.print(
                f"[cyan]Platform (SoC) :[/cyan] {device_info.get('platform', '-')}"
            )
            console.print(
                f"[cyan]Kernel Version :[/cyan] {device_info.get('kernel', '-')}"
            )
            console.print(
                f"[cyan]Hardware       :[/cyan] {device_info.get('hardware', '-')}"
            )
            console.print(
                f"[cyan]Kernel Type    :[/cyan] {device_info.get('kernel_type', '-')}"
            )

        elif pilihan == "10":  # ✅ Tes boot.img
            console.print("[magenta]🧪 Tes boot.img hasil repack...[/magenta]")
            test_boot_img()

        elif pilihan == "11":
            console.print("[bold red]Keluar...[/bold red]")
            break

        else:
            console.print("[bold red]❌ Pilihan tidak valid.[/bold red]")

        console.print("\n")
        time.sleep(1)


if __name__ == "__main__":
    clear_screen()  # ✅ Bersihkan terminal sebelum tampil menu
    menu()
