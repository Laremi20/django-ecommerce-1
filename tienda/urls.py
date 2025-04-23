from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('finalizar/', views.finalizar_compra, name='finalizar_compra'),
path('confirmacion/', views.confirmacion_pedido, name='confirmacion_pedido'),
    
]