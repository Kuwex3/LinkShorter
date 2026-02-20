import qrcode

def generate_QR_code(code):
    a = qrcode.make(f"http://localhost:8000/{code}")
    a.save(f"./src/QR{code}.png")