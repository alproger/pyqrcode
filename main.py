from qr import makeQR           #function to generate qrcode 
from qr import get_infoQR       # function to decode qrcode

info = "https://github.com/alproger"

makeQR(info, bgcolor = 'black', fillcolor = 'white')       # making qrcode for value of info  

result = get_infoQR('./examples/5602a3ae-4c3d-42d3-9702-58a005b7271a.png') # decoding and getting info in qrcode

print(result)



