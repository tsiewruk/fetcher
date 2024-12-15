import platform
import sys


def check_os(kernel_name):
    if kernel_name.startswith('IRIX'):
        return 'IRIX'
    elif kernel_name in ('Linux', 'GNU') or kernel_name.startswith('GNU'):
        return 'Linux'
    elif any(kernel_name.endswith(bsd) for bsd in ['BSD', 'DragonFly', 'Bitrig']):
        return 'BSD'
    elif any(name in kernel_name for name in ['CYGWIN', 'MSYS', 'MINGW']):
        return 'Windows'
    else:
        print(f"Unknown OS detected: '{kernel_name}', aborting...", file=sys.stderr)
        print("Open an issue on GitHub to add support for your OS.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    kernel_name = platform.uname().system
    check_os(kernel_name)
