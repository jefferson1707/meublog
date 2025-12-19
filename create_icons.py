from PIL import Image, ImageDraw, ImageFont
import os

print(" Criando ícones PWA para seu blog Django...")

# Cria pasta se não existir
os.makedirs('static/icons', exist_ok=True)
print(" Pasta criada: static/icons/")

# Cores do seu tema Bootstrap (navbar-dark)
bg_color = (52, 58, 64)    # #343a40 - cor da navbar do seu blog
text_color = (255, 255, 255)  # branco - texto visível

# Tamanhos necessários para PWA (em pixels)
sizes = [72, 96, 128, 144, 152, 192, 384, 512]

for size in sizes:
    # 1. Cria imagem quadrada com cor de fundo
    img = Image.new('RGB', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # 2. Tenta adicionar texto/ícone
    try:
        # Tamanho da fonte proporcional ao ícone
        font_size = size // 3
        
        # Para tamanhos maiores, adiciona "Blog"
        if size >= 192:
            text = "Blog"
            font_size = size // 6
        else:
            text = "B"
        
        # Desenha o texto no centro
        draw.text(
            (size // 2, size // 2), 
            text, 
            fill=text_color, 
            anchor="mm",  # middle-middle
            font_size=font_size
        )
    except Exception as e:
        # Se falhar (sem fonte), só salva o quadrado colorido
        print(f"  Sem fonte para {size}x{size}, criando ícone simples")
    
    # 3. Salva o arquivo
    filename = f'static/icons/icon-{size}x{size}.png'
    img.save(filename)
    print(f" {filename}")

print("\n TODOS os ícones PWA foram criados!")
print(" Local: static/icons/")
print(" Tamanhos: 72, 96, 128, 144, 152, 192, 384, 512 pixels")
