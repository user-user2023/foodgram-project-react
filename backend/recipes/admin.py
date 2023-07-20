from django.contrib import admin

from .models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                     ShoppingCart, Tags)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'name',
        'cooking_time',
        'favorites_count',
    )
    list_filter = ('author', 'name', 'tags',)
    search_fields = ('author', 'name', 'tags',)
    inlines = [RecipeIngredientInline]

    def favorites_count(self, obj):
        count = 0
        if Favorite.objects.filter(recipe=obj).exists():
            count = Favorite.objects.filter(recipe=obj).count()
        return count


class TagsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'slug',
    )
    list_filter = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit',
    )
    list_filter = ('name',)
    search_fields = ('name',)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )
    list_filter = (
        'user',
        'recipe',
    )
    search_fields = (
        'user',
        'recipe',
    )


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )
    list_filter = (
        'user',
        'recipe',
    )
    search_fields = (
        'user',
        'recipe',
    )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
