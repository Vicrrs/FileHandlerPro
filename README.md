# FileHandlerPro

FileHandlerPro é um projeto Django que utiliza Celery e RabbitMQ para gerenciar o upload e download de arquivos. Este README fornece instruções sobre como configurar e rodar o projeto, além de exemplos de como interagir com o sistema de arquivos via API.

## Configuração

### Pré-Requisitos

- Docker
- Docker Compose

### Instruções de Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Vicrrs/FileHandlerPro.git
   cd filehandlerpro
   ```

2. Construa e inicie os contêineres usando Docker Compose:
   ```bash
   docker-compose up --build
   ```

### Executando Migrações

Após iniciar os contêineres pela primeira vez, é necessário criar as tabelas no banco de dados. Execute as migrações com os seguintes comandos:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

## URLs Disponíveis

- **Upload de Arquivos (Formulário)**: [http://localhost:8100/file/upload-form/](http://localhost:8100/file/upload-form/)
- **Download de Arquivos**: Substitua `{file_id}` pelo ID do arquivo desejado:
  [http://localhost:8100/file/download/{file_id}/](http://localhost:8100/file/download/{file_id}/)

## Testando o Upload de Arquivos com cURL

Você pode testar a funcionalidade de upload de arquivos usando o `curl` para enviar uma requisição POST para a API. Substitua `"caminho_para_seu_arquivo/arquivo.txt"` pelo caminho do arquivo que deseja enviar:

```bash
curl -F "file=@caminho_para_seu_arquivo/arquivo.txt" http://localhost:8100/file/upload-form/ -v
```

## Comandos Docker Úteis

- **Ver Logs do Contêiner**:
  ```bash
  docker-compose logs [nome_do_servico]
  ```
  Substitua `[nome_do_servico]` por `web`, `celery` ou `rabbitmq` para ver os logs específicos.

- **Reiniciar todos os Serviços**:
  ```bash
  docker-compose down
  docker-compose up --build
  ```

- **Executar Comandos Dentro de um Contêiner**:
  Por exemplo, para acessar o shell do Django:
  ```bash
  docker-compose exec web python manage.py shell
  ```

## Problemas Comuns e Soluções

**Problema**: Celery não consegue conectar ao RabbitMQ.
**Solução**: Verifique se o RabbitMQ está rodando e se as portas estão configuradas corretamente. Use `docker-compose ps` para verificar se todos os serviços estão rodando sem erros.
