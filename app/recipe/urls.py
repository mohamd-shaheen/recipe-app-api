from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeModelViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredienViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
