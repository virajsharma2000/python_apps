import streamlit as st
import qrcode
import io

def generate_payment_qrcode(upi, amount = None):
 if amount is None:
  url = f'upi://pay?pa={upi}'

 else:
  url = f'upi://pay={upi}&am={amount}'

 payment_qrcode = qrcode.make(url)
 
 with io.BytesIO() as output:
  payment_qrcode.save(output, format="PNG")

  return output.getvalue()
 

st.write('<h1>Generate payment qrcode within seconds!!</h1>', unsafe_allow_html = True)

upi = st.text_input('Enter upi your id')
amount = st.text_input('Enter amount (optional)')

if st.button('Generate QRcode'):
 if amount:
  payment_qrcode = generate_payment_qrcode(upi, amount = amount)

 else:
  payment_qrcode = generate_payment_qrcode(upi)
 
 print(payment_qrcode)
 st.image(payment_qrcode)


