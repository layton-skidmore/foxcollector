from django.shortcuts import render

foxes = [
  {'name': 'Felix', 'species': 'Arctic Fox', 'description': 'Fearless leader', 'age': 5},
  {'name': 'Hans', 'species': 'Fennec Fox', 'description': 'Playful little guy and twin of Frans', 'age': 2},
  {'name': 'Frans', 'species': 'Fennec Fox', 'description': 'Food is his passion. Twin of Hans', 'age': 2},
]


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def foxes_index(request):
  return render(request, 'foxes/index.html', {
    'foxes': foxes
  })