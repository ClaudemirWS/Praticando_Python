print("========== PREÇO DO ALUGUEL COM BASE EM KM E DIAS DE ALUGUEL ==========")
dias = int(input('Digite quantos dias o carro ficou alugado: '))
km = float(input('Quantos KMs foram percorridos com o veículo: '))
#cada dia vale R$ 60 e cada KM rodado vale R$ 0,15
calc = (dias * 60) + (km * 0.15)
print('Com base em {} dias e {} KMs percorridos, o preço do aluguel é R$ {:.2f}'.format(dias, km, calc))