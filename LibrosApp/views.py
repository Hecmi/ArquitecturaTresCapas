# nombre_de_la_aplicacion/views.py
import requests,json
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest,HttpResponseRedirect,QueryDict
from django.urls import reverse

from .models import Cliente, Sucursales, Producto_Sucursales
#BUSCAR PRODUCTO
def buscar_producto(request):
    if request.method == 'POST':
        texto_buscar = request.POST.get('texto_buscar')
        print(texto_buscar)
        # Hacer una solicitud a la API para obtener los datos de la sucursal
        api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/producto/buscar'
        response = requests.post(api_url, data=texto_buscar, headers={'Content-Type': 'text/plain'})

        if response.status_code == 200:
            if response.text != '':
                productos = response.json()
                return render(request, 'ver_producto_sucursales.html', {'producto_sucursales': productos})
        
        return redirect('ver_producto_sucursales')
#BUSCAR CLIENTE
def buscar_cliente(request):
    if request.method == 'POST':
        texto_buscar = request.POST.get('texto_buscar')
        print(texto_buscar)
        # Hacer una solicitud a la API para obtener los datos de la sucursal
        api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/cliente/buscar'
        response = requests.post(api_url, data=texto_buscar, headers={'Content-Type': 'text/plain'})
        
        print(response.status_code)
        if response.status_code == 200:
            if response.text != '':
                cliente = response.json()
                return render(request, 'ver_cliente.html', {'clientes': cliente})
        
        return redirect('ver_cliente')
#BUSCAR SUCURSAL
def buscar_sucursal(request):
    if request.method == 'POST':
        texto_buscar = request.POST.get('texto_buscar')
        print(texto_buscar)
        # Hacer una solicitud a la API para obtener los datos de la sucursal
        api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/sucursal/buscar'
        response = requests.post(api_url, data=texto_buscar, headers={'Content-Type': 'text/plain'})
        
        print(response.status_code)
        if response.status_code == 200:
            if response.text != '':
                sucursales = response.json()
            return render(request, 'ver_sucursales.html', {'sucursales': sucursales})
        
        return redirect('ver_sucursales')
