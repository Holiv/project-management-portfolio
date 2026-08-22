# Ecossistema de acompanhamento de obras

**Plataforma web de project controls, em produção** · aplicação corporativa (repositório
privado do empregador, de minha autoria — histórico de commits verificável) · versão genérica
aberta em construção: [Chainage](https://github.com/Holiv/chainage)

## Contexto

O acompanhamento de um programa rodoviário multi-contrato dependia de arquivos dispersos:
cronogramas das contratadas em MS Project, medições em planilha, curvas montadas à mão,
relatórios remontados a cada ciclo. A informação existia, mas não em um lugar só — e cada
pergunta simples ("como está o avanço da frente X?") custava abrir arquivos.

## Proposta

Uma plataforma web única onde o cronograma entra **no formato nativo** (.mpp, sem conversão
manual), o avanço é lançado onde a obra acontece — por formulário, pelo mapa ou pelo
retigráfico — e toda leitura (curva, desvio, relatório) deriva do mesmo dado.

## Como funciona

- **Cronograma** — importação nativa de MS Project via serviço próprio de leitura (Java +
  MPXJ), com snapshots imutáveis por entrega e validações que recusam arquivo inconsistente
  (data de status divergente, avanço em data futura).
- **Curva S** — prevista × realizada por frente, com o rateio da quantidade no tempo
  **reproduzindo o cálculo do MS Project ao centavo** — incluindo calendários com exceções,
  jornadas parciais e retomadas de tarefa interrompida.
- **Retigráfico (gráfico tempo-caminho)** — a obra linear vista por quilometragem × tempo,
  com lançamento de avanço diretamente no gráfico.
- **Mapa** — lançamento e visualização georreferenciados, com posição por estaca/km projetada
  sobre o eixo da rodovia.
- **Clima** — coleta diária de chuva por localização, como variável explicativa de
  produtividade.
- **Relatórios e painel executivo** — leitura de uma página para gestão.
- **Assistente de IA** — consulta em linguagem natural sobre os dados do programa.
- **Recepção de relatórios via API** — o [comparador de cronogramas](../comparador-de-cronogramas/)
  envia seu relatório ao aplicativo com um clique; gestores são notificados e consultam em
  qualquer lugar.

## Resultado

- **Fonte única de verdade** para avanço físico: o mesmo dado alimenta curva, mapa,
  retigráfico e relatório — eliminando a reconciliação manual entre planilhas.
- Informação de avanço e desvio acessível **em 2 cliques, de qualquer dispositivo**, por
  qualquer gestor autorizado — antes, exigia abrir arquivos no computador.
- Cronogramas de até **6.483 atividades (60 MB)** processados com validação automática — com
  travas que já impediram, em produção, avanço lançado em data futura e dupla contagem por
  inconsistência de grafia.
- Escala de entrega: **329 commits em dois meses**, ~11 domínios funcionais, 48 migrations —
  concepção, implementação e operação por uma pessoa.
- *Em levantamento: horas economizadas por ciclo de medição, usuários ativos, volume de
  relatórios processados.*

## Capacidades demonstradas

Arquitetura de produto e visão de plataforma · desenvolvimento full-stack (TypeScript,
Next.js) · serviço de integração em Java (MPXJ) · modelagem de dados com segurança por linha
(RLS) · geoprocessamento aplicado a obra linear · integração de IA · e a capacidade-síntese:
**traduzir o método de project controls em software que a operação usa de verdade**.

→ [Arquitetura e decisões técnicas](arquitetura.md)
