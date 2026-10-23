from django.urls import path

from . import views

app_name = "eventos"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("eventos/<int:evento_id>/", views.detalle, name="detalle"),
]