#------------------------------------------------------------------------------------------------------------------------------
def agregarcliente(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        identificacion = request.POST.get('identificacion') 
        id_sucursal=request.POST.get('id_sucursal') # Corregir el nombre del campo
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        

        # URL de la API para insertar clientes
        api_url = "http://26.48.208.162:8080/LibrosDistribuido/api/cliente/insertar"

        try:
            # Datos a enviar a la API
            data = {
                'identificacion': identificacion,
                'id_sucursal':id_sucursal,
                'nombres': nombres,
                'apellidos': apellidos,
                'direccion': direccion,
                'telefono': telefono,
                'email':email,
                'fecha_nacimiento': fecha_nacimiento
                
            }

            # Realizar una solicitud POST a la API
            response = requests.post(api_url, json={'data': data}, headers={'Content-Type': 'application/json'})

            # Verificar si la solicitud fue exitosa (código 200)
            if response.status_code == 200:
                # Redirigir a la página de éxito o a la lista de sucursales
                return redirect('ver_cliente')
            else:
                # Si la solicitud no fue exitosa, enviar una respuesta BadRequest con el mensaje de error
                return HttpResponseBadRequest(f"Error al agregar cliente. Código de respuesta: {response.status_code}")

        except requests.RequestException as e:
            # Manejar cualquier excepción que pueda ocurrir durante la solicitud
            # Enviar una respuesta BadRequest con el mensaje de error
            return HttpResponseBadRequest(f"Error al conectar con la API: {e}")
    else:
        # Si la solicitud no es POST, mostrar el formulario para agregar sucursales
        return render(request, 'agregarcliente.html')
#---------------------------------------------------------------------------------------------
def agregarsucursales(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        pais = request.POST.get('pais')
        ciudad = request.POST.get('ciudad')
        direccion = request.POST.get('direccion')  # Corregir el nombre del campo
        descripcion = request.POST.get('descripcion')

        # URL de la API para insertar sucursal
        api_url = "http://26.48.208.162:8080/LibrosDistribuido/api/sucursal/insertar"

        try:
            # Datos a enviar a la API
            data = {
                'pais': pais,
                'ciudad': ciudad,
                'direccion': direccion,  # Corregir el nombre del campo
                'descripcion': descripcion
            }

            # Realizar una solicitud POST a la API
            response = requests.post(api_url, json={'data': data}, headers={'Content-Type': 'application/json'})

            # Verificar si la solicitud fue exitosa (código 200)
            if response.status_code == 200:
                # Redirigir a la página de éxito o a la lista de sucursales
                return redirect('ver_sucursales')
            else:
                # Si la solicitud no fue exitosa, enviar una respuesta BadRequest con el mensaje de error
                return HttpResponseBadRequest(f"Error al agregar sucursal. Código de respuesta: {response.status_code}")

        except requests.RequestException as e:
            # Manejar cualquier excepción que pueda ocurrir durante la solicitud
            # Enviar una respuesta BadRequest con el mensaje de error
            return HttpResponseBadRequest(f"Error al conectar con la API: {e}")
    else:
        # Si la solicitud no es POST, mostrar el formulario para agregar sucursales
        return render(request, 'agregarsucursales.html')
#-------------------------------------------------------------------------------------------------------------------  
#Agregar Producto
def producto_sucursales(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        id_sucursal = request.POST.get('id_sucursal') 
        producto=request.POST.get('producto') # Corregir el nombre del campo
        cantidad = request.POST.get('cantidad')
        unidad_medida = request.POST.get('unidad_medida')
        precio_unitario = request.POST.get('precio_unitario')
        iva = request.POST.get('iva')
        descuento = request.POST.get('descuento')
        descripcion = request.POST.get('descripcion')
        

        # URL de la API para insertar productos
        api_url = "http://26.48.208.162:8080/LibrosDistribuido/api/producto/insertar"

        try:
            # Datos a enviar a la API
            data = {
                'id_sucursal': id_sucursal,
                'producto':producto,
                'cantidad': cantidad,
                'unidad_medida': unidad_medida,
                'precio_unitario': precio_unitario,
                'iva': iva,
                'descuento':descuento,
                'descripcion': descripcion
                
            }

            # Realizar una solicitud POST a la API
            response = requests.post(api_url, json={'data': data}, headers={'Content-Type': 'application/json'})

            # Verificar si la solicitud fue exitosa (código 200)
            if response.status_code == 200:
                # Redirigir a la página de éxito o a la lista de sucursales
                return redirect('ver_producto_sucursales')
            else:
                # Si la solicitud no fue exitosa, enviar una respuesta BadRequest con el mensaje de error
                return HttpResponseBadRequest(f"Error al agregar producto. Código de respuesta: {response.status_code}")

        except requests.RequestException as e:
            # Manejar cualquier excepción que pueda ocurrir durante la solicitud
            # Enviar una respuesta BadRequest con el mensaje de error
            return HttpResponseBadRequest(f"Error al conectar con la API: {e}")
    else:
        # Si la solicitud no es POST, mostrar el formulario para agregar sucursales
        return render(request, 'producto_sucursales.html')
#---------------------------------------------------------------------------------------------   
def obtener_datos_sucursal(id_sucursal):
    # Hacer una solicitud a la API para obtener los datos de la sucursal
    api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/sucursal/get/{id_sucursal}'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        datos_sucursal = response.json()
        return datos_sucursal
    else:
        return None

def actualizar_datos_sucursal(nuevos_datos):
    # Hacer una solicitud a la API para actualizar los datos de la sucursal
    api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/sucursal/editar'
    response = requests.put(api_url,  json={'data': nuevos_datos}, headers={'Content-Type': 'application/json'})

    print(response)

    print(nuevos_datos)
    if response.status_code == 200:
        return True
    else:
        return False
    
def editar_sucursal(request, id_sucursal):
    if request.method == 'GET':
        # Obtener los datos de la sucursal desde la API
        datos_sucursal = obtener_datos_sucursal(id_sucursal)

        if datos_sucursal:
            # Renderizar el formulario con los datos de la sucursal
            return render(request, 'modificar_sucursal.html', context={'sucursal': datos_sucursal})
        else:
            # Manejar el caso en que no se puedan obtener los datos de la sucursal
            return render(request, 'LibrosApp/error.html', {'mensaje': 'Error al obtener datos de la sucursal'})

    else:
        nuevos_datos = {
            'id_sucursal': request.POST.get('id_sucursal'),
            'pais': request.POST.get('pais'),
            'ciudad': request.POST.get('ciudad'),
            'direccion': request.POST.get('direccion'),
            'descripcion': request.POST.get('descripcion')
        }
        
        # Actualizar los datos de la sucursal
        actualizar_datos_sucursal(nuevos_datos)
        return redirect('ver_sucursales')
        # else:
        #     return HttpResponseBadRequest("Error al actualizar datos de la sucursal")

#-----------------------------------------------------------------
def obtener_datos_cliente(identificacion):
    # Hacer una solicitud a la API para obtener los datos de la sucursal
    api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/cliente/get/{identificacion}'
    response = requests.get(api_url)
    print(api_url)
    
    if response.status_code == 200:
        datos_cliente = response.json()
        return datos_cliente
    else:
        return None

def actualizar_datos_cliente(nuevos_datos2):
    # Hacer una solicitud a la API para actualizar los datos de la sucursal
    api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/cliente/editar'
    response = requests.put(api_url,  json={'data': nuevos_datos2}, headers={'Content-Type': 'application/json'})

    print(response)

    print(nuevos_datos2)
    if response.status_code == 200:
        return True
    else:
        return False
    
def editar_cliente(request, identificacion):
    if request.method == 'GET':
        # Obtener los datos del cliente desde la API
        datos_cliente = obtener_datos_cliente(identificacion)

        if datos_cliente:
            # Renderizar el formulario con los datos del cliente
            return render(request, 'modificar_cliente.html', context={'cliente': datos_cliente})
        else:
            # Manejar el caso en que no se puedan obtener los datos del cliente
            return render(request, 'LibrosApp/error.html', {'mensaje': 'Error al obtener datos del cliente'})

    else:
        nuevos_datos2 = {
            'identificacion': request.POST.get('identificacion'),
            'id_sucursal': request.POST.get('id_sucursal'),
            'nombres': request.POST.get('nombres'),
            'apellidos': request.POST.get('apellidos'),
            'direccion': request.POST.get('direccion'),
            'email': request.POST.get('email'),
            'telefono': request.POST.get('telefono'),
            'fecha_nacimiento': request.POST.get('fecha_nacimiento')
        }
        
        # Actualizar los datos de la sucursal
        actualizar_datos_cliente(nuevos_datos2)
        return redirect('ver_cliente')
        # else:
        #     return HttpResponseBadRequest("Error al actualizar datos de la sucursal")
#---------------------------------------------------------------------
def obtener_datos_producto_sucursales(id_producto_sucursal):
    # Hacer una solicitud a la API para obtener los datos de la sucursal
    api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/producto/get/{id_producto_sucursal}'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        datos_producto = response.json()
        return datos_producto
    else:
        return None

def actualizar_datos_producto_sucursales(nuevos_datos):
    # Hacer una solicitud a la API para actualizar los datos de la sucursal
    api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/producto/editar'
    response = requests.put(api_url,  json={'data': nuevos_datos}, headers={'Content-Type': 'application/json'})

    print(response)

    print(nuevos_datos)
    if response.status_code == 200:
        return True
    else:
        return False
    
def editar_producto_sucursales(request, id_producto_sucursal):
    if request.method == 'GET':
        # Obtener los datos de la sucursal desde la API
        datos_producto = obtener_datos_producto_sucursales(id_producto_sucursal)

        if datos_producto:  
            # Renderizar el formulario con los datos de la sucursal
            return render(request, 'modificar_producto_sucursales.html', context={'producto': datos_producto})
        else:
            # Manejar el caso en que no se puedan obtener los datos de la sucursal
            return render(request, 'LibrosApp/error.html', {'mensaje': 'Error al obtener datos de la sucursal'})

    else:
        nuevos_datos = {
            'id_producto_sucursal': request.POST.get('id_producto_sucursal'),
            'id_sucursal': request.POST.get('id_sucursal'),
            'producto': request.POST.get('producto'),
            'cantidad': request.POST.get('cantidad'),
            'unidad_medida': request.POST.get('unidad_medida'),
            'precio_unitario': request.POST.get('precio_unitario'),
            'iva': request.POST.get('iva'),
            'descuento': request.POST.get('descuento'),
            'descripcion': request.POST.get('descripcion')
        }
        
        # Actualizar los datos de la sucursal
        actualizar_datos_producto_sucursales(nuevos_datos)
        return redirect('ver_producto_sucursales')
#-------------------------------------------------------------------
def eliminar_datos_sucursal(id_sucursal):
    # Hacer una solicitud a la API para actualizar los datos de la sucursal
    api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/sucursal/eliminar/{id_sucursal}'
    response = requests.delete(api_url)

    print(api_url, response.status_code)
    if response.status_code == 200:
        return True
    else:
        return False
     

def eliminar_sucursal(request, id_sucursal):    
    eliminar_datos_sucursal(id_sucursal)
    return redirect('ver_sucursales')
#-----------------------------------------------------------------------------------
def eliminar_datos_cliente(identificacion):
    # Hacer una solicitud a la API para actualizar los datos de la sucursal
    api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/cliente/eliminar/{identificacion}'
    response = requests.delete(api_url)

    print(api_url, response.status_code)
    if response.status_code == 200:
        return True
    else:
        return False
     

def eliminar_cliente(request, identificacion):    
    eliminar_datos_cliente(identificacion)
    return redirect('ver_cliente')
#----------------------------------------------------------------------------------------------------       
def eliminar_datos_producto(id_producto_sucursal):
    # Hacer una solicitud a la API para actualizar los datos de la sucursal
    api_url = f'http://26.48.208.162:8080/LibrosDistribuido/api/producto/eliminar/{id_producto_sucursal}'
    response = requests.delete(api_url)

    print(api_url, response.status_code)
    if response.status_code == 200:
        return True
    else:
        return False
     

def eliminar_producto(request, id_producto_sucursal):    
    eliminar_datos_producto(id_producto_sucursal)
    return redirect('ver_producto_sucursales')

#--------------------------------------------------------------------------------------------------


def ver_producto_sucursales(request):
    # URL de la API
    api_url = "http://26.48.208.162:8080/LibrosDistribuido/api/producto/listar"

    try:
        # aqui lo que se esta haciendo es realizar una solicitud get a la api
        response = requests.get(api_url)

        # Verificar si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            # Convertir la respuesta JSON a un diccionario Python
            producto_sucursales = response.json()

            # Renderizar la plantilla con los datos de la API
            return render(request, 'ver_producto_sucursales.html', {'producto_sucursales': producto_sucursales})
        else:
            # Si la solicitud no fue exitosa, mostrar un mensaje de error
            return render(request, 'error.html', {'mensaje': f"Error al obtener datos de la API. Código de respuesta: {response.status_code}"})

    except requests.RequestException as e:
        # Manejar cualquier excepción que pueda ocurrir durante la solicitud
        return render(request, 'error.html', {'mensaje': f"Error al conectar con la API: {e}"})


#---------------------------------------------------------------------------------------
def ver_cliente(request):
    # URL de la API
    api_url = "http://26.48.208.162:8080/LibrosDistribuido/api/cliente/listar"

    try:
        # aqui lo que se esta haciendo es realizar una solicitud get a la api
        response = requests.get(api_url)

        # Verificar si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            # Convertir la respuesta JSON a un diccionario Python
            clientes = response.json()

            # Renderizar la plantilla con los datos de la API
            return render(request, 'ver_cliente.html', {'clientes': clientes})
        else:
            # Si la solicitud no fue exitosa, mostrar un mensaje de error
            return render(request, 'error.html', {'mensaje': f"Error al obtener datos de la API. Código de respuesta: {response.status_code}"})

    except requests.RequestException as e:
        # Manejar cualquier excepción que pueda ocurrir durante la solicitud
        return render(request, 'error.html', {'mensaje': f"Error al conectar con la API: {e}"})

def ver_sucursales(request):
    # URL de la API
    api_url = "http://26.48.208.162:8080/LibrosDistribuido/api/sucursal/listar"

    try:
        # aqui lo que se esta haciendo es realizar una solicitud get a la api
        response = requests.get(api_url)

        # Verificar si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            # Convertir la respuesta JSON a un diccionario Python
            sucursales = response.json()

            # Renderizar la plantilla con los datos de la API
            return render(request, 'ver_sucursales.html', {'sucursales': sucursales})
        else:
            # Si la solicitud no fue exitosa, mostrar un mensaje de error
            return render(request, 'error.html', {'mensaje': f"Error al obtener datos de la API. Código de respuesta: {response.status_code}"})

    except requests.RequestException as e:
        # Manejar cualquier excepción que pueda ocurrir durante la solicitud
        return render(request, 'error.html', {'mensaje': f"Error al conectar con la API: {e}"})