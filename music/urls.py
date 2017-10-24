from django.conf.urls import url
# . means current directyy means music
from . import views

urlpatterns=[
    #this is called when they req nothing in music
    url(r'^$',views.index,name='index')
]