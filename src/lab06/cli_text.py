import argparse
import sys
from pathlib import Path

# Импорты из ЛР3 (предполагается, что функции лежат в src/lib/text.py)
from src.lib.text import normalize, tokenize, count_freq, top_n

def cmd_stats(args):
    """Анализ частот слов в тексте."""
    p_in = Path(args.input)
    if not p_in.is_file():
        # Выводим понятную ошибку и завершаем работу
        print(f"Ошибка: Файл '{args.input}' не найден.", file=sys.stderr)
        sys.exit(1)

    text = p_in.read_text(encoding="utf-8")
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{args.top}:")
    for word, count in top_n(freq, args.top):
        print(f"{word}:{count}")

def cmd_cat(args):
    """Вывод содержимого файла построчно."""
    p_in = Path(args.input)
    if not p_in.is_file():
        print(f"Ошибка: Файл '{args.input}' не найден.", file=sys.stderr)
        sys.exit(1)

    with p_in.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if args.n:
                # Выравниваем номера строк по правому краю (ширина 6 символов)
                print(f"{i:6}\t{line}", end="")
            else:
                print(line, end="")

def main():
    parser = argparse.ArgumentParser(description="CLI-утилита для работы с текстом (ЛР6)")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные команды")

    # Подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов (по умолчанию 5)")
    stats_parser.set_defaults(func=cmd_stats)

    # Подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывод содержимого файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    cat_parser.set_defaults(func=cmd_cat)

    args = parser.parse_args()
    # Вызываем функцию, привязанную к подкоманде
    args.func(args)

if __name__ == "__main__":
    main()