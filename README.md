# 🔔 AutoSchoolBell

AutoSchoolBell é um sistema de automação de sinal escolar desenvolvido em Python. O projeto realiza a reprodução automática de arquivos de áudio em horários previamente configurados, permitindo que escolas, cursos e instituições de ensino automatizem completamente o acionamento da sirene.

O sistema foi projetado para ser simples, leve, configurável e de fácil implantação em computadores Windows, podendo ser executado como script Python ou como um executável gerado pelo PyInstaller.
Atualmente, o sistema está implementado em uma Escola Estadual, com a administração e suporte em minha responsabilidade.

---

# Funcionalidades

- Reprodução automática de áudios em horários programados.
- Configuração dos horários por meio de arquivo JSON.
- Reprodução de um áudio diferente para cada dia útil da semana.
- Ignora automaticamente sábados e domingos.
- Registro de todas as execuções em arquivo de log.
- Estrutura organizada para facilitar manutenção.
- Compatível com Windows Task Scheduler.
- Compatível com executáveis (.exe).
- Baixo consumo de memória e processamento.

---

# Stack utilizada

Linguagem

- Python 3

Bibliotecas

- pygame-ce (reprodução de áudio)
- schedule (agendamento de tarefas)
- json (configuração do sistema)
- os (manipulação de caminhos)
- sys (compatibilidade entre Python e executável)
- datetime (controle de data e hora)
- time (controle do loop principal)

---

# Estrutura do Projeto

```
AutoSchoolBell/
│
├── audio/
│   ├── musica_seg.mp3
│   ├── musica_ter.mp3
│   ├── musica_quar.mp3
│   ├── musica_quin.mp3
│   └── musica_sexta.mp3
│
├── logs/
│   ├── .gitkeep
│   └── logs.txt
│
├── config.json
├── main.py
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

---

# Como funciona

Ao iniciar, o sistema executa as seguintes etapas:

1. Inicializa o módulo de reprodução de áudio utilizando pygame-ce.
2. Identifica automaticamente o diretório da aplicação.
3. Carrega o arquivo de configuração `config.json`.
4. Agenda todos os horários definidos no arquivo de configuração.
5. Permanece em execução aguardando o próximo horário programado.
6. Quando chega um horário agendado:
   - identifica o dia da semana;
   - seleciona o áudio correspondente;
   - reproduz o arquivo;
   - registra a execução no log.
7. Aos sábados e domingos a execução é ignorada automaticamente.

Todo o funcionamento ocorre de maneira automática após a inicialização do sistema.

---

# Arquivo de Configuração

Toda a configuração da aplicação é realizada através do arquivo `config.json`.

Exemplo:

```json
{
    "horarios": [
        "07:00",
        "07:50",
        "08:40",
        "09:30",
        "10:20"
    ],

    "audios": {
        "segunda": "musica_seg.mp3",
        "terca": "musica_ter.mp3",
        "quarta": "musica_quar.mp3",
        "quinta": "musica_quin.mp3",
        "sexta": "musica_sexta.mp3"
    }
}
```

Os horários podem ser alterados sem necessidade de modificar o código-fonte.

---

# Sistema de Logs

Todas as execuções são registradas automaticamente.

Exemplo:

```
[2026-07-22 07:00:00] | Segunda | Sirene executada com sucesso.
```

Os logs permitem acompanhar o histórico de execuções do sistema.

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/devmartins-tech/AutoSchoolBell.git
```

Acesse a pasta do projeto:

```bash
cd AutoSchoolBell
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Executando o projeto

Execute diretamente pelo Python:

```bash
python main.py
```

Ou gere um executável utilizando o PyInstaller:

```bash
pyinstaller --onefile --noconsole main.py
```

Após gerar o executável, recomenda-se configurá-lo para iniciar automaticamente junto ao Windows utilizando o Agendador de Tarefas.

---

# Requisitos

- Windows 10 ou superior
- Python 3.10 ou superior
- pygame-ce
- schedule

---

# Casos de Uso

- Escolas públicas
- Escolas particulares
- Instituições de ensino
- Cursos profissionalizantes
- Centros de treinamento
- Empresas que utilizam sinalização sonora

---

# Melhorias Futuras

- Interface gráfica para configuração.
- Editor integrado de horários.
- Seleção de áudios pela interface.
- Múltiplos perfis de horários.
- Suporte para diferentes calendários letivos.
- Rotação automática dos arquivos de log.
- Tratamento avançado de exceções.
- Painel de monitoramento das execuções.

---

# Licença

Este projeto está licenciado sob a Licença MIT.

Consulte o arquivo LICENSE para mais informações.

---

# Autor

João Pedro da Silva Martins

Analista de Suporte de TI | Python | SQL | MySQL | Database

GitHub

https://github.com/devmartins-tech