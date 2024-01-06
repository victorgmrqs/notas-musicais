# Aplicação do desafio

# Notas musicais
Notas musicais é um CLI para ajudar na formação de escalas e acordes.

Temos dois comandos disponíveis: `escala` e `acorde`

## Como usar?

### Escalas
Você pode chamar as escalas via linha de comando. Por exemplo:
```bash
poetry run notas-musicais escala


Retornando os graus e as notas correspondentes a essa escala:

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘

```

#### Alteração na escala
O primeiro parâmetro do CLI é a tônica qie deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala de `F#`: 

```bash
poetry run notas-musicais escala F#

Resultando em: 
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘

```


#### Alteração na tonalidade da escala
Você pode alterara a tonalidade da escala também! 
Esse é o segundo parâmetro da linah de comando. Por exemplo, a escala de `D#` menor:


```bash
poetry run notas-musicais escala D# menor

Resultando em: 
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ F#  │ G# │ A# │ B  │ C#  │
└────┴────┴─────┴────┴────┴────┴─────┘


```

## Mais informações sobre o CLI

Para descobrir outras opções, você pode usar a flag `--help`:

```bash
poetry run notas-musicais --help

 Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...                                                                                              
                                                                                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell. [default: None]                     │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or customize the            │
│                                                              installation.                                                                   │
│                                                              [default: None]                                                                 │
│ --help                                                       Show this message and exit.                                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ acorde                                                                                                                                       │
│ escala                                                                                                                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯




```