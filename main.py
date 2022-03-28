from Definições import module1
import requests
import json
from requests.auth import HTTPBasicAuth

    #r=requests.get('http://10.19.1.230:8080/api/faces?offset=0&portion=50&module=Complete', auth=HTTPBasicAuth('root', ''))
    #print(r.json())


for n in range(500,1350):
        f=module1.Functions(n)
        url='http://10.19.1.230:8080/api/faces?module=light'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data= {
        "first_name": f.name_use_cpf()[1],
        "face_images": [f.pic_to_base64()],
        "external_id": f.name_use_cpf()[0],
        }
        r = requests.post(url, data=json.dumps(data), headers=headers,auth=HTTPBasicAuth('root', ''))
        print(r)