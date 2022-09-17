# Grade Horária
Registra, exclui e exibe matérias em seus respectivos horários, na forma de uma grade horária.

Exercício e antigo trabalho da matéria Algoritmos e Programação de Computadores

* Particularidades:
  * Código da Matéria:
    + Os códigos seguem o formato da UnB, em que os três primeiros caracteres são letras maiúsculas indicando o departamento que oferece a matéria, e os próximos 4 são digítos representando qual é a matéria.
    + Além disso, neste código há uma ultima letra após esses 7 caracteres para indicar a turma na qual se está matriculado.
  * Formato dos Horários:
    + Novamente, segue-se o padrão da UnB, explicado no site da universidade: https://noticias.unb.br/67-ensino/4317-tire-suas-duvidas-sobre-o-sigaa# (Subtópico "Como entender os dias e horários de aulas?")
    + Há 5 hoários matutinos, 6 vespertinos e 4 noturnos, com 10 minutos de pausa após 2 horários seguidos:
      * Os horários diurnos tem duração de 55 minutos.
      * Os horários noturnos tem duração de 50 minutos.

* Comandos:
  + Obs1: Não utilizar aspas
  + Obs2: Haverá erro de sintaxe caso o comando não seja válido


  * Adicionar horários:
    + Formato:
      + '+' {código da matéria} {todos os horários em que se quer adicionar esta matéria, de forma conjunta ou separada}
    + Ação:
      + Se não há nenhuma outra matéria ocupando os horários solicitados, adiciona a matéria ao dicionário que organiza os dados.
      + Caso contrário, retorna uma mensagem de erro da seguinte forma: !({comando}) 
  * Retirar horários:
    + Formato:
      + '-' {código da matéria} {todos os horários em que há esta matéria, de forma conjunta ou separada}
    + Ação:
      + Se há no dicionário a matéria em todos os horários dados, retira essa matéria do dicionário.
      + Caso contrário, retorna uma mensagem de erro no formato: !({comando})
  * Exibir a grade horária:
    + Formato:
      + ?
    + Ação:
      + Exibe todas as matérias registradas pelo aluno, exibindo-as apenas nos horários e dias fornecidos no momento em que ela foi registrada.
      + Apenas exibe os horários nos quais há alguma matéria registrada.
  * Terminar o código:
    + Formato:
      + Hasta la vista, beibe!
    + Ação:
      + Sai do loop de receber os comandos acima, logo terminando a execução do programa.
