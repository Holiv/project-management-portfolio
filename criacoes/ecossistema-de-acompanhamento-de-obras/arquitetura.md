# Arquitetura — ecossistema de acompanhamento

## Visão geral

Aplicação web (TypeScript, Next.js, React, Tailwind, PWA) sobre PostgreSQL com Row-Level
Security, e um **serviço separado de leitura de cronogramas** em Java (biblioteca MPXJ),
containerizado e sem estado, chamado apenas servidor-a-servidor. A separação é deliberada: a
leitura de .mpp/.xer é um problema de JVM; o produto é um problema de web — cada um na sua
runtime.

## Decisões que valem registro

- **Snapshot imutável por entrega.** Cada cronograma recebido vira um snapshot com hash;
  reenvio duplicado é recusado. O histórico não se reescreve.
- **Acervo semanal por (frente, semana).** A semana é declarada no upload e **conferida
  contra a data de status do arquivo** — divergiu, recusa. A trava transforma erro humano
  silencioso em recusa explícita.
- **Rateio no tempo fiel à ferramenta de origem.** O rateio de quantidades reproduz o
  MS Project ao centavo, incluindo os mecanismos internos menos documentados — retomada de
  tarefa interrompida (Stop/Resume), calendários com centenas de exceções, jornadas com
  intervalo. Validado caso a caso contra a ferramenta, número a número.
- **Validações que protegem a série histórica**: avanço em data futura recusado; chaves de
  agrupamento normalizadas (maiúscula/minúscula contava em dobro); quantidade que
  "desaparecia" por intervalo invertido recuperada em duas camadas — parser e consulta, para
  proteger também o que já estava gravado.
- **Migrations reprodutíveis com portão de CI.** O banco é reconstruído do zero a cada PR e
  conferido objeto a objeto contra a produção (**844 objetos idênticos**) — a fundação de
  deploy foi consertada sem custo de infraestrutura adicional.
- **Assistente de IA** com ferramentas de consulta sobre o modelo de dados, não sobre texto
  livre — a resposta sai do banco, não de suposição.

## Genérico × aplicado

A versão em produção pertence ao contexto corporativo onde nasceu. A versão genérica —
**[Chainage](https://github.com/Holiv/chainage)**, Apache-2.0 — reconstrói o método do zero:
um **modelo canônico** de programa de infraestrutura e um **perfil de mapeamento
declarativo** que traduz a estrutura de cada organização (campos customizados, códigos,
níveis de EAP) para o modelo, sem mudar código. Nenhuma linha de código corporativo
atravessa; o que atravessa é o método, documentado.
