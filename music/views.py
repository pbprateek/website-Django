
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>This is the music home page</h2>")
