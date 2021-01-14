import art;
art.welcome();
while True:
    try:
        total = int(input("Quantas coisas deseja comprar?\n"));
        break;
    except:
        print("Por favor, insira um número inteiro válido.");
lista = {};
preco = {}
precoTotal = 0;
x = 1;
while x <= total:
    lista[x] = input("Digite a {num}ª coisa que deseja comprar ultimamente.\n".format(num=x));
    while True:
        try:
            preco[x] = float(input("Qual o preço desse produto?(R$)(Por favor,\nuse ponto ao invés de vírgula)\n"));
            break;
        except:
            print("Digite um valor válido por favor. Verifique se não usou vírgua\nno lugar de um ponto.")
    x+=1;
for x in preco:
    precoTotal = precoTotal+preco[x];
print("Ao todo você deseja comprar {total} coisas. Totalisando {preco}R$. Realmente\n precisa de tudo isso?\nConfira a lista logo abaixo:\n".format(total=total, preco=precoTotal));
for key in lista:
    print("%s: %s Preço: %.2f R$" %(key, lista[key], preco[key]));
confirm = input("Realmente tudo isso é necessário? Repense. (sim/não)\n");
if confirm[0].lower() != "s":
    print("Você foi bem sensato(a) e repensou naquilo que iria comprar!\n Pode ter certeza que a natureza agradece!");
    while True:
        try:
            if lista == {}:
                break;
            for k in lista:
                print("%s: %s Preço: %.2f" %(k, lista[k], preco[k]));
            removeList = input("Selecione os números das compras que você quer retirar separados por vírgula\n");
            removeList = removeList.split(",");
            x = 0;
            while x<len(removeList):
                removeList[x] = int(removeList[x]);
                lista.pop(removeList[x]);
                preco.pop(removeList[x]);
                x+=1;
            break;
        except:
            print("Verifique se separou todos os números por vírgula, se não tem pontos,\nse não colocou nenhuma letra ou se colocou algo inexistente por favor");
    precoFinal = 0;
    for x in preco:
        precoFinal = precoFinal + preco[x];
    print("Lista de compras final:");
    for x in lista:
        print("%s: %s Preço: %s R$" %(x, lista[x], preco[x]));
    precoFinal = precoTotal - precoFinal;
    print("Nossa! Olha só quanto que você economizou! %.2f R$! E de quebra \nainda preservou o meio ambiente!" %(precoFinal));
    print("Parabéns! Você é incrível!");
    input("Aperte ENTER para sair");
