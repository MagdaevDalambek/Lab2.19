#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Разработайте аналог утилиты tree в Linux. Используйте возможности модуля argparse для
# управления отображением дерева каталогов файловой системы. Добавьте дополнительные
# уникальные возможности в данный программный продукт.

import argparse
from datetime import datetime
from pathlib import Path


def list_files(path, show_time, show_size, only_dir, max_level=1, level=0,size = "", time=""):

    if level == max_level:
        pass

    else:
        indent = f"{'   ' * level} "
        for item in path.iterdir():
            if item.is_file() and not (only_dir):
                if show_time:
                    time = datetime.fromtimestamp(item.stat().st_mtime)

                if show_size:
                    size = item.stat().st_size
                print(f"{indent}{item.name} {size} {time}")
            elif item.is_dir():
                if show_time:
                    time = datetime.fromtimestamp(item.stat().st_mtime)

                if show_size:
                    size = item.stat().st_size
                print(f"{indent}{item.name}/ {size} {time}")

                list_files(
                    item, show_size, show_time, only_dir, max_level, level + 1
                )


def main():
    parser = argparse.ArgumentParser(
        description="Утилита для отображения дерева каталогов и файлов"
    )
    parser.add_argument("path", nargs="?", default=".", help="Путь к каталогу")
    parser.add_argument(
        "-l", "--level", default=1, type=int, help="Уровень вложенности"
    )
    parser.add_argument(
        "-d", "--dir", default=False, help="Показывать только директории"
    )
    parser.add_argument(
        "-s", "--showsize", default=False, help="Показать размер файлов"
    )
    parser.add_argument(
        "-t", "--time", default=False, help="Показать время изменения"
    )
    args = parser.parse_args()

    path = Path(args.path)
    max_level = args.level
    only_dir = args.dir
    show_size = args.showsize
    show_time = args.time

    if path.is_dir():
        list_files(path, show_time, show_size, only_dir, max_level)
    else:
        print(f"Путь {args.path} не существует или не является каталогом")


if __name__ == "__main__":
    main()
