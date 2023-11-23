from django.urls import path
from rubiks import views

urlpatterns = [
    path('api/solvecube', views.solve_cube)
]