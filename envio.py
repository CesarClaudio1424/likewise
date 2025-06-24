import procesamiento
import time
import urls

#------------------Iteración de rutas-----------------
def ejecucionurl (lista,links):
    routes = {}
    if (lista != "\u200b") & (lista != ""):
        routes['routes'] = lista
        response = procesamiento.envio(links, routes)
        if response == 200:
            mensaje = (f"{lista[0]} fue procesado.")
            color = ("green600")
            time.sleep(urls.TIEMPO)
            return mensaje, color
            #print(response)
            #time.sleep(0.3)
        else:
            mensaje = (f"{lista[0]} NO fue procesado.")
            color = ("red800")
            time.sleep(urls.TIEMPO)
            return mensaje, color
            #print(response)
            #time.sleep(0.3)

#------------------Iteración de Visitas-----------------
def ejecucionurlvisitas (lista,links):
    routes = {}
    if (lista != "\u200b") & (lista != ""):
        routes['visits'] = lista
        response = procesamiento.envio(links, routes)
        if response == 200:
            mensaje = (f"{lista[0]} fue procesado.")
            color = ("green600")
            time.sleep(urls.TIEMPO)
            return mensaje, color
            #print(response)
            #time.sleep(0.3)
        else:
            mensaje = (f"{lista[0]} NO fue procesado.")
            color = ("red800")
            time.sleep(urls.TIEMPO)
            return mensaje, color
            #print(response)
            #time.sleep(0.3)