import sys
from pathlib import Path

# --- ИСПРАВЛЕНИЕ ОШИБКИ "src not found" ---
# Находим корень проекта (поднимаемся на 2 папки вверх от текущего файла)
root_dir = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root_dir))

# Теперь импорты сработают
from src.lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
from src.lib.text import normalize, tokenize, top_n, count_freq
import argparse

def generate_report(input_path: str | Path, output_path: str | Path, encoding: str = "utf-8"):
    # Читаем текст (с обработкой ошибки, если файла нет)
    try:
        text = read_text(input_path, encoding=encoding) 
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_path}' не найден.")
        sys.exit(1)

    normal_text = normalize(text)  # нормализуем 
    tokens = tokenize(normal_text) # разбиваем на слова
    freq = count_freq(tokens)      # считаем частоту

    # ВАЖНО: Сортируем ВСЕ слова для CSV (count ↓, слово ↑)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # Записываем в CSV (если текст пустой, запишется только заголовок)
    write_csv(sorted_items, output_path, header=("word", "count"))

    # Получаем топ-5 для консоли
    top_words = top_n(freq, 5)     

    total_words = len(tokens) 
    unique_words = len(freq)  

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_file", default="data/input.txt")
    parser.add_argument("--out", dest="output_file", default="data/report.csv")
    parser.add_argument("--encoding", dest="encoding", default="utf-8")
    args = parser.parse_args()

    generate_report(args.input_file, args.output_file, args.encoding)




#для за пуска А используем
#python src/lab04/text_report.py --in data/lab04/input.txt


#для запуска В используем 
#python src/lab04/text_report.py --in data/lab04/input.txt



#для запуска C используем 
#python -c "open('data/input.txt', 'w', encoding='cp1251').write('Привет')"
#python src/lab04/text_report.py --in data/input.txt --encoding cp1251