fio=input('ФИО:')
s=fio.split()
famil=s[0]
imya=s[1]
otchest=s[2]
i1=famil[0].upper()
i2=imya[0].upper()
i3=otchest[0].upper()
inicial=i1+i2+i3+'.'
imfamot=famil+' '+imya+' '+otchest
dlina=len(imfamot)
print(f'ФИО: {imfamot}')
print(f'Инициалы: {inicial}')
print(f'Длина (символов): {dlina}')