import random
import time

# ----- Personagem em si ----- #
Eu = {
    "nome": "",
    "classe": "",
    "vida": 0,
    "dano_base": 0,
    "experiencia": 0,
    "level": 1,
    "nivelmagico": 0,
    "divino": 0,
    "chance": 0,
    "tipo": 0,
    "sorte": 0,
    "cd": 0,
    "turno": "Você ataca",
}

Eu['nome'] = input("Qual o seu nome?\n")
# ----- Invocações do lich ----- #
invocacao = {
    1: {
        "nome": "Cavaleiro da morte",
        "vida": 200,
        "dano": 100,
    },
    2: {
        "nome": "Lobo",
        "vida": 50,
        "dano": 20,
    },
    3: {
        "nome": "Orc",
        "vida": 100,
        "dano": 25,
    },
    4: {
        "nome": "Esqueleto",
        "vida": 80,
        "dano": 10,
    }
}

# ----- INIMIGOS ----- # 
Lobo = {
    "nome": "Lobo",
    "vida": 100,
    "dano": 15,
    "tipo": 2,
    "velocidade": 5,
    "xp": 50
    #fraqueza nada
}
Orc = {
    "nome": "Orc",
    "vida": 200,
    "dano": 20,
    "tipo": 2,
    "velocidade": 2,
    "xp": 100
    #fraqueza magia
}
Goblin = {
    "nome": "Goblin",
    "vida": 70,
    "dano": 10,
    "tipo": 2,
    "velocidade": 1,
    "xp": 35
    #fraqueza físico
}
Urso = {
    "nome": "Urso",
    "vida": 300,
    "dano": 30,
    "tipo": 2,
    "velocidade": 3,
    "xp": 150
    #fraqueza nada
}
Fada = {
    "nome": "Fada",
    "vida": 50,
    "dano": 10,
    "tipo": 1,
    "velocidade": 5,
    "xp": 50
}
Cultistas = {
    "nome": "Cultistas",
    "vida": 150,
    "dano": 25,
    "tipo": 3,
    "velocidade": 4,
    "xp": 120
}
Esqueleto = {
    "nome": "Esqueleto",
    "vida": 80,
    "dano": 15,
    "tipo": 1,
    "velocidade": 2,
    "xp": 40
}

inimigos = {
    1: Lobo,
    2: Orc,
    3: Goblin,
    4: Urso,
    5: Fada,
    6: Cultistas,
    7: Esqueleto,
}   
# ----- Semi BOSS e BOSS ----- #
Hidra = {
    "nome": "Hidra",
    "vida": 1000,
    "dano": 100,
    "tipo": "todos",
    "velocidade": 10,
    "xp": 1000
    #fraqueza magia normal=10% e divino=5%
}
Hidra_Falsa = {
    "nome": "Hidra Falsa",
    "vida": 5000,
    "dano": 300, 
    "tipo": "todos",
    "velocidade": 10,
    "xp": 9999999999
}
# ----- Ataque de cada classe e suas mecanicas ----- # 
def ataque_sacerdote(Pla):
    danobase = Pla['dano_base']
    divino = Pla['divino']
    chance = random.randint(1, 100)
    if chance >= 50 and chance < 85:
        print(f"\033[36mA divindade lhe concede {danobase * divino * 2} de dano, o inimigo é queimado pela luz divina!\033[0m")
        return danobase * divino * 2
    elif chance >= 85:
        print(f"\033[35m?01000100 01101001 01110110 01101001 01101110 01101111? causa {danobase * (divino * 5)} de dano\033[0m") # "Divino" em binario
        return danobase * (divino * 5)
    else:
        print(f"A divindade lhe concede poder, você causa {danobase * divino} de dano, o inimigo é atingido pela luz divina!")
        return danobase * divino

def ataque_guerreiro(Pla):
    danobase = Pla['dano_base']
    chance = random.randint(1, 100)
    if chance >= 45 and chance < 80:
        print(f"\033[33mSua espada pede por sangue, você causa {danobase * 5} de dano\033[0m")
        return danobase * 5
    elif chance >= 80:
        print(f"\033[31mEntra em modo de fúria\033[0m")
        for i in range(5):
            print("\033[31mAtaca\033[0m")
        return danobase * 15
    else:
        print(f"Você acerta o inimigo em cheio e causa {danobase * 2} de dano")
        return danobase * 2

