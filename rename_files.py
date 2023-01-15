import os

folder = "Path to your folder"

number = 1

for file_name in os.listdir(folder):
    numberstr = str(number)
    source = folder + file_name
    dest = folder + 'fig-' + numberstr + '.png'
    number += 1
    os.rename(source, dest)
    
