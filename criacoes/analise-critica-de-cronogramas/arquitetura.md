# Arquitetura — análise crítica de cronogramas

## Estrutura

Dois módulos VBA: o de análise (verificações, filtros, tabelas e agrupamentos dentro do
Project) e o de relatório (coleta, aplica os mesmos critérios e injeta os dados num template
HTML com gráficos e exportação em PDF). Instalador distribui modelo global + template.

## Decisões que valem registro

- **Código estável por achado.** "A1" continua sendo A1 quando a implementação muda — é o que
  permite falar de um problema ao longo de semanas e entregas.
- **Rodar onde o dado está.** A verificação acontece dentro da ferramenta, sem exportação ou
  pipeline. Verificação que exige preparação não é rodada semanalmente; uma que é um atalho
  de teclado, sim.
- **Imunidade a idioma**: toda a lógica usa propriedades do modelo de objetos (sempre em
  inglês); nomes visíveis de campos são resolvidos em tempo de execução — a macro pergunta à
  instalação como o campo se chama, em vez de supor.
- **Convenção de contagem explícita.** Um mesmo conjunto de vínculos violados produz
  contagens diferentes conforme se conte sucessoras, predecessoras ou atividades distintas —
  todas defensáveis. A contagem oficial é alinhada à da própria ferramenta, porque divergir
  da convenção que a outra parte vê é entregar a discussão.
- **Separar problema de execução de problema de registro**: uma predecessora 100% física sem
  término real não conta como quebra de rede — migra para um achado próprio de apontamento
  pendente. Sem essa regra, a conversa com quem executa começa acusando a coisa errada.
- **Unidades internas respeitadas**: medidas de tempo do Project são armazenadas em minutos
  sobre a jornada configurada — toda comparação deriva de uma constante lida do arquivo,
  nunca de número mágico.

## Genérico × aplicado

As verificações e o relatório são transferíveis a qualquer obra; as convenções de campo
corporativas (situação, justificativa) são pontos de configuração identificados para a
versão genérica.
