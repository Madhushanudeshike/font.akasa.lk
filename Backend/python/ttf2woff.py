import os
from fontTools.ttLib import TTFont

fontpath = r'E:\\projects\akasa\cdnakasa\fonts\ttf'

for file in os.listdir(fontpath):
    if file.endswith('.ttf'):
        filename = os.path.splitext(file)[0];
        f = TTFont('fonts/ttf/'+file)
        f.flavor='woff'
        f.save('fonts/woff/'+filename+'.woff')
