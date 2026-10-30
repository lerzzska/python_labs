import csv
from pathlib import Path
from typing import Iterable, Sequence


def ensure_parent_dir(path: str | Path) -> None:
    """
    Создает родительские директории для указанного пути, если они не существуют.
    
    #:param path: Путь к файлу, для которого нужно создать директории.
    """

    p=Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)





def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открывает файл на чтение в указанной кодировке и возвращает его содержимое.
    
    Если файл не найден или кодировка не подходит, поднимаются соответствующие исключения (FileNotFoundError, UnicodeDecodeError). 
    Для чтения файлов в другой кодировке (например, Windows-1251),  передайте параметр encoding="cp1251".
    
    :param path: Путь к текстовому файлу.
    :param encoding: Кодировка файла (по умолчанию "utf-8").
    :return: Содержимое файла в виде одной строки.
    """
    
    p=Path(path)
    # Исключения FileNotFoundError и UnicodeDecodeError всплывают наверх естественным путем
    return p.read_text(encoding=encoding)
    




def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:

    """
    Создает или перезаписывает CSV-файл с разделителем ','.
    
    Перед записью проверяет, что все строки в `rows` имеют одинаковую длину.
    Если передан `header`, он записывается в качестве первой строки.
    
    :param rows: Список строк данных (списки или кортежи).
    :param path: Путь к создаваемому CSV-файлу.
    :param header: Опциональный заголовок (кортеж строк).
    :raises ValueError: Если строки данных имеют разную длину.
    """

    # Опционально: создаем папки, если их нет (полезно перед записью)
    ensure_parent_dir(path)

    # Определяем ожидаемую длину строки (из заголовка или из первой строки данных)
    expected_len = len(header) if header is not None else (len(rows[0]) if rows else 0)

    # Валидация: проверяем, что все строки одинаковой длины
    for i, row in enumerate(rows):
        if len(row) != expected_len:
            raise ValueError(f"Ошибка в строке {i}: длина {len(row)}, ожидалось {expected_len}.")
    p=Path(path)

    # Открываем файл с newline="", чтобы избежать двойных переводов строк на Windows
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for row in rows:
            writer.writerow(row)




if __name__ == "__main__":

    # Мини-тесты для проверки
    Path("data/lab04/input.txt").write_text("Привет, мир, привет!!!",encoding = "utf-8")
    txt = read_text("data/lab04/input.txt")
    write_csv([("word","count"),("test",3)], "data/lab04/check.csv")



