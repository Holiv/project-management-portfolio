# Linha do tempo

Como as criações se encadeiam — cada ferramenta nasceu de um limite encontrado na anterior.

## Antes de 2026 — a base

Mais de dez anos de engenharia civil, incluindo prática independente com **~100 projetos e
mais de 1.200 ARTs**, e a transição deliberada para desenvolvimento de software como segunda
competência — não como troca de carreira, mas como instrumento da primeira.

## Jun–Ago 2026 — o ecossistema de acompanhamento

O acompanhamento de obras de um programa rodoviário multi-contrato era manual e disperso.
Em **dois meses (329 commits)**, concebi e implementei uma plataforma web completa:
importação nativa de cronogramas (MS Project, via serviço próprio em Java), curva S,
retigráfico com lançamento de avanço, mapa com lançamento por posição, monitoramento de
chuva, relatórios e assistente de IA.

## Jul 2026 — o comparador de cronogramas

As reuniões quinzenais exigiam comparar a entrega semanal de cronograma de cada contratada
com a anterior — trabalho manual crescente. Construí um motor VBA (Excel ↔ MS Project) que
gera o comparativo completo em um comando, com **tendência de 6 semanas** e **série
histórica embutida nos próprios relatórios**, sem banco de dados.

Em seguida, o limite: o relatório ainda exigia abrir o computador. A resposta foi um módulo
no ecossistema que **consome o relatório via API** — um botão no próprio relatório o envia ao
aplicativo, e qualquer gestor é notificado e consulta os dados **em dois cliques, de onde
estiver**.

## Ago 2026 — a análise crítica de cronogramas

Analisar a qualidade de um cronograma entregue dependia de leitura e experiência. Codifiquei
as verificações — cada uma nascida de um achado real, nenhuma inventada por completude — em
macros que rodam **dentro do próprio MS Project** e geram relatório reprodutível: cada achado
diz de onde saiu e como conferir.

## Ago 2026 — a plataforma aberta

Os sistemas acima pertencem ao contexto onde nasceram. O **método** deles está sendo
reconstruído do zero na plataforma aberta [Chainage](https://github.com/Holiv/chainage)
(Apache-2.0): modelo canônico de programa de infraestrutura + perfil de mapeamento
declarativo, para servir a qualquer organização sem mudar código.

## Em paralelo — gestão de equipe

O sistema de gestão de equipe (competências em escala Dreyfus, metas, RACI, acompanhamento)
entrou em uso real pela equipe de planejamento, com uma decisão de longo prazo: **captura
mensal de série longitudinal** de competência × desempenho — dado que quase nenhuma equipe
tem, coletado com consentimento informado desde o primeiro registro.
