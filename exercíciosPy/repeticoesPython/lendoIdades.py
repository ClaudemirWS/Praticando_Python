from datetime import date
print('========== MAIORIDADE E MENORIDADE ==========')
data = date.today().year
maior = 0
menor = 0
for count in range (1,8):
    pessoa = int(input('Digite o ano de nascimento da pessoa {}: '.format(count)))
    idade = data-pessoa
    if (idade >= 18):
        maior = maior + 1
    elif (idade < 18):
        menor = menor + 1
print("""\n{} pessoas estão no grupo da \033[035mMAIORIDADE\033[m
{} pessoas estão no grupo da \033[033mMENORIDADE\033[m""".format(maior,menor))