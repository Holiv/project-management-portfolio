# Sistema de gestão de equipe e competências

**Aplicação web em uso pela equipe de planejamento** · projeto pessoal (repositório privado)
· será absorvido como módulo de equipe da plataforma [Chainage](https://github.com/Holiv/chainage)

## Contexto

Gestão de equipe técnica costuma viver em planilhas dispersas: quem domina o quê, metas de
desenvolvimento, matriz de responsabilidades, registros de 1:1. Sem estrutura, a informação
não se acumula — e perguntas como "a equipe está evoluindo nas competências que o trabalho
exige?" ficam sem resposta objetiva.

## Proposta

Um sistema único com seis módulos — pessoas, competências, metas, RACI, acompanhamento,
painel — desenhado desde o início para **medir**, não só registrar: cada dado nasce com
escala definida, visibilidade deliberada e captura mensal para série histórica.

## Como funciona

- **Competências em escala de aquisição de habilidade (Dreyfus, 1–5)**, com a régua
  documentada em manual — incluindo perguntas de desempate entre níveis vizinhos — e
  **imposta no banco de dados** (tipo numérico com restrição), não apenas na tela: seis
  pessoas medindo com a mesma régua produzem números comparáveis.
- **Visibilidade desenhada por tipo de dado**: metas descem em cascata hierárquica (servem
  para o nível acima ajudar); competências não — são visíveis apenas ao dono e à
  administração, porque expõem fraqueza pessoal e exigem confiança. **A regra de acesso
  protege a honestidade do registro** — quem se sente vigiado subnotifica, e o dado enviesa.
- **Registro de retrabalho** com definição operacional única ("a entrega já tinha sido dada
  como pronta?") e **exportação mensal em CSV** — a fotografia da equipe, com carimbo de
  data em cada linha.
- **Consentimento informado desde o primeiro registro**: a equipe sabe o que é registrado,
  com que frequência, quem vê, e o possível uso em pesquisa acadêmica pseudonimizada.
- Manual do usuário completo (PDF, 20 páginas) entregue antes do primeiro cadastro.

## Resultado

- Uma equipe real operando com **régua de competência comparável e trilha de
  desenvolvimento individual** — em vez de avaliação por impressão.
- **Série longitudinal mensal** de competência, cadência de acompanhamento e retrabalho —
  base de dados que quase nenhuma equipe de planejamento possui, coletada com consentimento
  e desenho de medição desde a origem.
- *Em consolidação: primeira fotografia mensal da série (set/2026).*

## Capacidades demonstradas

Desenho de instrumento de medição (escala, régua, trava de integridade) · segurança por
linha (RLS) com visibilidade diferenciada por natureza do dado · ética de dados aplicada
(consentimento, pseudonimização) · gestão de pessoas instrumentada — a ponte entre liderança
de equipe e engenharia de dados.
