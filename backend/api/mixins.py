from django.shortcuts import get_object_or_404
from recipes.models import Recipe
from rest_framework import exceptions, status
from rest_framework.response import Response

from .serializers import PreviewRecipeSerializer


class CreateOrDeleteMixin():
    def create_favorite(model, recipe_pk, request):
        user = request.user
        recipe = get_object_or_404(Recipe, pk=recipe_pk)
        if model.objects.filter(recipe=recipe, user=user).exists():
            raise exceptions.ValidationError(
                'Такой рецепт уже есть в избранном.'
            )
        model.objects.create(user=user, recipe=recipe)
        serializer = PreviewRecipeSerializer(
            recipe, context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_favorite(model, recipe_pk, request):
        user = request.user
        recipe = get_object_or_404(Recipe, pk=recipe_pk)
        if not model.objects.filter(user=user, recipe=recipe).exists():
            raise exceptions.ValidationError(
                'Такого рецепта нет в избранном.'
            )
        model.objects.filter(user=user, recipe=recipe).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create_cart(model, recipe_pk, request):
        user = request.user
        recipe = get_object_or_404(Recipe, pk=recipe_pk)
        if not model.objects.filter(user=user, recipe=recipe).exists():
            raise exceptions.ValidationError(
                'Такой рецепт уже есть в корзине.'
            )
        model.objects.filter(user=user, recipe=recipe).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete_cart(model, recipe_pk, request):
        user = request.user
        recipe = get_object_or_404(Recipe, pk=recipe_pk)
        if not model.objects.filter(user=user, recipe=recipe).exists():
            raise exceptions.ValidationError(
                'Такого рецепта нет в корзине.'
            )
        model.objects.filter(user=user, recipe=recipe).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
