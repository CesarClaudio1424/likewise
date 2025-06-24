import urls

#------------------Asignacion de urls-----------------
def links (cuenta):
    #print (cuenta)
    if cuenta == 'Telefonica':
        urlcreacion = urls.CREACIONTELEFONICA
        urlinicio = urls.INICIOTELEFONICA
        urlchekout = urls.CHECKOUTTELEFONICA
        urlexclucion = urls.EXCLUIRTELEFONICA
        return urlcreacion, urlinicio, urlchekout, urlexclucion
    
    if cuenta == 'Entel':
        urlcreacion = urls.CREACIONENTEL
        urlinicio = urls.INICIOENTEL
        urlchekout = urls.CHECKOUTENTEL
        urlexclucion = urls.EXCLUIRENTEL
        return urlcreacion, urlinicio, urlchekout, urlexclucion

    if cuenta == 'Omnicanalidad':
        urlcreacion = urls.CREACIONOMNI
        urlinicio = urls.INICIOOMNI
        urlchekout = urls.CHECKOUTOMNI
        urlexclucion = urls.EXCLUIROMNI
        return urlcreacion, urlinicio, urlchekout, urlexclucion

    if cuenta == 'Biobio':
        urlcreacion = urls.CREACIONBIOBIO
        urlinicio = urls.INICIOBIOBIO
        urlchekout = urls.CHECKOUTBIOBIO
        urlexclucion = urls.EXCLUIRBIOBIO
        return urlcreacion, urlinicio, urlchekout, urlexclucion