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

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))


print('')



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

print(tokenize("привет мир"))
print(tokenize('hello,world!!!'))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))


print('')


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq={}
    for i in tokens:
        freq[i]=freq.get(i,0)+1
    return freq

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

tokens = ["a", "b", "a", "c", "b", "a"]
freq = count_freq(tokens)
print(freq)                      
print(top_n(freq, n=2)) 

print('')

tokens = ["bb", "aa", "bb", "aa", "cc"]
freq = count_freq(tokens)
print(freq)                      
print(top_n(freq, n=2)) 

