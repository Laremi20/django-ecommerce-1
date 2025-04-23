from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),

    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='tienda/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),

    path('finalizar/', views.finalizar_compra, name='finalizar_compra'),
    path('confirmacion/', views.confirmacion_pedido, name='confirmacion_pedido'),
]