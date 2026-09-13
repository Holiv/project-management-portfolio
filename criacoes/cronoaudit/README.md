# cronoaudit — auditoria de integridade de cronograma como capacidade instalável

**Agent Skill pública, formato aberto** · [github.com/Holiv/cronoaudit](https://github.com/Holiv/cronoaudit)
· Apache 2.0 · v0.6.0

> A única das cinco criações que **não é de uso interno**: ela sai da empresa e funciona na
> máquina de qualquer pessoa.

## Contexto

As quatro criações anteriores resolvem o controle de um programa específico. Elas dependem do
arquivo, do banco e das convenções daquele contrato — e, por isso, o conhecimento que as
sustenta fica preso a elas.

Havia um conjunto de achados que não dependia de nada disso: **o que dá errado silenciosamente
em controle de cronograma.** Valor agregado apurado contra a linha de base errada; custo que
some da curva; contagem que muda sem o dado mudar; jornada suposta em vez de lida. São defeitos
de método, não de sistema — acontecem em qualquer obra, com qualquer ferramenta.

Nenhuma delas estava disponível em forma utilizável por outra pessoa.

## Proposta

Empacotar esse conhecimento no **formato aberto de Agent Skill**, que é lido por Claude Code,
Codex, Gemini CLI, Cursor, Copilot, VS Code e OpenCode. Instalação por **uma linha de comando**,
sem dependência de fornecedor.

O recorte é deliberado e está declarado na própria skill: **não é "como fazer valor agregado"** —
isso existe em livro. É **o que dá errado sem sintoma, e como verificar.**

## Como funciona

- **Contrato de operação no topo:** quem usa, que trabalhos distintos existem, que entrada cada
  um exige, o que sai, que decisão alimenta — e **o que a skill explicitamente não faz.**
- **Eixo organizador:** a pergunta do *datum* — *todas as parcelas deste cálculo estão medidas
  contra a mesma referência?*
- **Rótulos de procedência viajam com cada afirmação**: medido, inferido ou relatado. A skill
  tem uma seção explicando por que eles existem.
- **Escopo negativo declarado:** não cobre Primavera P6, DCMA 14-point nem análise forense de
  atraso — e diz isso.

## Resultado

- **Publicada com autorização explícita**, após varredura de identidade arquivo a arquivo:
  nenhum nome de empregador, contratada, contrato, quilometragem, pessoa ou valor. Nenhum
  caminho local. O arquivo de validação fica fora do repositório.
- **Instalação provada a partir do GitHub em ambiente limpo**, não só localmente.
- **29 commits com a decisão na mensagem** — inclusive as três correções de rumo de uma
  afirmação técnica e a célula que a especificação de rede omitiu.

**Esse histórico é parte do produto, não subproduto dele.** Um método que documenta os próprios
erros de percurso é auditável de um jeito que um método polido não é: dá para ler **como se
chegou**, e não só onde se chegou.

## Capacidades demonstradas

Empacotamento de conhecimento tácito em artefato reutilizável · formato aberto e independente de
fornecedor · disciplina de procedência aplicada a material público · varredura de identidade
antes da publicação permanente · **e a decisão de publicar o erro junto com o acerto**, que é o
que torna o conjunto verificável.
