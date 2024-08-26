"""
POO
Multiparadigmas
- Flask e Django - O.O

Programação Estruturada Com O.O
- Flet

Programação Funcional - (Cientista, analista, estastiscos, matematicos...)
- Lambda

"""

from logging import fatal


class Aluno():

    def __init__(self, ch, faltas):
        self.ch = ch
        self.faltas = faltas
    
    def calcular_faltas(self):
        percent_ch = self.ch * (25/100)
            
        msg = ''
        if (self.faltas < percent_ch): 
            msg = 'Aluno Aprovado!'
        else:
            msg = 'Retido'
            
        return f"faltas-hs permitidas: {percent_ch} você {self.faltas} horas, resultado: {msg} por faltas"
    
  # Exercicio 

