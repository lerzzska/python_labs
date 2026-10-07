# ЛР3 — Тексты и частоты слов (словарь/множество)
## Задание А
### 1
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result=''
    for i in text:
        if i.isspace() or not i.isprintable():
            result+=' '
        else:
            result+=i
    words= result.split()
    result=' '.join(words)
    if yo2e:
        result= result.replace('ё','е')
        result= result.replace('Ё','Е')
    if casefold:
        result=result.casefold()
    else:
        result=result.lower()
    return result
```
normalize делает строку аккуратной. Она меняет все невидимые символы (табы, переводы строк) на пробелы. Потом убирает лишние пробелы — оставляет по одному и обрезает края. Если yo2e=True, заменяет «ё» на «е» и «Ё» на «Е». В конце приводит всё к нижнему регистру через casefold() или lower(). Возвращает готовую строку.

![фото](/images/lab03/text1.png)

### 2
```python
def tokenize(text: str) -> list[str]:
    tokens=[]
    k=''
    for i in text:
        if i.isalnum() or i=='_' or i=='-':
            k+=i
        else: 
            if k:
                tokens.append (k)
                k=''
    if k:
        tokens.append(k)
    return tokens
```
tokenize разбивает строку на слова: идёт по каждому символу и копит буквы, цифры, подчёркивания и дефисы в переменную k. Как только встречается любой другой символ (пробел, запятая, эмодзи), накопленное слово добавляется в список tokens, а k обнуляется. В конце, если в k что-то осталось, последнее слово тоже добавляется. Возвращает список слов.

![фото](/images/lab03/text2.png)

### 3
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq={}
    for i in tokens:
        freq[i]=freq.get(i,0)+1
    return freq
```
count_freq считает, сколько раз встречается каждое слово: проходит по списку токенов и для каждого увеличивает счётчик в словаре freq. Метод get(i, 0) берёт текущее число (или 0, если слова ещё не было) и прибавляет 1. Возвращает словарь «слово → количество».

![фото](/images/lab03/text3.png)

### 4
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    k=[]
    for word in freq:
        k.append((word, freq[word]))
    for i in range (len(k)):
        for j in range (len(k)-1-i):
            w1, c1=k[j]
            w2, c2=k[j+1]
            if c1<c2 or (c1==c2 and w1>w2):
                k[j], k[j+1] = k[j+1], k[j]
    return k[:n]
```
top_n возвращает топ-N слов по частоте. Сначала собирает пары (слово, частота) из словаря в список k. Потом сортирует их «пузырьком»: если у правой пары частота больше или при равных частотах её слово идёт раньше по алфавиту — пары меняются местами. В итоге берёт первые n элементов.

![фото](/images/lab03/text3.png)

## Задание В





