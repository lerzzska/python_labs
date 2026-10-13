from src.lib.text import normalize, tokenize, count_freq, top_n
import sys 
b_stat=1
raw_text=sys.stdin.read()
if raw_text.strip()== '':
    raise ValueError

clean=normalize(raw_text)
tokens=tokenize(clean)
total_w=len(tokens)
unique=len(set(tokens))
freq_dict= count_freq(tokens)
top_5=top_n(freq_dict)


print(f'Всего слов: {total_w}')
print(f'Уникальных слов: {unique}')
print(f'Топ-5:')

if not b_stat:
    for word, count in top_5:
        print(f'{word}:{count}')
else:
    ml=max([len(word[0]) for word in top_5])
    ml=max(ml, len('слово'))
    head=f'{'слово':<{ml}} | частота'
    print(head)
    print('-' * len (head))
    for top in top_5:
        print(f'{top[0]:<{ml}} | {top[1]}')




