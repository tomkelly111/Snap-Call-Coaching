from django.shortcuts import render
from .models import Coach

# Create your views here.


def coach_bios(request):
    """a view to return coaches page"""

    coaches = Coach.objects.all()

    context = {
        'coaches': coaches
    }

    return render(request, 'coaches/coach_bios.html', context)
