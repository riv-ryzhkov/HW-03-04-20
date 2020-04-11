from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from groupes.models import Groupe


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
            return HttpResponseRedirect('/groupes-list/')
    elif request.method == 'GET':
        form = form_class()
    return render(request, 'groupe-create.html', {'create_form': form, 'one': 'Groupe'})


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