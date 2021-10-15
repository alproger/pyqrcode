<h2 align = center> **__pyqrcode__** </h2>

<h3> Qrcode generator in python. </h3>

<p> It's simple programm to generate qrcode and getting info in qrcode for some information. You can generate qrcode for your information and you can scan qrcode for get your information. 

* <h4>installition for generate qrcode </h4>
  
  `pip install qrcode`

* <h4>installition for get info in qrcode</h4>
  
  `pip install pyzbar`

<br>

<p> <strong>main.py</strong> is code for testing <strong>qr.py</strong> code. <strong>qr.py</strong> has 2 main functions they are :

* makeQR
* get_infoQR 

<strong>makeQR</strong> is function for to generate qrcode for user inputed information. For this function user can input some values. They are :

* data ---> information for to generate qrcode
* folder ---> folder in ram of computer to save qrcode file  
* bgcolor ---> background color of qrcode
* fillcolor --->  is color of qrcode
* bordersize ---> border of qrcode
* boxsize   --->  boxsize of qrcode  

User must input data value other values not necessarily . If user doesn't inputs other values qrcode gets standart format.
For exaple :

`#1`

```info = "https://github.com/alproger"```

```makeQR(info, bgcolor = 'black', fillcolor = 'white')```

`#2`

```makeQR(info)```

<br>

<p><strong>get_infoQR</strong> function for to decode qrcode file. User must add only one value 'qrcode'. Value qrcode is address of qrcode file.
Example :

`qrcode = 'D:/Documents/QRcode/qr.png'`

`info = get_infQR(qrcode)`

`print(info)`

<h3>example generated qrcodes</h3>
<br>

<img src="https://raw.githubusercontent.com/alproger/pyqrcode/main/examples/3fc126b3-603c-4cfd-857a-029cdff71bd2.png"
     alt="image"
     style="float: left; margin-right: 10px;"
     width="100" height="100"
      />
<img src="https://raw.githubusercontent.com/alproger/pyqrcode/main/examples/5602a3ae-4c3d-42d3-9702-58a005b7271a.png"
     alt="image"
     style="float: left; margin-right: 10px;"
     width="100" height="100"
      />
<img src="https://raw.githubusercontent.com/alproger/pyqrcode/main/examples/b9cfef79-bbf5-46c9-85ad-ee11b29e074b.png"
     alt="image"
     style="float: left; margin-right: 10px;"
     width="100" height="100"
      />
<img src="https://raw.githubusercontent.com/alproger/pyqrcode/main/examples/c0d5ad20-49e1-4351-8303-da33c1b96af3.png"
     alt="image"
     style="float: left; margin-right: 10px;"
     width="100" height="100"
      />
<img src="https://raw.githubusercontent.com/alproger/pyqrcode/main/examples/d462700e-71ce-4016-9f3f-1b60b8da435d.png"
     alt="image"
     style="float: left; margin-right: 10px;"
     width="100" height="100"
      />
<img src="https://raw.githubusercontent.com/alproger/pyqrcode/main/examples/dee3178c-3769-454f-a177-68679e43f302.png"
     alt="image"
     style="float: left; margin-right: 10px;"
     width="100" height="100"
      />
</div>