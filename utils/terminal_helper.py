import os


def clear_screen():
    """Bersihkan layar terminal (Windows / Linux / macOS)."""
    os.system("cls" if os.name == "nt" else "clear")
