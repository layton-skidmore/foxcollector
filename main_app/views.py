from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Fox, Toy
from .forms import HabitatsForm
from django.urls import reverse


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


@login_required
def foxes_index(request):
    foxes = Fox.objects.filter(user=request.user)
    return render(request, 'foxes/index.html', 
    { 
        'foxes': foxes 
    }
)

@login_required
def foxes_detail(request, fox_id):
  fox = Fox.objects.get(id=fox_id)
  id_list = fox.toys.all().values_list('id')
  toys_fox_doesnt_have = Toy.objects.exclude(id__in=id_list)
  habitats_form = HabitatsForm()
  return render(request, 'foxes/detail.html', {
    'fox': fox, 'habitats_form': habitats_form,
    'toys': toys_fox_doesnt_have
  })

@login_required
def add_habitats(request, fox_id):
    form = HabitatsForm(request.POST)
    
    if form.is_valid():
        new_habitats = form.save(commit=False)
        new_habitats.fox = Fox.objects.get(id=fox_id) 
        new_habitats.save()
    return redirect('detail', fox_id=fox_id)

class FoxCreate(LoginRequiredMixin, CreateView):
    model = Fox
    fields = ['name', 'species', 'description', 'age']

    def get_success_url(self):
        return reverse('detail', kwargs={'fox_id': self.object.id})
    
    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

class FoxUpdate(LoginRequiredMixin, UpdateView):
  model = Fox
  fields = ['species', 'description', 'age']

class FoxDelete(LoginRequiredMixin, DeleteView):
  model = Fox
  success_url = '/foxes'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys'

@login_required
def assoc_toy(request, fox_id, toy_id):
  Fox.objects.get(id=fox_id).toys.add(toy_id)
  return redirect('detail', fox_id=fox_id)

@login_required
def unassoc_toy(request, fox_id, toy_id):
  Fox.objects.get(id=fox_id).toys.remove(toy_id)
  return redirect('detail', fox_id=fox_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)