def is_macos():
    return os.name == "posix" and sys.platform == "darwin"


def is_linux():
    return os.name == "posix" and sys.platform.startswith("linux")