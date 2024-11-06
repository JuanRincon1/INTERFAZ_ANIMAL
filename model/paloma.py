from interfaces.Respirar import RespirarAble
from interfaces.Terrestre import TerrestreAble
from interfaces.Volar import VolarAble

class paloma(RespirarAble,TerrestreAble,VolarAble):
    
    def respirar(self):
        print("la paloma respira")
        
    def desplazar(self):
        print("la paloma se desplaza")
        
    def volar(self):
        print("la paloma vuela")        