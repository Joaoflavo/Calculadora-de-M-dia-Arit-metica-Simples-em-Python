print('Bem vindo à Calculadora de Média Aritmética Simples!')
print('Programa desenvolvido por João Flavo 13-10-2020 j°@°2@2@ 14:09 PM')
print ('Atenção,digite apenas notas de 0 a 10')
print('Se ocorrer erro na digitação reinicie o programa')
a = int(input('Digite à sua Nota do Primeiro Bimestre:'))
b = int(input('Digite à sua Nota do Segundo Bimestre:'))
c = int(input('Digite à sua Nota do Terceiro Bimestre:'))
d = int(input('Digite à sua Nota do Quarto Bimestre:'))
media = (a + b + c + d) /4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    #.format é usado para formatar a resposta
    print('Sua media é: {}'.format(media))
    print('Obrigado por usar a calculadora de media.')

    if media > 7:
        print('Congratulations! Parabéns você foi aprovado!')
    else:
        print('Infelizmente você não foi aprovado')
        print('Estude mais e tente de novo no próximo período letivo!')
        print('Mas um ano chega ao fim, desejamos à todos, um ótimo fim de a novo & boas festas!')
        print('Este é o Fim do programa.')

else:
     print('Desculpe foi informado alguma nota errada,')
     print('digite apenas nota de 0 à 10.')
     print('Reinicie o programa e tente de novo.')
     print('Obrigado por usar a calculadora de media.')
