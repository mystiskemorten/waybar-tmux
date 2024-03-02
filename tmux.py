#!/usr/bin/env python3

import sys
import subprocess

icons = {
    "bash": "",
    "dnf": "",
    "docker": "",
    "fdisk": "",
    "fish": "󰈺",
    "git": "",
    "go": "",
    "java": "",
    "kubectl": "󱃾",
    "lazygit": "",
    "node": "",
    "npm": "",
    "nvim": "",
    "python": "",
    "python3": "",
    "[tmux]": "",
    "top": "",
    "vim": "",
    "yum": "",
    "zsh": "",
}


def get_session_directory():
    try:
        command_output = subprocess.check_output(
            'tmux display-message -p "#{pane_current_path}" | xargs basename',
            shell=True,
        )

        directory = command_output.decode("utf-8").strip()

        return directory
    except subprocess.CalledProcessError:
        return None


def get_windows():
    try:
        windows = []

        output_bytes = subprocess.check_output(
            "tmux list-windows | cut -f2 -d' '", shell=True
        )

        output_text = output_bytes.decode("utf-8")

        for window in output_text.splitlines():
            ACTIVE = "*" in window

            color = "#d3869b" if ACTIVE else "#b16286"

            window = window.replace("*", "").replace("-", "").strip()
            icon = icons.get(window)
            if icon is not None:
                window = icon

            windows.append(f'<span font_size="large" color="{color}">{window}  </span>')

        return windows
    except subprocess.CalledProcessError:
        return None


output = ""

directory = get_session_directory()
if directory:
    output += f"<span> ⎢ </span> {directory} >  "

windows = get_windows()
if windows:
    output += "".join(windows)

sys.stdout.write(output)
sys.stdout.flush()
