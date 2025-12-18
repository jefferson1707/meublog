# 1. models: contém as classes para criar modelos (Model, CharField, etc)
# 2. User: modelo de usuário padrão do Django (já vem pronto)
# 3. reverse: gera URLs a partir do nome das views
# 4. timezone: para trabalhar com datas com timezone

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



# Explicação de cada Category: modelo de categoria para classificar posts
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField('Criada em', auto_now_add=True)  # ADICIONE ESTA LINHA
    
    def __str__(self):
        return self.name
    
    def post_count(self):
        return self.post_set.count()
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

# Explicação de cada Post: modelo de postagem do blog
class Post(models.Model):
    title = models.CharField("Título", max_length=200)
    content = models.TextField("Conteúdo")
    image = models.ImageField("Imagem", upload_to="blog/images/", null=True, blank=True)
    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)
    updated_at = models.DateTimeField("Data de Atualização", auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    categories = models.ManyToManyField(Category, blank=True, verbose_name="Categoria")
    published = models.BooleanField("Publicado", default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})      

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"
        ordering = ["-created_at"]


# Explicação de cada Comment: modelo de comentário para posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name="Post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    content = models.TextField("Comentário")
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    approved = models.BooleanField("Aprovado?", default=True)

    def __str__(self):
        return f"Comentário de {self.author} em {self.post.title}"

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
        ordering = ["created_at"]