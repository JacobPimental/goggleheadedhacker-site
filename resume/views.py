from django.shortcuts import render, get_object_or_404
from .models import Resume
from django.views.decorators.csrf import csrf_protect
# Create your views here.
@csrf_protect
def resume(request):
    resume = get_object_or_404(Resume, pk=1)
    return render(request, 'resume/about.html', {'resume':resume,
                                                 'title':'About Me'})
