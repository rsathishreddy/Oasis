
from django.urls import path, include
from .views import candidateView

urlpatterns = [
    path('', candidateView),
    path('products/', include('api.Product.urls'))
]
