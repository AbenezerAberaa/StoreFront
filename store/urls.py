from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet, basename='product')
router.register('collections', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, 'product', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

# URLConf
urlpatterns = router.urls + products_router.urls
