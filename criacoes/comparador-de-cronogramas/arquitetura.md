# Arquitetura — comparador de cronogramas

## Estrutura

Motor em módulos VBA desacoplados — extração, comparação, relatório — comunicando-se por
estruturas de dicionário, mais módulos de template que acompanham cada relatório gerado.
Interface em dois modos: standalone do Excel ou suplemento dentro do MS Project.

## Decisões que valem registro

- **Snapshot-diff, não estado acumulado.** O comparador não mantém banco: compara dois
  arquivos e embute o resultado — incluindo a série histórica — no próprio relatório. O
  relatório N é a fonte do relatório N+1. Persistência sem infraestrutura, auditável por
  qualquer pessoa com o arquivo.
- **Instância COM única do Project.** O MS Project não abre duas instâncias independentes
  como o Excel; o modo suplemento existe para receber a instância viva e abrir apenas o
  arquivo anterior — o tratamento desse comportamento está documentado no próprio código.
- **Template que empresta módulos.** O relatório gerado é um artefato autônomo (.xlsm):
  carrega os próprios botões e funções. Quem recebe não precisa do motor instalado.
- **Âncora de marcos por convenção de campo** — a estrutura de marcos é detectada a partir
  do preenchimento de um campo corporativo; na versão genérica, isso vira configuração
  declarada (o mesmo princípio do perfil de mapeamento do
  [Chainage](https://github.com/Holiv/chainage)).

## Genérico × aplicado

A versão em uso carrega convenções da organização (mapeamento posicional de campos
customizados, campo corporativo de entrega, módulo de envio à API interna). O corte para a
versão genérica está identificado: mapeamento de campos extraído para configuração, módulo
de API parametrizado, credenciais fora do código. A arquitetura — snapshot-diff, histórico
embutido, relatório autônomo — é integralmente transferível.
