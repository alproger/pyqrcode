import qrcode
from uuid import uuid4

data = "https://github.com/alproger"


def makeQR(data, bgcolor = 'white', fillcolor = 'black', border = 5, boxsize = 10):
    '''function for making qrcode you must enter value data other values you may enter if you want
       * data is info for to make qrcode
       * bgcolor is background color of qrcode
       * fillcolor is color of qrcode
       * border is border of qrcode
       * boxsize is boxsize of qrcode  
    '''
    qr = qrcode.QRCode(
        version = 1,
        box_size= 10,
        border = 5  )

    qr.add_data(data)
    
    img = qr.make_image(fill_color = fillcolor, back_color = bgcolor)
    name = str(uuid4()) + '.png'
    img.save(name)


def get_infoQR(data):
    ''''function for to get info in qrcode'''
    
