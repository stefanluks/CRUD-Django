from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Lista, Tarefa, UsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def Home(request):
    if request.user.is_authenticated:
        lista = Lista.objects.filter(dono = request.user)
        return render(request, 'home.html', {'lista':lista})
    else:
        return redirect("login")

def Concluir(request,id):
    if request.user.is_authenticated:
        tarefa = Tarefa.objects.get(pk=id)
        tarefa.concluido = not tarefa.concluido
        tarefa.save()
        return redirect("home")
    else:
        return redirect("login")

def Excluir(request,id):
    if request.user.is_authenticated and Tarefa.objects.filter(pk=id):
        tarefa = Tarefa.objects.get(pk=id)
        tarefa.delete()
        return redirect("home")
    else:
        return redirect("login")

def ExcluirLista(request,id):
    if request.user.is_authenticated and Lista.objects.filter(pk=id):
        lista = Lista.objects.get(pk=id)
        lista.delete()
        return redirect("home")
    else:
        return redirect("login")

def CriarTarefa(request):
    if request.user.is_authenticated and request.method == "POST":
        print(request.POST)
        if Lista.objects.filter(pk=int(request.POST["lista_id"])):
            lista = Lista.objects.get(pk=int(request.POST["lista_id"]))
            tarefa = Tarefa()
            tarefa.texto = request.POST["texto"]
            tarefa.pertence = lista
            tarefa.save()
            return redirect("home")
    else:
        return redirect("login")

def CriarLista(request):
    if request.user.is_authenticated and request.method == "POST":
        lista = Lista()
        lista.nome = request.POST["nome"]
        lista.cor = request.POST["cor"]
        lista.dono = request.user
        lista.save()
        return redirect("home")
    else:
        return redirect("login")
    
def CriarConta(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nuser = User()
            nuser.first_name = request.POST["first_name"]
            nuser.username = request.POST["username"]
            nuser.password = make_password(request.POST["password"])
            nuser.save()
            return redirect("home")
        else:
            return HttpResponse('''
                <h2>Houve algum problema com as informações!</h2>
                <h5>tente novamente <a href="../">voltar</a> </h5>
            ''')
    else:
        form = UsuarioForm()
        return render(request, 'registration/cadastrar.html', {"form":form})