from django.db import connection
from .models import MyModel

# Exemplo de uma query raw simples
query = "SELECT * FROM myapp_mymodel WHERE nome = %s"
param = ['Leticia']

# Executar a raw query
with connection.cursor() as cursor:
    cursor.execute(query, param)
    resultados = cursor.fetchall()

# Exibir os resultados
for resultado in resultados:
    print(resultado)

# OU 

# Query raw usando o método raw() do modelo
resultados = MyModel.objects.raw("SELECT * FROM myapp_mymodel WHERE nome = %s", ['Leticia'])

for resultado in resultados:
    print(resultado.nome)
