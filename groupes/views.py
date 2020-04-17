from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from groupes.models import Groupe
from django.urls import reverse


def Groupe_(request):
    g = Groupe.objects.create(name='Ivan', head='Petrov', email='erw@gmail.com', phone='77686565')
    return render(request, g.name + g.head + g.email + g.phone)


def clear(request):
    return


def create_groupe(request):
    from groupes.forms import GroupeForm
    form_class = GroupeForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groupes-list'))
    elif request.method == 'GET':
        form = form_class(initial={'name': 'groupe', 'head': 'teacher', 'email': 'wrww@gmail.com', 'phone': '875759'})
    return render(request, 'groupe-create.html', {'create_form': form, 'one': 'Groupe'})

def groupe_edit(request, pk):
    from groupes.forms import GroupeForm
    from django.http import Http404
    form_class = GroupeForm

    try:
        groupe = Groupe.objects.get(id=pk)
    except Groupe.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = form_class(request.POST, instance=groupe)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groupes-list'))
    elif request.method == 'GET':
        form = form_class(instance=groupe)
    return render(request, 'groupe-edit.html', {'form': form, 'one': 'Groupe'})

def groupes_list(request):
    groupes = Groupe.objects.all()

    head_to_filter = request.GET.get('head')
    name_to_filter = request.GET.get('name')
    if head_to_filter:
        groupes = groupes.filter(heade__startswith=head_to_filter)

    if head_to_filter:
        groupes = groupes.filter(name__startswith=name_to_filter)

    sorting = request.GET.get('order-by')
    if sorting:
        groupes = groupes.order_by(*sorting.split(','))

    return render(request, 'groupes-list.html', {'groupes': groupes})