from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Postagen

def index(request):
    return render(request, 'index.html', {})

def assistsocial(request):
    return render(request, 'assistsocial.html', {})

def atendimento_fr(request):
    return render(request, 'atendimento_fr.html', {})

def bazar(request):
    return render(request, 'bazar.html', {})

def blog(request):
    object_list = Postagen.objects.all()[::-1]
    paginator = Paginator(object_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
       paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 

    context = {
        # 'object_list': object_list,
        'object_list': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'blog.html', context)

def comarte(request):
    return render(request, 'comarte.html', {})

def consolarte(request):
    return render(request, 'consolarte.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST["user_name"]
        email = request.POST['user_email']    
        message = request.POST['user_message']
        
        send_mail(
            name,
            f'Email enviado através do website \nMensagem de: {name} \nEmail: {email}\n\nMensagem: ' + message,
            email,
            ['contato@casaespiritaoconsolador.com.br']
        )

        return render(request, 'contact.html', {'name' : name})   
    else:
        return render(request, 'contact.html', {})


def doacoes(request):
    return render(request, 'doacoes.html', {})

def estudos(request):
    return render(request, 'estudos.html', {})

def eventos(request):
    return render(request, 'eventos.html', {})

def evang_infantil(request):
    return render(request, 'evang_infantil.html', {})

def mocidade(request):
    return render(request, 'mocidade.html', {})