def ataque_mago(Pla):
    danobase = Pla['dano_base']
    chance = random.randint(1, 100)
    if chance >= 40 and chance < 75:
        print(f"\033[31mVocê carrega um ataque mágico de nível superior e causa {danobase * Pla['nivelmagico'] * 2} de dano, o inimigo é engolido por chamas\033[0m")
        return danobase * Pla['nivelmagico'] * 2
    elif chance >= 75:
        print(f"\033[32mVocê conjura uma explosao e causa {danobase * Pla['nivelmagico'] * 5} de dano, o inimigo é derrotado facilmente\033[0m")
        return danobase * Pla['nivelmagico'] * 5
    else:
        print(f"Você conjura um feitiço intermediario e causa {danobase * Pla['nivelmagico']} de dano")
        return danobase * Pla['nivelmagico']    

def invocando():
    chance = random.randint(1, 100)
    if chance >= 85:
        return invocacao[1]
    elif chance >= 55 and chance < 85:
        return invocacao[3]
    elif chance < 55 and chance >= 30:
        return invocacao[2]
    else:
        return invocacao[4]

def ataque_arqueiro(Pla):
    danobase = Pla['dano_base']
    chance = random.randint(1, 100)
    if chance >= 40 and chance < 70:
        print(f"\033[33mVocê ataca e causa {danobase * 5} de dano (Crítico)\033[0m")
        return danobase * 5
    elif chance >= 70:
        print(f"\033[32mSua flecha atinge o ponto fraco do inimigo, causando {danobase * 14} de dano\033[0m")
        return danobase * 14
    else:
        print(f"Você dispara 3 flechas causando {danobase * 3} de dano")
        return danobase * 3

def ataque_cartunista(Pla):
    danobase = Pla['dano_base']
    divino = Pla['divino']
    chance = random.randint(1, 100)
    if chance >= 65 and chance < 85:
        print(f"\033[33mVocê tira sorte grande, 5 caminhões atingem o inimigo e causam {danobase * 5 * divino} de dano (Crítico)\033[0m")
        return danobase * 5 * divino
    elif chance >= 85:
        print(f"\033[35mVocê tira a sorte gigante! Voce invoca uma bomba nuclear! causando {danobase * 10 * divino} de dano\033[0m")
        return danobase * 10 * divino
    else:
        print(f"Você tira a sorte pequena! invoca {divino} metralhadoras em campo! causando {danobase * divino} de dano") 
        return danobase * divino

def ataque_artista_marcial(Pla):
    danobase = Pla['dano_base']
    chance = random.randint(1, 100)
    if chance >= 50 and chance < 70:
        print(f"\033[33mVocê atinge um ponto fraco do inimigo, você causa {danobase * 5} de dano (Crítico)\033[0m")
        return danobase * 5
    elif chance >= 75:
        print(f"\033[35mVocê ultrapassa seu estado atual\033[0m")
        for i in range(3):
            print(f"\033[35mO inimigo recebe {danobase * 5}\033[0m")
        return danobase * 15
    else:
        print(f"Você lança 2 ataques consecutivos {danobase * 2} de dano")
        return danobase * 2

def ataque_lich(Pla):
    danobase = Pla['dano_base']
    chance = random.randint(1, 100)
    if chance >= 55 and chance < 80:
        print(f"\033[35mVocê lança um ataque mágico de nível máximo e causa {danobase * Pla['nivelmagico'] * 5} de dano, o inimigo é devorado por chamas escuras\033[0m")
        return danobase * Pla['nivelmagico'] * 5
    elif chance >= 80:
        print(f"\033[35mVocê invoca {Pla['nivelmagico']} magos e junto a eles causa {danobase * Pla['nivelmagico'] * 10} de dano, o inimigo é derrotado facilmente\033[0m")
        return danobase * Pla['nivelmagico'] * 10
    else:
        print(f"\033[35mVocê invoca um cavaleiro da morte e juntos causam {danobase * Pla['nivelmagico'] * 2} de dano\033[0m")
        return danobase * Pla['nivelmagico'] * 2

acao_da_classe = {
    "Sacerdote": ataque_sacerdote,
    "Guerreiro": ataque_guerreiro,
    "Mago": ataque_mago,
    "Arqueiro": ataque_arqueiro,
    "Cartunista": ataque_cartunista,
    "Artista Marcial": ataque_artista_marcial,
    "Lich": ataque_lich,
}

