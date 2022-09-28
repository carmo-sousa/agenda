# Agenda

## Implementações futuras

- [ ] Login

## Tabelas

- Tarefas
  - id
  - nm_tarefa
  - descricao
  - inicio
  - fim
  - frequencia
  - hora_alerta
  - status
  - created_at
  - updated_at

- Alertas
  - id
  - dt_inicio
  - dt_fim
  - frequencia
  - created_at
  - updated_at

- Anexo
  - id
  - tarefa_id
  - url
  - created_at
  - updated_at

- Contatos
  - id
  - nome
  - sobrenome
  - created_at
  - updated_at

- Atividades
  - id
  - created_at
  - updated_at

- Status
  - id
  - created_at
  - updated_at

- Telefone
  - id
  - ddd
  - contato_id
  - numero_telefone
  - created_at
  - updated_at

- E-mail
  - id
  - ddd
  - contato_id
  - numero_telefone
  - created_at
  - updated_at

## Rotas

- GET `/atividades`
- GET `/contatos`
- GET `/status`
- GET `/tarefas`

- POST `/atividades`
- POST `/contatos`
- POST `/status`
- POST `/tarefas`
- POST `/usuarios`

- PUT `/atividades/:id`
- PUT `/contatos/:id`
- PUT `/status/:id`
- PUT `/tarefas/:id`
- PUT `/usuarios/:id`

- DELETE `/atividades/:id`
- DELETE `/contatos/:id`
- DELETE `/status/:id`
- DELETE `/tarefas/:id`
- DELETE `/usuarios/:id`
