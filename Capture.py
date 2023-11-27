import pygetwindow as gw
from mss import mss


def get_window(win_name):
    window = gw.getWindowsWithTitle(win_name)
    if len(window) == 0:
        return ""
    else:
        return window[0]


def setup_monitor(win_name):
    window = get_window(win_name)

    if window == "":
        raise Exception("Window not found")
    else:
        x, y, width, height = window.left, window.top, window.width, window.height
        screen = mss()
        mon = screen.monitors[0]
        monitor = {"top": y, "left": x, "width": width, "height": height, "mon": mon}
        return screen, monitor