# ----- Função de batalha ----- #
def fisico(Pla, inimigo):

    # Declaracoes, puxando as informacoes das personagens/inimigos
    invocacaomax = 0
    Vid = Pla['vida']
    vidainimiga = inimigo['vida']
    if inimigo['nome'] == "Hidra" and Pla['tipo'] == 1:
        danobase = Pla['dano_base'] + Pla['dano_base'] * 0.1
    elif inimigo['nome'] == "Hidra" and Pla['tipo'] == 3:
        danobase = Pla['dano_base'] + Pla['dano_base'] * 0.05
    else: 
        danobase = Pla['dano_base']
    danoinimigo = inimigo['dano']
    velocidadeinimiga = inimigo['velocidade']
    xp = inimigo['xp']

    # Caso inimigo tenha um dano maior que o seu: um aviso.
    if danoinimigo > Pla['dano_base']:
        time.sleep(1)
        print("...")
        time.sleep(0.5)
        print(f"{inimigo['nome']} é mais forte que você, tome cuidado!")
        print("...")
        time.sleep(0.5)

    # Loop da batalha, até que a vida zere.
    while Vid > 0 and vidainimiga > 0:
        # "Dados"
        Chance = random.randint(1, 50)
        Chance2 = random.randint(1, 50)

        # Se tiver sorte, roda um ataque de sua classe.
        if Chance + Pla['chance'] > 35 and Pla['classe'] != "Necromante":
            print(f"\033[36mVocê surpreende {inimigo['nome']}\033[0m")
            ataque = acao_da_classe[Pla['classe']](Pla)
            vidainimiga = vidainimiga - ataque
            time.sleep(1)
        elif invocacaomax < 2 and Pla['classe'] == "Necromante":
            invocado = invocando()
            print(f"\033[35mVocê invoca {invocado['nome']}\033[0m")
            Vid += invocado['vida']
            danobase += invocado['dano']
            invocacaomax += 1
            time.sleep(1)
        # Se o inimigo tirar o resultado melhor que voce no dado, ele que acerta "Crítico"
        elif Chance2 + velocidadeinimiga > 35:
            print(f"\033[31m{inimigo['nome']} te surpreende e causa {(inimigo['dano'] * 2):.2f}\033[0m")
            Vid -= inimigo['dano'] * 2
            time.sleep(1)
            invocacaomax = 0
        # Usando o dado novamente pra ver quem ataca primeiro 
        elif Chance > 25:
            print(f"\033[34m{Eu['turno']} {inimigo['nome']} e causa(m) {(random.uniform(danobase, danobase + (danobase * 0.3))):.2f}\033[0m")
            vidainimiga -= random.uniform(danobase, danobase + (danobase / 3))
            time.sleep(1)
            print(f"\033[33m{inimigo['nome']} te ataca e causa {(inimigo['dano']):.2f}\033[0m")
            Vid -= inimigo['dano']
            time.sleep(1)
        # Caso o dado de menor que 25 o inimigo ataca primeiro
        else:
            print(f"\033[33m{inimigo['nome']} te ataca e causa {(inimigo['dano']):.2f}\033[0m")
            Vid -= inimigo['dano']
            time.sleep(1)
            print(f"\033[34m{Eu['turno']} {inimigo['nome']} e causa(m) {(random.uniform(danobase, danobase + (danobase * 0.3))):.2f}\033[0m")
            vidainimiga -= random.uniform(danobase, danobase + (danobase * 0.3))
            time.sleep(1)
            invocacaomax -= 1
    # Se a vida for maior que 0: mostra a sua vida e a quantidade de xp que ganhou.
    if Vid > 0:
        print(f"\033[32mVida restante: {Vid:.2f}\033[0m")
        print("\033[32mVocê venceu!\033[0m")
        time.sleep(1)
        print(f"\033[32mVocê ganhou {xp} de experiência\033[0m")
        print("...")
        time.sleep(0.5)
        print("\033[32mVocê se sente mais forte\033[0m\n")
        Eu['experiencia'] += xp
        Eu['level'] += Pla['experiencia'] / (50 * Pla['level'])
        Eu['dano_base'] += Pla['level']
        Eu['vida'] += Pla['vida'] * ((Pla['level']) / 10)
        Eu['chance'] += Pla['level'] / 10
        invocacao[1]['vida'] += Eu['level']
        invocacao[1]['dano'] += Eu['level']
        invocacao[2]['vida'] += Eu['level']
        invocacao[2]['dano'] += Eu['level']
        invocacao[3]['vida'] += Eu['level']
        invocacao[3]['dano'] += Eu['level']

    else:
        print("\033[31mVocê perdeu!\033[0m")
    return Vid

