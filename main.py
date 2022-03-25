from qr import makeQR           #function to generate qrcode 
from qr import get_infoQR       # function to decode qrcode

info = "https://github.com/alproger"

# makeQR(info, bgcolor = 'black', fillcolor = 'white')       # making qrcode for value of info
result = get_infoQR('./examples/qr.png') # decoding and getting info in qrcode
print(result)



