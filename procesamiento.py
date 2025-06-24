import requests

#------------------Procesamiento de Webhook-----------------
def envio(url, envio):
    #print(envio)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json = envio)
    #payload = response.json()
    #print(payload)
    return response.status_code