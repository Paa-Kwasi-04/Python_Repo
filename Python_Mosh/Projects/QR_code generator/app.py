import qrcode

data = input('Enter the URL: ').strip()
file_name = input('Enter a filename: ').strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(file_name)

print(f'QR code saved as {file_name}')
