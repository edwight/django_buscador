from principal.models import ubicacion
from django.shortcuts import render_to_response
from principal.forms import Buscar_Mapa
from django.template import RequestContext
from django.db.models import Q

def ubicacion_view(request):
    formulario = Buscar_Mapa()

    #busqueda = '')formulario.Busqueda
    #busqueda = ''
    if request.method == "POST":
        formulario = Buscar_Mapa(request.POST)
        #formulario.is_valid():

        #busqueda = formulario.cleaned_data['busqueda']
        busqueda = str(request.POST.get('Busqueda',''))

        ubicaciones= ubicacion.objects.filter( Q(localidade__startswith= busqueda) | Q(parroquia__startswith= busqueda) | Q(municipios__startswith= busqueda))
        #ubicaciones = ubicacion.objects.filter(localidade = busqueda)
        #ubicaciones = ubicacion.objects.filter(localidade = busqueda, parroquia = busqueda)

        #int(request.POST.get('num_emp', ''))
    else:
        ubicaciones = ubicacion.objects.all()
    #filter(municipio = formulario.busqueda)
    ctx = {'lista':ubicaciones,'form':formulario}
    #return render_to_response('principal.html',ctx,context_instance=RequestContext(request))
    return render_to_response('principal.html',ctx,context_instance=RequestContext(request))
    #return render_to_response('principal.html',{'lista':ubicaciones })

#def formulario_view(request):
    #formulario = Buscar_Mapa
    #if formulario.is_Valid():
        #busqueda = formulario.cleaned_data['Busqueda']
        #titulo = formulario.cleaned_data['Titulo']
        #ubicaciones = ubicacion.objects.all()

    ##return render_to_response('principal.html',{'form':formulario})
"""
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            topic = form.clean_data['topic']
            message = form.clean_data['message']
            sender = form.clean_data.get('sender', 'noreply@example.com')

    form = ContactForm()
    return render_to_response('contact.html', {'form': form})

def ejemplo_view(request):
    form= UbicacionForm()

    if request.method == "POST":
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()

            ubicaciones =  form.objects.all()
            ctx = {'form':form, 'listas':ubicaciones}
            return render_to_response('principal.html',ctx,context_instance=RequestContext(request))
        else:
            ubicaciones = ubicacion.objects.all()
            ctx = {'form':form, 'listas':ubicaciones}
            return render_to_response('principal.html',ctx,context_instance=RequestContext(request))
"""
