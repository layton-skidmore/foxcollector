from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Fox, Toy
from .forms import HabitatsForm
from django.urls import reverse


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')



def foxes_index(request):
    foxes = Fox.objects.all()
    return render(request, 'foxes/index.html', 
    { 
        'foxes': foxes 
    }
)

def foxes_detail(request, fox_id):
  fox = Fox.objects.get(id=fox_id)
  id_list = fox.toys.all().values_list('id')
  toys_fox_doesnt_have = Toy.objects.exclude(id__in=id_list)
  habitats_form = HabitatsForm()
  return render(request, 'foxes/detail.html', {
    'fox': fox, 'habitats_form': habitats_form,
    'toys': toys_fox_doesnt_have
  })

def add_habitats(request, fox_id):
    form = HabitatsForm(request.POST)
    
    if form.is_valid():
        new_habitats = form.save(commit=False)
        new_habitats.fox = Fox.objects.get(id=fox_id) 
        new_habitats.save()
    return redirect('detail', fox_id=fox_id)

class FoxCreate(CreateView):
    model = Fox
    fields = ['name', 'species', 'description', 'age']

    def get_success_url(self):
        return reverse('detail', kwargs={'fox_id': self.object.id})

class FoxUpdate(UpdateView):
  model = Fox
  fields = ['species', 'description', 'age']

class FoxDelete(DeleteView):
  model = Fox
  success_url = '/foxes'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, fox_id, toy_id):
  Fox.objects.get(id=fox_id).toys.add(toy_id)
  return redirect('detail', fox_id=fox_id)

def unassoc_toy(request, fox_id, toy_id):
  Fox.objects.get(id=fox_id).toys.remove(toy_id)
  return redirect('detail', fox_id=fox_id)