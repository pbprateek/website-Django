
# Create your views here.

from django.http import HttpResponse
from .models import Albums

def index(request):
    all_Albums=Albums.objects.all()
    html=''

    for album1 in all_Albums:
        url="/music/"+str(album1.id)+"/"
        html += '<a href="'+url+'">'+album1.artist+'</a><br>'
    return HttpResponse(html)

def details(request,album_id):
    return HttpResponse("<h2>Details are"+ album_id+"</h2>")