# Pergunta inicial de qual classe escolher
Classe = int(input("Qual sua classe?\n1:Sacerdote 2:Guerreiro 3:Mago 4:Necromante 5:Arqueiro 6:Cartunista 7:Artista Marcial\n"))

# ----- Escolha de Classe ----- #
match Classe:
    case 1:
        print("\033[33mVocê agora é um Sacerdote\033[0m")
        Eu['vida'] += 100
        Eu['dano_base'] = 10
        Eu['tipo'] = 3
        Eu['velocidade'] = 2
        Eu['divino'] = random.randint(2, 15)
        Eu['classe'] = "Sacerdote"
        
         
    case 2:
        print("\033[31mVocê agora é um Guerreiro\033[0m")
        Eu['vida'] = 500
        Eu['dano_base'] = 30
        Eu['tipo'] = 2
        Eu['velocidade'] = 4
        Eu['classe'] = "Guerreiro"
         
    case 3: 
        print("\033[34mVocê agora é um Mago\033[0m")
        Eu['vida'] = 80
        Eu['dano_base'] = 40
        Eu['tipo'] = 1
        Eu['velocidade'] = 1
        Eu['nivelmagico'] = random.randint(2, 15)
        Eu['classe'] = "Mago"
        
    case 4:
        print("\033[35mVocê agora é um Necromante\033[0m")
        Eu['vida'] = 50
        Eu['dano_base'] = 5
        Eu['tipo'] = 1
        Eu['velocidade'] = 2
        Eu['classe'] = "Necromante"
        Eu['turno'] = "Suas invocações atacam"
        Eu['nivelmagico'] = random.randint(2, 15)
        
    case 5:
        print("\033[32mVocê agora é um Arqueiro\033[0m")
        Eu['vida'] = 200
        Eu['dano_base'] = 25
        Eu['tipo'] = 2
        Eu['velocidade'] = 6
        Eu['classe'] = "Arqueiro"
        
    case 6: 
        print("\033[36mVocê agora é um Cartunista\033[0m")
        Eu['vida'] = 20
        Eu['dano_base'] = 80
        Eu['tipo'] = 3
        Eu['velocidade'] = 5
        Eu['classe'] = "Cartunista"
        Eu['divino'] = random.randint(2, 5)
        
    case 7:
        print("\033[33mVocê agora é um Artista Marcial\033[0m")
        Eu['vida'] = 550
        Eu['dano_base'] = 25
        Eu['tipo'] = 2
        Eu['velocidade'] = 3
        Eu['classe'] = "Artista Marcial"

# Lugar: Seleção de cenários.
Lugar = 0

Lugar = random.randint(1, 7)

