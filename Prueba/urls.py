from django.urls import path
from Prueba import views

urlpatterns = [
     path('', views.primera_pagina),
     path('segunda_pagina/', views.segunda_pagina),
    path('tercera_pagina/', views.tercera_pagina),
]
