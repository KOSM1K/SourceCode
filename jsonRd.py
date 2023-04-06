import json
import math
from PIL import Image

f = open('C:\\Users\\Dan\\Downloads\\16a4qD2PcAw (1).json')
picturePath = 'C:\\Users\\Dan\\Downloads\\16a4qD2PcAw (1).jpg'
debugLayout = True

data = json.loads(f.read())

nObj = len(data['shapes'])
cnt = 0

for curObj in data['shapes']:
    x1, y1, x2, y2 = \
        (min(curObj['points'][0][0], curObj['points'][1][0]),
         min(curObj['points'][0][1], curObj['points'][1][1]),
         max(curObj['points'][0][0], curObj['points'][1][0]),
         max(curObj['points'][0][1], curObj['points'][1][1]))
    width, height = math.ceil(x2 - x1), math.ceil(y2 - y1)
    x1, y1 = int(x1), int(y1)
    name = curObj['label']

    if debugLayout: print('{:10s}, {:5d}, {:5d}, {:5d}, {:5d}'.format(name, x1, y1, width, height))

    image = Image.open(picturePath)
    image.crop((x1, y1, math.ceil(x2), math.ceil(y2))).save(str(cnt) + ' ' + data['imagePath'])
    cnt += 1
