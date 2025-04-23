# Organizagora - Organizador de Downloads em Python

Quem nunca perdeu alguns minutos procurando por um arquivo na pasta Downloads — aquela que vira uma verdadeira bagunça com o tempo? Arquivos acumulam, nomes se misturam, e encontrar algo específico pode virar um desafio.

Esse projeto visou exatamente solucionar isso, trata-se de um script em Python que organiza automaticamente os arquivos das suas pastas, inicialmente idealizado para a pastas **Downloads**, que como sabemos costuma ficar um caos, em subpastas baseadas no tipo de arquivo (vídeos, imagens, documentos etc.), adaptável para qualquer outra pasta. Também monitora a pasta em tempo real para mover novos arquivos conforme são criados.

![Funcionamento do Organizagora](funcionamento.gif)

## 🛠️ Funcionalidades

- Organização inicial de todos os arquivos já existentes na pasta.
- Monitoramento em tempo real de novos arquivos usando `watchdog`.
- Classificação de arquivos por extensão, com um dicionário modular de categorias (`categorias.py`).
- Tratamento de conflitos de nomes: adiciona sufixo numérico ao detectar arquivos com mesmo nome.
- Logs detalhados de operações, registrados em arquivo `organizador_log.txt`.

## 📁 Estrutura do Projeto

```
meu_organizador/
├── categorias.py        # Dicionário de categorias e extensões
├── organizador.py       # Script principal que organiza e monitora
├── organizador_log.txt  # Arquivo de logs gerado em tempo de execução
└── README.md            # Este arquivo
```

## 🚀 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/arthurantonello/organizagora.git
   cd organizagora
   ```
2. Crie um ambiente virtual (recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install watchdog
   ```

## ⚙️ Uso

1. Abra o arquivo `categorias.py` e ajuste as extensões conforme sua necessidade.
2. No `organizador.py`, ajuste a variável `pasta` para a pasta que deseja monitorar (por padrão, usa `~/Downloads`).
3. Execute o script:
   ```bash
   python organizador.py
   ```

O script fará a organização inicial dos arquivos existentes e, em seguida, ficará em execução monitorando novos arquivos.

## 📋 Configuração de Categorias

Edite o arquivo `categorias.py` para adicionar ou remover extensões da sua escolha:

```python
CATEGORIAS = {
    'Vídeos': ['mp4', 'avi', 'mkv', ...],
    'Imagens': ['jpg', 'png', 'gif', ...],
    'Documentos': ['pdf', 'docx', 'txt', ...],
    # ... outras categorias ...
    'Outros': []
}
```

Para usar o dicionário direto no script, um mapeamento de extensão para categoria é gerado automaticamente:

```python
ext2cat = {ext: cat for cat, exts in CATEGORIAS.items() for ext in exts}
```

## 📦 Gerando Executável (Opcional)

Se preferir um executável no Windows sem console:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile organizador.py
```

Coloque o executável gerado na inicialização do sistema para rodar automaticamente ao ligar.

Pressione Win + R e procure por shell:startup

## 📝 Logs

Todas as operações são registradas em `organizador_log.txt` no mesmo diretório do script. O log inclui timestamps, tipo de mensagem (INFO, SUCESSO, ERRO, ALERTA) e detalhes das ações.

## 🤝 Contribuição
### Adoraria que, caso tenha ideias de como melhorar, que participe desse projeto!

1. Fork este repositório.
2. Crie uma branch para sua feature ou correção: `git checkout -b feature/nova-categoria`.
3. Faça commit das alterações: `git commit -m "Adiciona nova categoria X"`.
4. Envie para o repositório remoto: `git push origin feature/nova-categoria`.
5. Abra um Pull Request.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

