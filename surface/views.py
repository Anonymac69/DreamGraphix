from django.shortcuts import render
from .models import Pane


def index(request):
    panes = Pane.objects
    return render(request, 'surface/index.html', {'panes': panes})
