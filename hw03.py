import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama
init(autoreset=True)


def visualize_directory(path, prefix=""):
    """
    Рекурсивно візуалізує структуру директорії з кольоровим виведенням.
    """
    contents = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))

    for index, item in enumerate(contents):
        is_last = index == len(contents) - 1
        connector = "┗ " if is_last else "┣ "
        extension = "  " if is_last else "┃ "

        if item.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}📂 {item.name}")
            visualize_directory(item, prefix + extension)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}📜 {item.name}")


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}❌ Вкажіть шлях до директорії як аргумент.")
        print(f"{Fore.YELLOW}Використання: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}❌ Шлях '{directory_path}' не існує.")
        sys.exit(1)

    if not directory_path.is_dir():
        print(f"{Fore.RED}❌ '{directory_path}' не є директорією.")
        sys.exit(1)

    print(f"{Fore.CYAN}📦 {directory_path.name}")
    visualize_directory(directory_path)


if __name__ == "__main__":
    main()