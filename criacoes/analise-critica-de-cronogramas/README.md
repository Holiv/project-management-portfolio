# Sistema de análise crítica de cronogramas

**Método provado em análise real, depois codificado em macros dentro do próprio MS Project**
· em uso; versão genérica planejada

## Contexto

Quem contrata obra recebe o cronograma da contratada e precisa dizer se ele se sustenta. Na
prática, isso é feito por leitura e experiência — o que não escala para centenas de
atividades por entrega, não se repete igual entre semanas, e não deixa rastro: quando a
contratada contesta um achado, a discussão vira opinião contra opinião.

## Proposta

Transformar o faro em **verificações nomeadas, com código estável**, executáveis por
qualquer pessoa dentro do próprio MS Project — e um relatório em que **cada achado diz de
onde saiu e como conferir**.

## Do método à ferramenta

A ordem de construção é parte do resultado: **primeiro a análise, depois o código**. A
primeira análise crítica foi executada com um pipeline próprio (Python + MPXJ) sobre uma
entrega real de 510 atividades — e cada verificação nasceu de um achado dessa análise,
nenhuma foi inventada por completude. Só então o método foi codificado em macros VBA, para
que a mesma auditoria rodasse dentro do próprio MS Project, por qualquer pessoa, a cada
entrega.

## Como funciona

- **Verificações em três camadas, e a ordem é parte do método**: primeiro a integridade da
  rede (execução fora de sequência, inversões totais), porque datas recalculadas sobre uma
  rede violada são números derivados de premissa falsa; depois aderência de datas; por fim
  consistência de apontamento.
- Cada verificação **marca as atividades e aplica filtro e tabela próprios** — o resultado é
  navegável no próprio cronograma, no contexto, e conferível na reunião com a contratada.
- **Nada é alterado** no arquivo: apenas um campo marcador e a exibição, com rotina de
  limpeza. As macros são imunes a idioma da instalação (propriedades em inglês, nomes de
  campo resolvidos em tempo de execução).
- **Um comando gera o relatório completo** — visual moderno, gráficos, lista de achados com
  identificadores, exportação em PDF — incluindo a seção *"como reproduzir qualquer número
  deste relatório"*.
- Distribuição por instalador: modelo global + template, para uso em qualquer máquina da
  equipe.

## Resultado

Na análise fundadora (entrega de **510 atividades** de um trecho de ~22 km), o método
encontrou — com evidência reproduzível:

- **60 vínculos de rede violados** na data de status, com 8 inversões totais (sucessora
  concluída, predecessora nem iniciada);
- um **adiantamento agregado de +3,72 p.p. que era ilusório**: atividades fora de sequência
  cobrindo aritmeticamente atividades que deveriam estar concluídas e estavam em zero;
- **86,9% do custo de linha de base em 0,0% previsto e 0,0% realizado** — não havia
  adiantamento onde estava o dinheiro, havia ausência de partida;
- reserva de improdutividade climática **aplicada no ano errado** em parte das atividades —
  otimismo de duração da ordem de 30%, invisível a olho nu.

Em seguida, já como macro em uso real, o mesmo conjunto de critérios auditou o cronograma de
uma **segunda contratada — 5.251 atividades folha — com o relatório completo gerado em um
comando**. A análise que dependia de experiência individual virou **procedimento executável,
auditável e escalável**: de 510 para 5.251 atividades com os mesmos critérios, e a discussão
com a contratada passou de opinião para evidência conferível.

*Tempos de execução e comparativo com a análise manual: em levantamento — entram com data e
método de medição.*

## Capacidades demonstradas

Domínio da mecânica interna do MS Project (rede, calendários, campos, unidades internas) ·
desenho de auditoria com código estável por achado · automação VBA robusta a idioma ·
geração de relatório reprodutível · **a disciplina de método**: cada verificação nasceu de um
achado real — nenhuma foi inventada por completude, e duas foram removidas ao se mostrarem
redundantes.

→ [Arquitetura e decisões técnicas](arquitetura.md)