# ----- Cenários/Eventos ----- #
match Lugar:
    case 1:
        print("A lua brilha intensamente...")
        time.sleep(0.8)
        print("Você esta em uma floresta a noite")
        time.sleep(1)
        print("...")
        time.sleep(0.3)
        if Classe == 2:
            print("\033[35mA lua sorri para você (Você sente sua força aumentar)\033[0m")
            Eu['dano_base'] += 15
            
        print("Uma matilha lhe cerca, a não ser que você quebre o cerco, sua única opção é batalhar.\n")
        
        vida = fisico(Eu, Lobo)
        Eu['vida'] = vida
        
        if vida > 0:
            print("Você dilacera os seus oponentes!")
            time.sleep(1.2)
            print("...")
            time.sleep(0.3)
            print("Você caminha pelo breu da floresta sombria")
            time.sleep(1.9)
            print("Ao longe, você vê uma chama")
            time.sleep(1.3)
            print("A Luz laranja ilumina o ambiente gelado")
            time.sleep(2)
            print("Ao se aproximar, é visto uma fogueira juntamente de uma figura")
            time.sleep(2.6)
            print("\033[95mFigura desconhecida: Fique aí parado! Com quem falo?\033[0m")
            time.sleep(2.8)
            resposta = int(input (f"1:Uma alma vazia 2:Um ambulante 3:Um/a {Eu['classe']}. "))
            match resposta:
                case 1:
                    print("\033[95mFigura desconhecida: Uma alma vazia, é? Bem... no fim todos nós somos, não?\033")
                    time.sleep(3)
                    nome = input("\033[95mFigura desconhecida: Meu nome é Ana. Qual o seu nome?\033[0m")
                    time.sleep(2)
                    print(f"\033[95mAna: {nome}, hm... um nome bonito, mas não tem importância nesse mundo\033[0m")
                    time.sleep(2)
                    print("\033[95mAna: Bem, vamos seguir juntos por enquanto, a floresta é perigosa.\033[0m")
                case 2:
                    print("\033[95mFigura desconhecida: Um ambulante? Interessante.\033")
                    time.sleep(3)
                    nome = input("\033[95mFigura desconhecida: Meu nome é Ana. Qual o seu nome?\033[0m")
                    time.sleep(2)
                    print(f"\033[95mAna: {nome}, hm... um nome bonito, mas não tem importância nesse mundo\033[0m")
                    time.sleep(2)
                    print("\033[95mAna: Bem, vamos seguir juntos por enquanto, a floresta é perigosa.\033[0m")
                case 3:
                    print(f"\033[95mFigura desconhecida: Um/a {Eu['classe']}? Interessante, não vejo muitos por aqui\033[0m")
                    time.sleep(3)
                    nome = input("\033[95mFigura desconhecida: Meu nome é Ana. Qual o seu nome?\033[0m")
                    time.sleep(2)
                    print(f"\033[95mAna: {nome}, hm... um nome bonito, mas não tem importância nesse mundo\033[0m")
                    time.sleep(2)
                    print("\033[95mAna: Bem, vamos seguir juntos por enquanto, a floresta é perigosa.\033[0m")
    case 2:
        time.sleep(1)
        print("O sol quente lhe acorda")
        time.sleep(1)
        print("Você está escorado em um poço no meio de uma pequena vila")
        time.sleep(1)
        print("O sol é quente")
        time.sleep(0.5)
        print("...")
        time.sleep(1)
        if Classe == 7 or Classe == 5 or Classe == 1:
            Eu['dano_base'] += 20
            print("\033[33mO sol recuperou seu vigor\033[0m")
        else:
            print("\033[31m++Insolação\033[0m")
            Eu['vida'] -= 15
        time.sleep(1)
        print("Você não se lembra exatamente que vila é essa, entretanto")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print(f"As pessoas te reconhecem, você é um famoso {Eu['classe']}")
        time.sleep(1)
        print("Te contam sobre um dragao de nove cabeças")
        time.sleep(1)
        print("Querem que você derrote esse monstro.\n")
        time.sleep(0.5)
        print("\033[31mVOCÊ\033[0m")

        print("Escuta um rugido")
        time.sleep(0.5)
        print("A longe, você avista...")
        time.sleep(0.5)
        print("\033[31mHIDRA\033[0m\n")
        time.sleep(1)
        rotas = int(input("Há três rotas para chegar a hidra, qual você escolhe?\n1:Floresta(Costeando a montanha) 2:Caverna(Através da montanha) 3:Escalada(Por cima da montanha)\n"))
        match rotas:
            case 1:
                print("\nGoblin lhe recepciona\n")

                fisico(Eu, Goblin)
            case 2:
                print("\nOrc Lhe recepciona\n")

                fisico(Eu, Orc)
            case 3:
                print("\nLobo te recepciona\n")

                fisico(Eu, Lobo)
    case 3:
        time.sleep(1)
        print("\033[31mVocê não acorda\033[0m")
        if Classe == 4:
            time.sleep(1)
            print("\033[31mA morte te rejeita\033[0m")
            time.sleep(1)
            print("Você retorna a vida\033[0m")
            time.sleep(1)
            print("\033[31mAgora você controla a morte\033[0m")
            time.sleep(1)
            print("\033[32mVocê se sente mais forte por ter retornado da morte\033[0m")
            time.sleep(1)
            print("Você se levanta, e percebe que está em um local desconhecido, um cemitério. O chão é coberto por folhas secas e o ar é úmido e frio.")
            time.sleep(1)
            print("Enquanto você tenta se orientar, você ouve um barulho vindo de uma cripta próxima.")
            time.sleep(1)
            print("\033[35mIndo investigar, você vê um esqueleto se levantando de dentro da cripta, ele te encara com olhos vazios e começa a se aproximar de você.\033[0m")
            time.sleep(1)
            print("\033[31mEle saca a espada e vai te atacar\033[0m")
            time.sleep(1)
            fisico(Eu, Esqueleto)
            time.sleep(1)
            print("Você derrotou o esqueleto, mas ele te deixou ferido.")
            time.sleep(1)
            print("\033[35mVocê se sente mais forte derrotando um morto-vivo, aumentando seu poder\033[0m")
            Eu['dano_base'] += 30
            time.sleep(1)
            print("Você continua a explorar o cemitério, e encontra uma tumba com um nome gravado nela, é o nome de um antigo necromante que viveu há muito tempo atrás.")
            time.sleep(1)
            print("Ao abrir a tumba, você encontra um grimório antigo, cheio de feitiços e conhecimentos proibidos sobre a necromancia.")
            time.sleep(1)
            escolha = int(input("Você estuda o grimório e aprende um feitiço poderoso, mas perigoso, o que você faz?\n1:Aprender o feitiço 2:Deixar o grimório de lado\n"))
            match escolha:
                case 1:                    
                    print("Você decide aprender o feitiço, mesmo sabendo dos riscos envolvidos.")
                    time.sleep(1)
                    print("Ao estudar o grimório, você descobre um feitiço de necromancia tão poderoso que pode controlar os mortos-vivos, mas também tem um efeito colateral perigoso, ele pode corromper a sua alma e te transformar em um monstro sedento por sangue.")
                    time.sleep(1)
                    print("Você decide arriscar e aprender o feitiço, e ao lançá-lo, você sente uma onda de poder percorrer seu corpo, mas também sente uma escuridão crescente dentro de você.")
                    time.sleep(1)
                    print("Você reanima dois esqueletos para lutarem ao seu lado, mas saber de tudo é perder tudo. A escuridão dentro de você começa a te consumir, e você sente que está perdendo o controle sobre si mesmo.")
                    Eu['vida'] -= 20
                    time.sleep(1)
                    print("\033[33m+++ Classe\033[0m")
                    time.sleep(0.7)
                    print("\033[35mVocê agora é um Lich\033[0m")
                    Eu['classe'] = "Lich"
                    Eu['dano_base'] = 30
                    Eu['chance'] += 3
                    time.sleep(1)
                    print("Sem tempo para ficar se remoendo, você e seus servos avançam na cripta e havistam um ser enorme, com várias cabeças de serpente")
                    time.sleep(1)
                    print("\033[31mH I D R A\033[0m")
                    time.sleep(1)
                    print("A hidra, enfurecida por ter sido despertada, ataca você e seus servos, e a batalha começa.")
                    time.sleep(1)
                case 2:                    
                    print("Você decide deixar o grimório de lado, e seguir explorando a cripta")
                    time.sleep(1)
                    print("Enquanto explora, você encontra um ser enorme, com várias cabeças de serpente")
                    time.sleep(1)
                    print("\033[31mH I D R A\033[0m")
                    time.sleep(1)
                    print("A hidra, enfurecida por ter sido despertada, ataca você, e a batalha começa.")
                    time.sleep(1)
        time.sleep(1)
    case 4:
        print("Voce está em queda livre.")
        time.sleep(0.5)
        print("O que você faz?")
        time.sleep(1)
        print("1:Manter posição de voo")
        time.sleep(0.5)
        print("\033[31m2:Manter-\033[0m")
        time.sleep(0.2)
        print("\033[31mVocê caiu.\033[0m")
        time.sleep(0.3)
        print("\033[33m- Vida\033[0m")
        if Classe != 6:
            Eu['vida'] -= 45
        Eu['dano_base'] = random.randint(20, 30)
        time.sleep(1)
        print("Você se sente mais forte por ter sobrevivido a isso")
        time.sleep(1)
        Eu['dano_base'] += 10
        time.sleep(2)
        print("Você se levanta, e percebe que está em um local desconhecido, uma floresta densa e escura, o chão é coberto por folhas secas e o ar é úmido e frio.")
        time.sleep(1)
        print("Enquanto você tenta se orientar, você ouve um barulho vindo de trás de uma árvore próxima.")
        time.sleep(1)
        print("\033[31mV\033")
        time.sleep(0.3)
        print("\033[31mE\033")
        time.sleep(0.3)
        print("\033[31mN\033")
        time.sleep(0.3)
        print("\033[31mH\033")
        time.sleep(0.3)
        print("\033[31mA\033")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("\033[31mM\033")
        time.sleep(0.3)
        print("\033[31mE\033")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("\033[31mE\033")
        time.sleep(0.3)
        print("\033[31mN\033")
        time.sleep(0.3)
        print("\033[31mC\033")
        time.sleep(0.3)
        print("\033[31mO\033")
        time.sleep(0.3)
        print("\033[31mN\033")
        time.sleep(0.3)
        print("\033[31mT\033")
        time.sleep(0.3)
        print("\033[31mR\033")
        time.sleep(0.3)
        print("\033[31mA\033")
        time.sleep(0.3)
        print("\033[31mR\033[0m")
        time.sleep(1)
        print("A voz grita dentro da sua cabeça, você sente um medo profundo, como se algo muito poderoso estivesse te observando.")
        time.sleep(1)
        print("Você tenta se acalmar, mas a voz continua a gritar, cada vez mais alto, até que você sente uma presença atrás de você.")
        time.sleep(1)
        print("\033[31mV\033")
        time.sleep(0.3)
        print("\033[31mI\033")
        time.sleep(0.3)
        print("\033[31mR\033")
        time.sleep(0.3)
        print("\033[31mE\033[0m")
        time.sleep(1)
    case 5: 
        print("Você acorda e cultistas lhe rodeiam.")
        time.sleep(0.8)
        print("Eles gritam: Viva ao rei demonio!!!")
        time.sleep(2)
        print("Eles te veneram")
        if Classe == 1:
            print("\033[31mVocê se enfurece\033[0m")
            Eu['dano_base'] += 30
        print("Eles clamam por uma ordem")
        time.sleep(1)
        print("Você sente que tem que escolher um lado, ou se junta a eles ou os derrota")
        time.sleep(1)
        escolha = int(input("\033[35m1:Juntar-se a eles 2:Derrotar os cultistas\033[0m\n"))
        match escolha:
            case 1:
                print("\033[33mVocê se junta aos cultistas\033[0m")
                time.sleep(1)                
                print("Você se sente mais forte por ter se juntado a eles")
                Eu['dano_base'] += 20
                time.sleep(1)
                print("Eles te contam sobre a hidra, e que ela é um monstro de 9 cabeças que aterroriza o mundo e destrói a paz")
                time.sleep(1)
                print("Eles te dizem que a hidra é um monstro tão poderoso que nem eles conseguem derrotar, e que eles querem sua ajuda para derrotar a hidra, e que juntos vocês podem dominar o mundo")
                time.sleep(1)
                print("A ideia de poder absoluto te seduz, e você aceita a proposta dos cultistas")
                time.sleep(1)
            case 2:
                print("Você se prepara para lutar")
                time.sleep(1)
                print("Os cultistas te atacam")
                time.sleep(1)
                fisico(Eu, Cultistas)
                fisico(Eu, Cultistas)
                print("Você derrotou os cultistas, mas eles te deixaram ferido")
                time.sleep(1)
                print("Você examina o local e encontra um mapa, nele tem a localização da hidra, e um caminho para chegar até ela")
                time.sleep(1)
                print("Você sente que tem que seguir esse caminho, e se preparar para a batalha contra a hidra para salvar o mundo de um desastre maior")
    case 6:
        print("\033[35mA árvore do mundo lhe recepciona\033[0m")
        time.sleep(2)
        print("Você foi abençoado")
        Eu['dano_base'] += 12
        Eu['velocidade'] += 1
        if Classe == 5:
            time.sleep(2)
            print("\033[32mVocê absorveu a benção\033[0m")
            Eu['dano_base'] += 10
            Eu['velocidade'] += 2
        print("Você sente que a árvore do mundo lhe deu uma missão")
        time.sleep(1)
        print("Você deve derrotar a Hidra, o monstro de 9 cabeças que aterroriza o mundo e destrói a paz")
        time.sleep(1)
        print("Mas enquanto pensa nisso, três fadas aparecem e te atacam")
        time.sleep(1)
        fisico(Eu, Fada)
        fisico(Eu, Fada)
        fisico(Eu, Fada)
        print("Você derrotou as fadas, mas elas te deixaram ferido")
        time.sleep(1)
        print("Agora sim, você sente que pode prosseguir com os seus deveres e derrotar a Hidra")
    case 7:
        print("Enquanto você dormia tranquilamente, sua hospedagem foi bombardeada")
        time.sleep(1)
        print("-Vida")
        Eu['vida'] -= 10
        if Classe == 2:
            print("Você se sente mais forte por ter sobrevivido a isso")
            Eu['dano_base'] += 10
        if Classe == 3:
            print("Você se sente mais ágil por ter sobrevivido a isso")
            Eu['velocidade'] += 2
        time.sleep(2)
        print("Você sai para a rua para investigar o que aconteceu")
        time.sleep(1)
        print("Você vê destroços, chamas e um rastro de sangue. Você segue o rastro")
        time.sleep(1)
        print("O rastro de sangue te leva a um beco, onde você vê um urso devorando o corpo do dono da hospedagem")
        time.sleep(1)
        print("O urso te vê e te ataca")
        vida = fisico(Eu, Urso)
        if vida > 0:
            time.sleep(1)
            print("Você sobreviveu ao ataque do urso, mas ele te deixou ferido")
            time.sleep(1)
            print(("Sua mente está confusa, você não sabe o que aconteceu, mas uma figura se forma claramente na sua mente"))
            time.sleep(1)
            print("A figura tem 9 cabeças, e você sente que ela é a responsável por tudo que aconteceu")
            time.sleep(1)
            print("Você sente que precisa derrotar essa criatura, pelos seus amigos, pelas vítimas do massacre e você sabe que ela está próxima")
            time.sleep(1)
            print("A criatura clama pelo seu nome. Você caminha em direção da voz e adentra a floresta sombria que se forma a sua frente")
        else:
            exit()

