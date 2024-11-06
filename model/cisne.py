from interfaces.Volar import VolarAble
from interfaces.Respirar import RespirarAble
from interfaces.Terrestre import TerrestreAble
from interfaces.Nadar import NadarAble

class cisne(VolarAble,RespirarAble,NadarAble,TerrestreAble):
    
    def volar(self):
        print("el cisne vuela")
        
    def respirar(self):
        print("el cisne respira")
        
    def nadar(self):
        print("el cisne nada")
        
    def desplazar(self):
        print("el cisne se desplaza")
               

