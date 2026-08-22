# Portfólio de Gerenciamento de Projetos

**Helton da Silva de Oliveira** · Engenheiro Civil (CREA-RJ) · Analista de Planejamento Sênior

> Construo as ferramentas que empresas de infraestrutura usam para planejar e acompanhar
> suas obras — **de quem alimenta o dado em campo a quem decide com ele na gestão**. Este
> repositório documenta o que foi construído, como funciona e **que resultado produziu**.

🌐 **Versão navegável:** [holiv.github.io/project-management-portfolio](https://holiv.github.io/project-management-portfolio/) · 🇧🇷 PT-BR *(versão bilíngue em preparação)*

---

## O que há aqui

Quatro sistemas concebidos, projetados e implementados por mim, todos **em uso real** no programa de
concessão da **Arteris** na BR-101/RJ. Cada um está documentado em duas partes:
a **narrativa** — o problema, a solução e o resultado — e a **arquitetura** — como foi
implementado, sem exposição de dados sensíveis.

| Criação | O que é | Estado |
|---|---|---|
| [**Ecossistema de acompanhamento de obras**](criacoes/ecossistema-de-acompanhamento-de-obras/) | Plataforma web completa de *project controls*: cronograma, curva S, retigráfico, mapa, clima, relatórios e assistente de IA | Em produção |
| [**Comparador de cronogramas**](criacoes/comparador-de-cronogramas/) | Motor VBA que compara entregas semanais de cronograma e gera relatório executivo com tendência e histórico embutido | Em uso semanal |
| [**Análise crítica de cronogramas**](criacoes/analise-critica-de-cronogramas/) | Verificações codificadas que auditam um cronograma entregue e produzem relatório reprodutível — dentro do próprio MS Project | Em uso |
| [**Gestão de equipe e competências**](criacoes/gestao-de-equipe/) | Sistema de gestão de equipe: competências (escala Dreyfus), metas, RACI, acompanhamento — com série longitudinal de dados | Em uso pela equipe |

**Versão genérica e aberta:** o método destes sistemas está sendo reconstruído, do zero e sem
dado corporativo, na plataforma aberta **[Chainage](https://github.com/Holiv/chainage)**
(Apache-2.0) — uma base de código, implantável por qualquer organização via perfil de
mapeamento declarativo.

## Em números

| | |
|---|---|
| Sistemas em uso real | **4** |
| Maior sistema | **329 commits em 2 meses** · 48 migrations · ~11 domínios funcionais |
| Maior cronograma processado | **6.483 atividades** (60 MB), lido e rateado no tempo **reproduzindo o MS Project ao centavo** |
| Verificações de análise crítica | **12 concebidas** a partir de achados reais → 6 ativas + 2 em standby |
| Acesso à informação de avanço | de "abrir o arquivo no computador" para **2 cliques, de qualquer lugar** |

*Números operacionais (horas economizadas por ciclo, usuários ativos, relatórios gerados)
estão em levantamento e serão incorporados com data e método de medição.*

## Como ler

- Cada criação: [`README.md`](criacoes/) = narrativa (contexto → proposta → funcionamento →
  **resultado** → capacidades demonstradas) · `arquitetura.md` = implementação e decisões.
- [**Onde os sistemas operam**](onde-operam.md) — o programa, as pessoas e o ciclo em que tudo roda.
- [**Linha do tempo**](linha-do-tempo.md) — a sequência de criação e como uma ferramenta levou à outra.
- [**Capacidades**](capacidades.md) — matriz habilidade × onde foi demonstrada.

## Nota de integridade

Este portfólio referencia sistemas em produção na Arteris, meu empregador — citados como um
currículo cita: o vínculo, a autoria (verificável pelo histórico de commits dos repositórios
privados) e informações públicas do programa. **Nenhum dado interno, contratual ou pessoal de
terceiros aparece aqui** — os números são de escala, engenharia e informação pública.

---

📫 [LinkedIn](https://www.linkedin.com/in/helton-so/) · [GitHub](https://github.com/Holiv)
