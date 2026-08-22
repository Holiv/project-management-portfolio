# Comparador de cronogramas e gerador de relatórios

**Motor VBA (Excel ↔ MS Project), em uso semanal** · aplicado em produção; versão genérica
planejada

## Contexto

As reuniões quinzenais e o reporte semanal exigiam uma análise comparativa dos cronogramas
entregues pelas contratadas: o que mudou desde a semana passada, onde o desvio cresceu, que
marcos escorregaram. Com múltiplas contratadas e dezenas de entregas ao longo do contrato, o
volume de análise manual só cresceria.

## Proposta

Um sistema que lê **dois snapshots do mesmo cronograma** — a entrega atual e a anterior — e
gera, em um comando, o relatório executivo completo do ciclo: avanço previsto × realizado,
decomposição do desvio por disciplina ponderada pelo peso, marcos com desvio de datas,
tendência das próximas seis semanas e série histórica de todo o contrato.

## Como funciona

- **Dois modos de entrada**: standalone (o Excel abre os dois arquivos e cria a própria
  instância do MS Project) ou como suplemento dentro do Project, recebendo a instância viva.
- **Tendência projetada do cronograma corrente**, não da linha de base — porque o previsto
  da linha de base, por definição, nunca varia entre execuções; a tendência que informa
  decisão é a do arquivo vivo.
- **Série histórica sem banco de dados**: cada relatório carrega a tabela completa do
  histórico numa aba oculta, e a execução seguinte a lê do relatório anterior. A persistência
  viaja com o próprio artefato — zero infraestrutura, zero dependência de rede.
- **Relatório autônomo**: o template "empresta" seus módulos ao relatório gerado, então cada
  relatório funciona sozinho — botões de PDF, imagem para ata e envio ao aplicativo
  continuam operantes em qualquer máquina.
- **Integração com o ecossistema**: um botão no relatório o envia via API ao
  [aplicativo de acompanhamento](../ecossistema-de-acompanhamento-de-obras/), que consome os
  dados, gera as visualizações e notifica os gestores.

## Resultado

- O comparativo semanal que exigia análise manual arquivo a arquivo passou a ser **gerado em
  um comando** — e o mesmo relatório serve à reunião, à ata e ao aplicativo.
- Da publicação à leitura: gestores notificados e consultando avanço e desvio **em dois
  cliques, de onde estiverem** — a informação deixou de depender de abrir o computador.
- Histórico completo do contrato preservado **sem nenhum servidor**: a série viaja nos
  próprios relatórios.
- *Em levantamento: horas de análise manual por ciclo antes × depois; número de ciclos já
  processados.*

## Capacidades demonstradas

VBA avançado com arquitetura desacoplada (extração → motor → relatório) · interoperabilidade
COM entre Excel e MS Project — incluindo o tratamento do comportamento de instância única do
Project, causa clássica de defeito nesse tipo de integração · desenho de persistência
portátil sem infraestrutura · integração via API com aplicação web · **percepção de produto**:
identificar que o limite seguinte era o acesso, e resolvê-lo.

→ [Arquitetura e decisões técnicas](arquitetura.md)
