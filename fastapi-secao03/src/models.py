from typing import Optional

from pydantic import BaseModel, field_validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    @field_validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras.')
        
        if value.islower():
            raise ValueError('O título deve ser capitalizado')
        
        return value
    
cursos = [
    Curso(id=1, titulo='Programação Básica C', aulas=112, horas=60),
    Curso(id=1, titulo='Programação Avançada C', aulas=120, horas=80)
]