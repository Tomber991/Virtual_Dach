import pygame
from perro import Perro
from data_manager import cargar_datos, guardar_datos

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Tamagochi Salchicha")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
rojo = (255, 0, 0)

# Cargar datos del perro
datos_perro = cargar_datos("perro_data.json")
perro = Perro(datos_perro)

# Crear botones
boton_alimentar = pygame.Rect(50, 500, 100, 50)
boton_jugar = pygame.Rect(200, 500, 100, 50)
boton_limpiar = pygame.Rect(350, 500, 100, 50)  # Nuevo botón

# Cargar fuente pixel art
fuente_pixel = pygame.font.Font("Fonts/PressStart2P-Regular.ttf", 18)

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_alimentar.collidepoint(evento.pos):
                perro.alimentar()
            elif boton_jugar.collidepoint(evento.pos):
                perro.jugar()
            elif boton_limpiar.collidepoint(evento.pos):  # Nueva interacción
                perro.limpiar()

    # Actualizar estado del perro
    perro.actualizar()

    # Dibujar en pantalla
    pantalla.fill(blanco)
    perro.dibujar(pantalla)

    # Dibujar indicadores de estado
    hambre_texto = fuente_pixel.render(f'Hambre: {int(perro.hambre)}', True, negro)
    felicidad_texto = fuente_pixel.render(f'Felicidad: {int(perro.felicidad)}', True, negro)
    suciedad_texto = fuente_pixel.render(f'Suciedad: {int(perro.suciedad)}', True, negro)  # Nuevo indicador
    
    pantalla.blit(hambre_texto, (50, 50))
    pantalla.blit(felicidad_texto, (50, 100))
    pantalla.blit(suciedad_texto, (50, 150))  # Nueva posición del indicador

    # Dibujar barras de estado
    pygame.draw.rect(pantalla, rojo, (50, 80, perro.hambre * 2, 20))
    pygame.draw.rect(pantalla, verde, (50, 130, perro.felicidad * 2, 20))
    pygame.draw.rect(pantalla, azul, (50, 180, perro.suciedad * 2, 20))  # Nueva barra

    # Dibujar botones
    pygame.draw.rect(pantalla, verde, boton_alimentar)
    pygame.draw.rect(pantalla, azul, boton_jugar)
    pygame.draw.rect(pantalla, azul, boton_limpiar)  # Nuevo botón

    # Dibujar texto en los botones
    texto_alimentar = fuente_pixel.render("Alimentar", True, negro)
    texto_jugar = fuente_pixel.render("Jugar", True, negro)
    texto_limpiar = fuente_pixel.render("Limpiar", True, negro)  # Nuevo texto del botón
    
    pantalla.blit(texto_alimentar, (boton_alimentar.x + 10, boton_alimentar.y + 10))
    pantalla.blit(texto_jugar, (boton_jugar.x + 10, boton_jugar.y + 10))
    pantalla.blit(texto_limpiar, (boton_limpiar.x + 10, boton_limpiar.y + 10))  # Nueva posición del texto

    pygame.display.flip()

# Guardar datos del perro
guardar_datos("perro_data.json", perro.obtener_datos())

pygame.quit()