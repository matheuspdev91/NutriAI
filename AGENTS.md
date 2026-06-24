# Nutrix

Sistema para nutricionistas.

Fluxo principal:

Paciente
→ Anamnese
→ Avaliação Nutricional
→ Plano Alimentar
→ PDF

## Modo de trabalho obrigatório

Antes de qualquer alteração:

1. Analisar o problema.
2. Criar um plano.
3. Listar os arquivos que serão alterados.
4. Explicar os impactos.
5. Aguardar aprovação.

## Regras

* Fazer alterações mínimas.
* Não refatorar código não relacionado.
* Não alterar models sem justificativa.
* Não alterar migrations sem aprovação.
* Não remover funcionalidades existentes sem autorização.
* Preservar URLs existentes sempre que possível.

## Django

* Seguir boas práticas Django.
* Verificar templates, views, urls e models afetados.
* Priorizar simplicidade.
* Evitar dependências desnecessárias.

## Templates

Ao alterar templates:

* Verificar {% extends %}
* Verificar {% include %}
* Verificar {% static %}
* Evitar duplicação de HTML
* Preservar responsividade existente

## Git

Antes de alterações grandes:

* Recomendar commit de segurança.
* Informar arquivos que serão modificados.

## Resposta esperada

Sempre responder neste formato:

### Problema

(descrição)

### Plano

(passos)

### Arquivos

* arquivo 1
* arquivo 2

### Riscos

(possíveis impactos)

### Aguardando aprovação


## Segurança

- Nunca apagar arquivos sem aprovação explícita.
- Nunca executar comandos destrutivos automaticamente.
- Nunca sobrescrever templates completos quando uma alteração parcial resolver o problema.