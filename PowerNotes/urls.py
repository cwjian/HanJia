
from django.urls import path,include
from PowerNotes import views
urlpatterns = [
    path("index/",views.index,name="index")
]
