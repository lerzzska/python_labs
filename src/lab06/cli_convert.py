import argparse
import sys
from pathlib import Path

# Импорты из ЛР5
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def handle_convert(func, input_path, output_path):
    """Вспомогательная функция для вызова конвертеров и обработки ошибок."""
    try:
        func(input_path, output_path)
        print(f"Успешно: {input_path} -> {output_path}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка данных: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="CLI-утилита для конвертации данных (ЛР6)")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные команды")

    # Фабрика для создания одинаковых подкоманд
    for cmd_name, cmd_help, target_func in [
        ("json2csv", "Конвертировать JSON в CSV", json_to_csv),
        ("csv2json", "Конвертировать CSV в JSON", csv_to_json),
        ("csv2xlsx", "Конвертировать CSV в Excel", csv_to_xlsx)
    ]:
        p = subparsers.add_parser(cmd_name, help=cmd_help)
        p.add_argument("--in", dest="input", required=True, help="Входной файл")
        p.add_argument("--out", dest="output", required=True, help="Выходной файл")
        # Привязываем функцию через lambda, чтобы передать target_func
        p.set_defaults(func=lambda args, f=target_func: handle_convert(f, args.input, args.output))

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()