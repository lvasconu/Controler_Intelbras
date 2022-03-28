import requests
import json
from requests.auth import HTTPBasicAuth
import base64
import os, sys
from string import digits
dirs=os.listdir("C:/Users/Lucas Morais/source/repos/API_Ecortex/images/")
from Definições import module1

class Functions:

    def __init__(self, n):
       self.n=n
    
    def only_numerics(seq):
        seq_type= type(seq)
        return seq_type().join(filter(seq_type.isdigit, seq))

    
    def replace_all(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text



   
    def pic_to_base64(self):
        pic=dirs[self.n]
        path="C:/Users/Lucas Morais/source/repos/API_Ecortex/images/"
        with open(path+pic, "rb") as img_file:
         b64_string = base64.b64encode(img_file.read())
        return b64_string.decode('utf-8')

    def user_cpf(seq):
        dirs=os.listdir("C:/Users/Lucas Morais/source/repos/API_Ecortex/images/")
        x=module1.Functions.only_numerics(dirs[seq])
        return x


    
    def name_use_cpf(self):
        urls="http://10.19.1.222:5865/GlobalAccess/api/RH?cpf="
        data="&data=28%2F01%2F2022"
        x=requests.get(urls+module1.Functions.user_cpf(self.n)+data)
        if(x.status_code==400):
            return "User not in database"
        else:
            y=x.json()
            y1=y['cpf']
            y2=y['name']
            return y1,y2



