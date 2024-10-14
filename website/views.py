from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Client
from .forms import CreateClientForm


# Vista principal de la página de inicio
def home_page(request):
    # Verifica si el método de la solicitud es POST, lo que indica un intento
    # de login
    if request.method == "POST":
        # Obtiene el nombre de usuario del formulario
        username = request.POST["username"]
        # Obtiene la contraseña del formulario
        password = request.POST["password"]
        user = authenticate(
            request, username=username, password=password
        )  # Autentica al usuario

        if user is not None:
            # Si la autenticación es exitosa, inicia sesión
            login(request, user)
            # Muestra un mensaje de éxito
            messages.success(request, "Login success")
            return redirect("home")  # Redirige a la página de inicio

        else:
            # Si falla, muestra un mensaje de error
            messages.error(request, "Login error")
            # Redirige nuevamente a la página de inicio
            return redirect("home")

    # Si no es una solicitud POST, simplemente renderiza la página con los
    # clientes existentes
    context = {}
    clients = Client.objects.all()  # Obtiene todos los clientes de la base de datos
    context["clients"] = clients  # Los agrega al contexto
    # Renderiza el template con los datos
    return render(request, "home_page.html", context)


# Vista para ver los detalles de un cliente específico
def client_details(request, pk):
    context = {}
    # Obtiene un cliente específico por su ID
    client = Client.objects.get(id=pk)
    context["client"] = client  # Lo agrega al contexto
    # Renderiza el template con los detalles del cliente
    return render(request, "client_details.html", context)


# Vista para crear un nuevo cliente
def create_client(request):
    context = {}
    # Crea un formulario para crear un cliente
    form = CreateClientForm(request.POST or None)
    context["form"] = form  # Agrega el formulario al contexto

    if request.method == "POST":  # Si la solicitud es POST, intenta guardar el cliente
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda el nuevo cliente en la base de datos
            # Muestra un mensaje de éxito
            messages.success(request, "Cliente creado con éxito")
            return redirect("home")  # Redirige a la página de inicio

    # Renderiza el template para crear clientes
    return render(request, "create_client.html", context)


# Vista para actualizar la información de un cliente existente
def update_client(request, pk):
    context = {}
    client = Client.objects.get(id=pk)  # Obtiene el cliente por su ID
    # Crea un formulario con los datos del cliente
    form = CreateClientForm(request.POST or None, instance=client)
    context["client"] = client  # Agrega el cliente al contexto
    context["form"] = form  # Agrega el formulario al contexto

    if (
        request.method == "POST"
    ):  # Si la solicitud es POST, intenta actualizar el cliente
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda los cambios en la base de datos
            # Muestra un mensaje de éxito
            messages.success(request, "Cliente actualizado")
            return redirect("home")  # Redirige a la página de inicio

    # Renderiza el template para actualizar clientes
    return render(request, "update_client.html", context)


# Vista para eliminar un cliente
def delete_client(request, pk):
    client = Client.objects.get(id=pk)  # Obtiene el cliente por su ID
    client.delete()  # Elimina el cliente de la base de datos
    messages.success(request, "Cliente borrado")  # Muestra un mensaje de éxito
    return redirect("home")  # Redirige a la página de inicio


# Vista para cerrar la sesión del usuario
def logout_user(request):
    logout(request)  # Cierra la sesión del usuario
    messages.success(request, "Logout success")  # Muestra un mensaje de éxito
    return redirect("home")  # Redirige a la página de inicio
