def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError
    
    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError
    
    if not isinstance(gpa, (int, float)) or isinstance(gpa, bool):
        raise TypeError
    
    if not 0.0 <= gpa <= 5.0:
        raise ValueError
    
    parts = fio.split()
    if len(parts) < 2:
        raise ValueError
    
    group = group.strip()
    if not group:
        raise ValueError
    
    surname = parts[0].capitalize()
    initials = "".join(p[0].upper() + "." for p in parts[1:3])
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

try:
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
except TypeError:
    print('TypeError')
try:
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
except ValueError:
    print('ValueError')
try:
    print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
except ValueError:
    print('ValueError')
try:
    print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
except TypeError:
    print('TypeError')
