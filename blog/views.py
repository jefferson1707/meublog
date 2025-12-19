from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import CommentForm, PostForm  
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Criar views para o blog.

# View para exibir a lista de posts do blog.
def post_list(request):

    #  Exibe todos os posts publicados, do mais recente para o mais antigo.

    posts = Post.objects.filter(published=True).order_by('-created_at')
    categories = Category.objects.all()

    # Contexto: dados que serão passados para o template.
    context = {
        'posts': posts,
        'categories': categories,
        'page_title': 'Blog - Pagina Inicial',
    }

    return render(request, 'blog/post_list.html', context)

# View para exibir os detalhes de um post específico.
def post_detail(request, pk):

    # Exibe um post individual pelo seu ID (primary key).
    post = get_object_or_404(Post, pk=pk, published=True)
    comments = post.comments.filter(approved=True)
    
    # Formulário de comentário.
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            
            if request.user.is_authenticated:
                comment.author = request.user

            # Salva o comentário no banco de dados.
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)

    # Se o método não for POST, cria um formulário vazio.   
    else:
        form = CommentForm()

    # Contexto: dados que serão passados para o template.
    context = {

        'post': post,
        'comments': comments,
        'form': form,
        'page_title': post.title
    }    

    return render(request, 'blog/post_detail.html', context)


# View para exibir posts por categoria.
def category_posts(request, category_name):
    
    # Exibe posts filtrados por categoria.
    posts = Post.objects.filter(categories__name__exact=category_name, published=True).order_by('-created_at')

    # Contexto: dados que serão passados para o template.
    context = {
        'posts': posts,
        'category': category_name,
        'page_title': f'Blog - Categoria: {category_name}',
    }

    return render(request, 'blog/category_posts.html', context)
            

# View para criar um novo post (requer login).            
@login_required
def create_post(request):    

    # View protegida: só usuários logados podem criar posts.
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES) # Request.FILES para upload de imagens.
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            # Salva o post no banco de dados.
            post.save() 
            
            # Salva as relações ManyToMany, se houver.
            form.save_m2m()  # Necessário quando usa commit=False com campos ManyToMany
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()       

    # Contexto: dados que serão passados para o template.
    context = {
        'form': form,
        'page_title': 'Criar Novo Post',
    }   
    return render(request, 'blog/create_post.html', context)

# View para exibir uma página offline.
def offline_page(request):
    return render(request, 'blog/offline.html')

# View para servir o manifest.json
def pwa_manifest(request):
    return HttpResponse(
        open('static/manifest.json').read(),
        content_type='application/json'
    )