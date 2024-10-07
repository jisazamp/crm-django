from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Client
from .forms import CreateClientForm


def home_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login success")
            return redirect("home")

        else:
            messages.error(request, "Login error")
            return redirect("home")

    context = {}
    clients = Client.objects.all()
    context["clients"] = clients
    return render(request, "home_page.html", context)


def client_details(request, pk):
    context = {}
    client = Client.objects.get(id=pk)
    context["client"] = client
    return render(request, "client_details.html", context)


def create_client(request):
    context = {}
    form = CreateClientForm(request.POST or None)
    context["form"] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente creado con éxito")
            return redirect("home")

    return render(request, "create_client.html", context)


def update_client(request, pk):
    context = {}
    client = Client.objects.get(id=pk)
    form = CreateClientForm(request.POST or None, instance=client)
    context['client'] = client
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente actualizado")
            return redirect("home")

    return render(request, "update_client.html", context)


def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    messages.success(request, "Cliente borrado")
    return redirect("home")
    


def logout_user(request):
    logout(request)
    messages.success(request, "Logout success")
    return redirect("home")
