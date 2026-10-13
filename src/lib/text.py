import re
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






if __name__== '__main__':

    assert(normalize("ПрИвЕт\nМИр\t"))
    assert(normalize("ёжик, Ёлка", yo2e=True))
    assert(normalize("Hello\r\nWorld"))
    assert(normalize("  двойные   пробелы  "))


    assert(tokenize("привет мир"))
    assert(tokenize('hello,world!!!'))
    assert(tokenize("по-настоящему круто"))
    assert(tokenize("2025 год"))
    assert(tokenize("emoji 😀 не слово"))


    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)
    assert(freq)                      
    assert(top_n(freq, n=2)) 


    tokens = ["bb", "aa", "bb", "aa", "cc"]
    freq = count_freq(tokens)
    assert(freq)                      
    assert(top_n(freq, n=2)) 