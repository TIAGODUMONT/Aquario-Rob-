print(' Bem vindo ao seu Aquario Robô !! Como posso te ajudar??')

opção = 0
while opção != 5:
    print(''' [1] Digite as medidas do seu Aquário

               [2] Digite o ph da sua água

               [3] Digite a litragem do seu tanque para sump

               [4] calculo de lumen's

               [5] T.P.A

               [6] TAMPONAMENTO ''')

    opção = int(input('ESCOLHA A OPÇÃO DESEJADA:  '))
    if opção == 1:
        c = float(input(' Digite o comprimento do seu Aquário em centímetros:  ' ))
        l = float(input(' Digite a largura do seu Aquário em centímetros:      '))
        a = float(input(' Digite a altura do seu Aquário em centímetros :       '))
        print(' Seu Aquário tem {:} litros de água'.format(c*l*a/1000))
        break

    elif opção == 2:
        alc = float(input(" Digite o ph da sua água"))
        if alc >= 7.1:
            print(' Sua agua esta alcalina')
        elif alc < 6.9:
            print(' sua agua esta acida')
        elif alc == 7.0:
            print('Seu ph esta neutro')
            break


    elif opção == 3:
        sump = float(input(' Para saber o tamanho ideal do seu sump , Digite quantos litros tem seu Aquário?: '))
        tsump = sump * 35 / 100
        print('Seu sump precisa ter {} litros de água .'.format(tsump))
        break

    elif opção == 4:
        alcalinizar = float(input(' para deixar seu ph neutro , Digite a quantidade de litros do seu Aquário: '))
        bicarbonato = litros * 0.5
        print(' Seu Aquario precisa de {} gramas de Bicarbonato de Sódio .'.format(bicarbonato))
        break

    elif opção == 5:
        tpa = float(input('Para saber a quantidade de trocas parcias , Digite quantos litros tem seu Aquário?: '))
        trocas = tpa * 15 / 100
        print(' Seu Aquario precisa de {}Litros de  água nova a cada 15 dias.'.format(trocas))
        break

    elif opção == 6:
        litros = float(input(' para deixar seu ph neutro , Digite a quantidade de litros do seu Aquário: '))
        bicarbonato = litros * 0.5
        print(' Seu Aquario precisa de {} gramas de Bicarbonato de Sódio .'.format(bicarbonato))
