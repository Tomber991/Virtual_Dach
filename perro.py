import pygame

class Perro:
    def __init__(self, datos):
        self.hambre = datos.get('hambre', 50)
        self.felicidad = datos.get('felicidad', 50)
        self.suciedad = datos.get('suciedad', 0)  # Nueva variable
        self.imagen = pygame.image.load("Dach_Assets/Dachs/Dach_Sprite_01.png")
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (100, 100)
    
    def actualizar(self):
        self.hambre += 0.1
        self.felicidad -= 0.02
        self.suciedad += 0.03

        if self.hambre > 80:
            self.felicidad -= 0.1
        
        if self.suciedad > 50:
            self.felicidad -= 0.1
        
        self.hambre = min(self.hambre, 100)
        self.felicidad = max(self.felicidad, 0)
        self.suciedad = min(self.suciedad, 100)
    
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)
    
    def alimentar(self):
        self.hambre -= 10
        if self.hambre < 0:
            self.hambre = 0
    
    def jugar(self):
        self.felicidad += 10
        if self.felicidad > 100:
            self.felicidad = 100
    
    def limpiar(self):
        self.suciedad -= 20
        if self.suciedad < 0:
            self.suciedad = 0
    
    def obtener_datos(self):
        return {
            'hambre': self.hambre,
            'felicidad': self.felicidad,
            'suciedad': self.suciedad
        }