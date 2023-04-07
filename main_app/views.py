from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Upgrade
from .forms import UpdatesForm

# Create your views here.



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def guitars_index(request):
    guitar = Guitar.objects.all()
    return render(request, 'guitars/index.html', {
        'guitars': guitars
    })

def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    id_list = guitar.upgrade.all().values_list('id')
    upgrade_guitar_doesnt_have = Upgrade.objects.exclude(id__in=id_list)
    updates_form = UpdatesForm()
    return render(request, 'guitars/detail.html', {
        'guitars': guitars , 'updates_form' : updates_form, 'upgrade' : upgrade_guitar_doesnt_have
    })

class GuitarCreate(CreateView):
    model = Guitar
    fields = ['make', 'model', 'year', 'description']

class GuitarUpdate(UpdateView):
  model = Guitar
  fields = ['model', 'year', 'description']

class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars'


def add_updates(request, guitar_id):
   form = UpdatesForm(request.POST)
   
   if form.is_valid():
    new_updates = form.save(commit=False)
    new_updates.guitar_id = guitar_id
    new_updates.save()
    return redirect('detail', guitar_id=guitar_id)
   

class UpgradeList(ListView):
  model = Upgrade

class UpgradeDetail(DetailView):
  model = Upgrade

class UpgradeCreate(CreateView):
  model = Upgrade
  fields = '__all__'

class UpgradeUpdate(UpdateView):
  model = Upgrade
  fields = ['name', 'description']

class UpgradeDelete(DeleteView):
  model = Upgrade
  success_url = '/upgrade'



def assoc_upgrade(request, guitar_id, upgrade_id):
  
  Guitar.objects.get(id=guitar_id).upgrade.add(upgrade_id)
  return redirect('detail', guitar_id=guitar_id)


def delete_upgrade(request, guitar_id, upgrade_id):
  Guitar.objects.get(id=guitar_id).upgrade.remove(upgrade_id)
  return redirect('detail', guitar_id=upgrade_id )
