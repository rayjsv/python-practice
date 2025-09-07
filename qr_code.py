import qrcode

website_link = input("Enter text or link: ")

qr = qrcode.QRCode(version = 1, box_size = 5, border = 1)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'maroon', back_color = 'white')
img.save('my_qr.png')

img.show()