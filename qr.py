import qrcode                          # libarary for generate qrcode
from uuid import uuid4                 # library for generate random name for qrcode
from pyzbar.pyzbar import decode       # library for decoding qrcode
from PIL import Image                  # library for working with image


def makeQR(data, folder = '' , bgcolor = 'white', fillcolor = 'black', bordersize = 5, boxsize = 10,):
    '''function for making qrcode you must enter value data other values you may enter if you want
       * data       is info for to make qrcode
       * bgcolor    is background color of qrcode
       * fillcolor  is color of qrcode
       * bordersize is border of qrcode
       * boxsize    is boxsize of qrcode
       * folder     is folder in ram of computer to save qrcode file  
    '''
    qr = qrcode.QRCode(
        version = 1,
        box_size= boxsize,
        border = bordersize  )

    qr.add_data(data)       # adding information to qrcode    
    img = qr.make_image(fill_color = fillcolor, back_color = bgcolor) # adding style information to qrcode
    name = 'qr.png' # generation name for qrcode
    
    if folder == '' :
       img.save(name)               # saving qrcode format of image
    
    else :
        save = folder+name
        img.save(save)   


def get_infoQR(qrcode):
    ''''function for to get info in qrcode
        * qrcode is qrcode image address to open
        * *example qrcode = 'C:/qrcode/img.png'
        '''
    img = Image.open(qrcode) # opennig image of qrcode
    result = decode(img)     # decoding qrcode 
    return f'info : {str(result[0][0])}' # to get only information of qrcode




