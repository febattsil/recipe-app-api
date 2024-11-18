"""URL mappings for the recipe app. """
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouters

from recipe import views


router = DefaultRouters()
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),

]
