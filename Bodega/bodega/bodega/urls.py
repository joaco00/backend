
from django.contrib import admin
from django.urls import path, include
from bodega_App import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('movimientos/', views.listarmovimiento),
    path('agregarmovimiento/', views.agregarmovimiento),
    path('interfazjefe/', views.interfazjefe,name="interfazjefe"),
    path('interfazusuario/', views.interfazusuario,name="interfazusuario"),
    path('productos/', views.listarproducto),
    path('agregarproducto/', views.agregarproducto),
    path('movimientosjefe/', views.listarmovimientojefe),
    path('eliminar/<int:id>', views.eliminarproducto),
    path('actualizar/<int:id>', views.actualizarproducto),
    path('eliminarm/<int:id>', views.eliminarmovimiento),
    path('actualizarm/<int:id>', views.actualizarmovimiento),
    path('actualizarmu/<int:id>', views.actualizarmovimientou),
    
]
