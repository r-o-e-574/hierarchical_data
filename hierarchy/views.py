from django.shortcuts import render
from hierarchy.models import File

# Create your views here.
def index_view(request):
    return render(request,'index.html', {'file': File.objects.all()})