from django.shortcuts import get_object_or_404
from rest_framework import exceptions, status
from rest_framework.response import Response

from recipes.models import Recipe
from .serializers import PreviewRecipeSerializer


class CreateOrDeleteMixin():
    def create_favorite_and_cart(self, model, recipe_pk, request, message):
        user = request.user
        recipe = get_object_or_404(Recipe, pk=recipe_pk)
        if model.objects.filter(recipe=recipe, user=user).exists():
            raise exceptions.ValidationError(message)
        model.objects.create(user=user, recipe=recipe)
        serializer = PreviewRecipeSerializer(
            recipe, context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_favorite_and_cart(self, model, recipe_pk, request, message):
        user = request.user
        recipe = get_object_or_404(Recipe, pk=recipe_pk)
        if not model.objects.filter(user=user, recipe=recipe).exists():
            raise exceptions.ValidationError(message)
        model.objects.filter(user=user, recipe=recipe).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
