from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fox


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def foxes_index(request):
  return render(request, 'foxes/index.html', {
    'foxes': foxes
  })

def foxes_index(request):
    foxes = Fox.objects.all()
    return render(request, 'foxes/index.html', 
    { 
        'foxes': foxes 
    }
)

def foxes_detail(request, fox_id):
  fox = Fox.objects.get(id=fox_id)
  return render(request, 'foxes/detail.html', { 'fox': fox })

class FoxCreate(CreateView):
  model = Fox
  fields = ['name', 'species', 'description', 'age']
  success_url = '/foxes/{fox_id}'

class FoxUpdate(UpdateView):
  model = Fox
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['species', 'description', 'age']

class FoxDelete(DeleteView):
  model = Fox
  success_url = '/foxes'