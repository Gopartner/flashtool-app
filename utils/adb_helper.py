import subprocess


def adb_cmd(cmd: str) -> str:
    """Jalankan perintah adb shell dan kembalikan output string."""
    try:
        result = subprocess.check_output(
            ["adb", "shell"] + cmd.split(), stderr=subprocess.STDOUT, text=True
        ).strip()
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.strip()}"
    except FileNotFoundError:
        return "ADB tidak ditemukan. Pastikan adb sudah diinstall dan masuk PATH."


def get_device_info() -> dict:
    """Ambil informasi lengkap device Android."""
    info = {
        "codename": adb_cmd("getprop ro.product.device"),
        "build_product": adb_cmd("getprop ro.build.product"),
        "vendor_device": adb_cmd("getprop ro.product.vendor.device"),
        "platform": adb_cmd("getprop ro.board.platform"),
        "kernel": adb_cmd("uname -r"),
        "hardware": adb_cmd("cat /proc/cpuinfo | grep Hardware"),
    }

    # deteksi GKI atau non-GKI
    if info["kernel"].startswith(("5.", "6.")):
        info["kernel_type"] = "✅ GKI (Generic Kernel Image)"
    else:
        info["kernel_type"] = "❌ Non-GKI (Kernel lama/vendor)"
    return info
