from django.urls import path
from app1 import views

urlpatterns = [
    path('exercies1',views.ex1),
    path('exercies2',views.ex2),
    path('prac',views.prac,name="prac"),
    path('',views.index,name="index"),
    # path('',views.ex1),
]
