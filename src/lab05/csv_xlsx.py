import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX с автошириной колонок (мин. 8 символов)."""
    p_in, p_out = Path(csv_path), Path(xlsx_path)

    if not p_in.is_file():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with p_in.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    if not rows or not rows[0]:
        raise ValueError("CSV файл пуст или не имеет заголовка")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    # Автоширина
    for col_idx, column in enumerate(ws.columns, start=1):
        max_length = max((len(str(cell.value)) for cell in column if cell.value), default=0)
        # Минимум 8 символов, плюс 2 для отступов
        adjusted_width = max(max_length + 2, 8)
        ws.column_dimensions[get_column_letter(col_idx)].width = adjusted_width

    p_out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(p_out)




