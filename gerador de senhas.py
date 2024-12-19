import random
import string

def gerar_senha(tamanho):
    letras = string.ascii_letters
    numeros = string.digits  
    simbolos = string.punctuation

    todos_caracteres = letras + numeros + simbolos

    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho desejado para a senha: "))

senha_gerada = gerar_senha(tamanho_senha)
print(f"Sua senha gerada é: {senha_gerada}")