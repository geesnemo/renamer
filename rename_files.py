import os

folder = "D:\studia\gowno_na_studia\ezgif-5-060f144125-gif-png\\"

number = 1

for file_name in os.listdir(folder):
    numberstr = str(number)
    source = folder + file_name
    dest = folder + 'fig-' + numberstr + '.png'
    number += 1
    os.rename(source, dest)
    
