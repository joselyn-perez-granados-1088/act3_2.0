from django.urls import path
from productos_app import views

urlpatterns = [
    path('',views.inicio_vista,name="inicio_vista"),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<codido>",views.seleccionarProducto,name="seleccionarProducto"),
    path("borrarProducto/<codido>",views.borrarProducto,name="borrarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto")
]
