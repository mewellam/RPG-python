# RPG-python
RPG de texto em Python com combate em turnos, classes e progressão de nível.

Como funciona?
- De início pergunta o nome do seu personagem (Que é guardado no dicionário do seu personagem, mesmo lugar onde guarda vida e outros status.)
- Depois pede para escolher sua classe (Cada classe com diferentes atributos e ataques)
- Então um cenário é escolhido (7 cenários ao todo, cada cenário com suas próprias características. Alguns cenários dão vantagem a certas classes.)
- Batalhas por turno (RNG de ataque, dependendo do número que cair no "dado", o ataque pode ser melhor ou pior.)
- Após os cenários, você ganha a chance de enfrentar o boss final.

A batalha foi feita através de apenas uma função que é chamada nos cenários e no boss.

Os cenários utilizam de match case.

Dicionarios para: Inimigos, invocações, personagem (usuário), ataques e ataques de classe especifica.
