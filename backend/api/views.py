
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from recipes.models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                            ShoppingCart, Tags)
from rest_framework import exceptions, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.pagination import LimitPagination
from api.permissions import IsAuthorOrAdminOrReadOnly
from .filter import IngredientSearchFilter, RecipeFilter
from .mixins import CreateOrDeleteMixin
from .serializers import (CreateRecipeSerializer, IngredientSerializer,
                          MyUserSerializer, RecipeSerializer,
                          SubscriptionSerializer, TagsSerializer)
from users.models import Follow


User = get_user_model()


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IngredientSearchFilter


class RecipeViewSet(viewsets.ModelViewSet, CreateOrDeleteMixin):
    queryset = Recipe.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsAuthorOrAdminOrReadOnly]
    pagination_class = LimitPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecipeSerializer
        return CreateRecipeSerializer

    @action(
        methods=['POST', 'DELETE'],
        detail=True,
        permission_classes=[IsAuthenticated],
    )
    def favorite(self, request, pk=None):
        if request.method == 'POST':
            message = 'Такой рецепт уже есть в избранном.'
            return self.create_favorite_and_cart(
                Favorite, pk, request, message
            )
        elif request.method == 'DELETE':
            message = 'Такого рецепта нет в избранном.'
            return self.delete_favorite_and_cart(
                Favorite, pk, request, message
            )

    @action(
        methods=['POST', 'DELETE'],
        detail=True,
        permission_classes=[IsAuthenticated],
    )
    def shopping_cart(self, request, pk=None):
        if request.method == 'POST':
            message = 'Такой рецепт уже есть в корзине.'
            return self.create_favorite_and_cart(
                ShoppingCart, pk, request, message
            )
        elif request.method == 'DELETE':
            message = 'Такого рецепта нет в корзине.'
            return self.delete_favorite_and_cart(
                ShoppingCart, pk, request, message
            )

    @action(detail=False, permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        ingredients = RecipeIngredient.objects.filter(
            recipe__shopping_cart__user=request.user
        ).values('ingredient').annotate(
            amount=Sum('amount')
        ).values_list(
            'ingredient__name', 'ingredient__measurement_unit', 'amount'
        )
        data = [
            f"{name} ({measurement_unit}) - {amount}"
            for name, measurement_unit, amount in ingredients
        ]
        return HttpResponse('\n'.join(data), content_type='text/plain')


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (permissions.AllowAny,)


class FollowUserView(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitPagination
    serializer_class = SubscriptionSerializer

    def post(self, request, id):
        user = request.user
        author = get_object_or_404(User, pk=id)
        if user == author:
            raise exceptions.ValidationError(
                'Нельзя подписаться на себя самого.'
            )
        if Follow.objects.filter(user=user, author=author).exists():
            raise exceptions.ValidationError(
                'Подписка уже существует'
            )
        Follow.objects.create(user=user, author=author)
        serializer = self.serializer_class(
            author, context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        user = request.user
        author = get_object_or_404(User, pk=id)
        follow = get_object_or_404(Follow, user=user, author=author)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriptionsView(ListAPIView):
    serializer_class = SubscriptionSerializer
    pagination_class = LimitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(subscribers__user=self.request.user)

    def subscriptions(self, request):
        user = request.user
        queryset = User.objects.filter(followings__user=user)
        pag_queryset = self.paginate_queryset(queryset)
        serializer = SubscriptionSerializer(pag_queryset, many=True)
        return self.get_paginated_response(serializer.data)
