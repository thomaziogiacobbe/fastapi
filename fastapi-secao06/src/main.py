from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjUyNDQyMTE4LCJpYXQiOjE2NTE4MzczMTgsInN1YiI6IjIifQ.5yeW2y_M3eAYrv-369FLsTTkjAFQn6W_eUR19Ivz_YA
Tipo: bearer

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjUyNDQzNDk1LCJpYXQiOjE2NTE4Mzg2OTUsInN1YiI6IjMifQ.jTq0xkcILa7kgrtMJhcew6OIwXODEjX24CzCToY7bbU
"""
