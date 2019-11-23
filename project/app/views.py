from django.shortcuts import render, redirect
from .models import Para
from .forms import AppForm


def list_app(request):
    app = Para.objects.all()
    return render(request, 'app.html', {'app': app})

def create_app(request):
    form = AppForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_app')

    return render(request, 'app-form.html', {'form': form})

def update_app(request, id):
    app = Para.objects.get(id=id)
    form = AppForm(request.POST or None, instance=app)

    if form.is_valid():
        form.save()
        return redirect('list_app')
    return render(request, 'app-form.html', {'form': form, 'app': app})

def delete_app(request, id):
    app = Para.objects.get(id=id)

    if request.method == 'POST':
        app.delete()
        return redirect('list_app')
    return render(request, 'app-delete-confirm.html', {'app': app})

