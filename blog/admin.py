from django.contrib import admin
from .models import Category, Post, Comment

# Registrando modelos.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'post_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    readonly_fields = ('created_at',)
    
    # Função para contar o número de posts em cada categoria
    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = 'Número de Posts'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published', 'display_categories')
    list_filter = ('published', 'categories', 'created_at')
    search_fields = ('title', 'content')
    filter_horizontal = ('categories',)
    readonly_fields = ('created_at', 'updated_at')

    # Função para exibir categorias como uma lista separada por vírgulas
    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Categorias'



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'approved', 'short_content')
    list_filter = ('post', 'approved', 'created_at')
    search_fields = ('content', 'author__username', 'post__title')
    actions = ['approve_comments', 'disapprove_comments']
    
    # Função para exibir um resumo do conteúdo do comentário
    def short_content(self, obj):
        if len(obj.content) > 50:
            return obj.content[:50] + "..."
        return obj.content
    short_content.short_description = 'Conteudo (resumo)'

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Aprovar comentários selecionados"

    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
    disapprove_comments.short_description = "Reprovar comentários selecionados"
