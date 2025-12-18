from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Post, Comment

class BlogTests(TestCase):
    def setUp(self):
        """Configuração inicial para todos os testes"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )
        
        self.category = Category.objects.create(name='Tecnologia')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user,
            published=True
        )
        self.post.categories.add(self.category)
    
    def test_post_list_view(self):
        """Testa se a lista de posts carrega corretamente"""
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'blog/post_list.html')
    
    def test_post_detail_view(self):
        """Testa se a página de detalhe do post funciona"""
        response = self.client.get(reverse('blog:post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
    
    def test_category_view(self):
        """Testa a view de posts por categoria"""
        response = self.client.get(reverse('blog:category_posts', args=['Tecnologia']))
        self.assertEqual(response.status_code, 200)
    
    def test_create_post_login_required(self):
        """Testa que a view create_post requer login"""
        response = self.client.get(reverse('blog:create_post'))
        # Deve redirecionar para login (302) se não estiver logado
        self.assertEqual(response.status_code, 302)
    
    def test_create_post_authenticated(self):
        """Testa criação de post por usuário logado"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('blog:create_post'))
        self.assertEqual(response.status_code, 200)
    
    def test_comment_submission(self):
        """Testa submissão de comentário"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('blog:post_detail', args=[self.post.pk]),
            {'content': 'Test comment'}
        )
        # Deve redirecionar após comentar (302)
        self.assertEqual(response.status_code, 302)
        
        # Verifica se comentário foi criado
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().content, 'Test comment')
    
    def test_model_str_methods(self):
        """Testa os métodos __str__ dos modelos"""
        self.assertEqual(str(self.category), 'Tecnologia')
        self.assertEqual(str(self.post), 'Test Post')
    
    
    def test_category_post_count(self):
        """Testa o método post_count da categoria"""
        self.assertEqual(self.category.post_count(), 1)
        
        # Cria outro post na mesma categoria
        Post.objects.create(
            title='Another Post',
            content='More content',
            author=self.user,
            published=True
        ).categories.add(self.category)
        
        self.assertEqual(self.category.post_count(), 2)


class AdminTests(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpass',
            email='admin@example.com'
        )
        self.client = Client()
        self.client.login(username='admin', password='adminpass')
    
    def test_admin_access(self):
        """Testa se o admin pode acessar o painel"""
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
    
    def test_admin_models_registered(self):
        """Testa se os modelos estão registrados no admin"""
        from django.contrib import admin
        self.assertIn(Post, admin.site._registry)
        self.assertIn(Category, admin.site._registry)
        self.assertIn(Comment, admin.site._registry)