from django .urls import path,include
from rest_framework.routers import SimpleRouter
from .views import AlumnoViewset, crud

#Definir un router
router =SimpleRouter()
router.register(r'api',AlumnoViewset)

#Producto Viewset: 
#ip:8000/producto/api <----GET de todo
#ip:8000/producto/api /{id}<----GET;POST,PUT;PUT,DELETE de uno

urlpatterns=[
    path('',include(router.urls)),
    path('alumnos/',crud,name='lista'),
]