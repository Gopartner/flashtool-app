#!/usr/bin/env python3
"""
dom-tree  – penampil struktur folder (rekursif) + opsi -i <pattern>
Contoh:
    dom-tree                             # tampil semua (kecuali bawaan skiplist)
    dom-tree -i "*.log" -i ".env"        # abaikan tambahan pola
"""

import os
import sys
import fnmatch

# default skip list
DEFAULT_IGNORE = [
    "__pycache__",
    "extracted",
    "venv",
    "requirements.txt",
    "README",
    "README.*",  # abaikan README.md, README.txt dll
]


def parse_args() -> tuple[str, list[str]]:
    ignore, paths, args, i = [], [], sys.argv[1:], 0
    while i < len(args):
        if args[i] == "-i" and i + 1 < len(args):
            ignore.append(args[i + 1])
            i += 2
        else:
            paths.append(args[i])
            i += 1
    root = os.path.abspath(paths[0] if paths else os.getcwd())
    return root, ignore


def skipped(name: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(name, p) for p in patterns)


def show(path: str, ignore: list[str], indent: str = "") -> None:
    if skipped(os.path.basename(path), ignore):
        return
    print(f"{indent}📁 {os.path.basename(path)}/")
    try:
        for item in sorted(os.listdir(path)):
            if skipped(item, ignore):
                continue
            full = os.path.join(path, item)
            if os.path.isdir(full):
                show(full, ignore, indent + "    ")
            else:
                print(f"{indent}    📄 {item}")
    except PermissionError:
        print(f"{indent}    [Permission Denied]")


if __name__ == "__main__":
    root_path, extra_ignore = parse_args()
    # gabungkan default ignore dengan user input
    ignore_list = DEFAULT_IGNORE + extra_ignore
    show(root_path, ignore_list)
