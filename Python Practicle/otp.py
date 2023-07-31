from twilio.rest import Client
import math as m
import random as r
def OTPgen() :  
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = "" 
    varlen= len(string) 
    for i in range(6) : 
        OTP += string[m.floor(r.random() * varlen)] 
  
    return (OTP)
otp=OTPgen()
print(otp)
account_sid = 'AC6fb8ed3e638b26a6f70f2674268dfc51'
auth_token = 'fe014271c5d0930cd5857b79623c2101'
client = Client(account_sid, auth_token)
message = client.messages.create(body=otp,from_='+12019755091',to='+918802012379') 
