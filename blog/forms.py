from django import forms
from .models import Comment, Post

# Formulário para criar/editar comentários.
class CommentForm(forms.ModelForm):

    # Configurações adicionais do formulário.
    class Meta:
        model = Comment
        fields = ['content']

        # Personalização dos widgets (elementos HTML).
        widgets = {
            'content': forms.Textarea(attrs={'rows':3, 'placeholder':'Escreva seu comentário aqui...', 
                                             'class':'form-control'}),
        }

        #  Mensagens de erro personalizadas.
        error_mensages = {
            'content': {
                'required': 'O conteúdo do comentário não pode estar vazio.',
                'max_length': 'O comentário é muito longo.',
            },
        }

# Formulário para criar/editar postagens.
class PostForm(forms.ModelForm):

    # Configurações adicionais do formulário.
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'published', 'categories']

        # Personalização dos widgets (elementos HTML).
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Título da postagem', 'class':'form-control'}),
            'content': forms.Textarea(attrs={'rows':10, 'placeholder':'Escreva sua postagem aqui...',
                                          'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'published': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'categories': forms.SelectMultiple(attrs={'class':'form-control'}),
        }

        # Labels personalizados.
        labels = {
            'title': 'Título',
            'content': 'Conteúdo',
            'image': 'Imagem',
            'published': 'Publicar agora?',
            'categories': 'Categorias',
        }


        help_texts = {
            'published': 'Desmarque para manter o rascunho.',
            'image': 'Imagem opcional para a postagem. Formatos suportados: JPG, PNG, GIF.'
     }
        
# Formulário para busca simples.    
class SearchForm(forms.Form): # Formulario independente (forms.Form).

    # Campo de busca.
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Pesquisar...', 
                                      'class': 'form-control', 'aria-label': 'Buscar',
        }),
        label = '', # Label vazio (placeholder já explica)
        help_text='Digite termos para buscar postagens.'
        ) 