# ----- Saída e entrada no loop do boss ----- #

time.sleep(1)
print(f"\nVocê se enche de determinação, {Eu['classe']} se torna obstinado(a)")
time.sleep(1)
print("\033[36mVocê sempre volta\033[0m\n")
time.sleep(0.5)
print("\033[33m+\033[0m")
time.sleep(0.5)
print("\033[33m+\033[0m")
time.sleep(0.5)
print("\033[33m+\033[0m\n")
time.sleep(1)

# ----- Loop Hidra ----- #
if Eu['vida'] > 0:

    while Hidra['vida'] > 0 and Eu['vida'] > 0:
        inimigo = inimigos[random.randint(1, 7)]
    
        print(f"{inimigo['nome']} encontra(m) você(s)")
        time.sleep(2)
        vida = fisico(Eu, inimigo)

        if vida > 0:
            endgame = int(input("Deseja enfrentar Hidra?\n1:S 2:N\n"))

            if endgame == 1:
                if Lugar == 1:
                        print("\033[32mAna se junta a batalha\033[0m")
                        Eu['turno'] = "Você e Ana atacam"
                        Eu['dano_base'] += random.randint(15, 30)
                        time.sleep(1)
                if Lugar == 3 and escolha == 1:
                        print("\033[32mOs esqueletos se juntam a batalha\033[0m")
                        Eu['turno'] = "Você e os esqueletos atacam"
                        Eu['dano_base'] += random.randint(17, 33)
                        time.sleep(1)        
                if Lugar == 5 and escolha == 1:
                        print("\033[32mOs cultistas se juntam a batalha\033[0m")
                        Eu['turno'] = "Você e os cultistas atacam"
                        Eu['dano_base'] += random.randint(20, 35)
                        time.sleep(1)
                vida = fisico(Eu, Hidra)

                if vida > 0:
                    Hidra['vida'] = 0
                    print("\033[32mVocê venceu Hidra.\033[0m")
                    time.sleep(1)
                    print("\033[35mHidra já não reside aqui\033[0m")
                    time.sleep(1)
                    print("\033[31mVocê venceu Hidra.\033[0m")
                    time.sleep(1)
                    print("O vento começa a cantar\033[0m")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("\033[31mO vento começa a cantar\033[0m")
                    time.sleep(1)
                    print("\033[35m♪ Onde você se esconde? ♪\033[0m")
                    time.sleep(1)
                    decisao = ""
                    while decisao != Eu['classe']:
                        decisao = (input("\033[35mO que é você? \033[0m"))
                    time.sleep(1)
                    while decisao != Eu['nome']:
                        decisao = (input("\033[35mQuem é você? \033[0m"))
                    time.sleep(1)
                    print("\033[32mVocê venceu Hidra.\033[0m")
                    time.sleep(2)
                    print("\033[31mDos restos de Hidra se levanta outra criatura.\033[0m")
                    time.sleep(1)
                    print("\033[35mVocê venceu Hidra.\033[0m")
                    time.sleep(3)
                    print("\033[31mVocê percebe Hidra falsa.\033[0m\n")
                    time.sleep(1)
                    vida = fisico(Eu, Hidra_Falsa)
                    if vida > 0:
                        print("\nVocê venceu, obrigado por jogar!")
                    else:
                        print("\nTente novamente\n")
                else:
                    # Volta pro inicio
                    print("\n")
else:
    print("\033[31mVocê não é digno\033[0m")

                    