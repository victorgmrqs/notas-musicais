NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala

    Returns:
        Um dicionário com a nota das escalas e os graus

    Raises:
        ValueError: Caso a tônica não seja uma nota válida
        KeyError: Caso a escala não exista ou não tenha sido implementada

    Examples:

        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('A', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """

    tonica = tonica.upper()

    try:
        intervalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS.index(tonica)
    except KeyError:
        print('entrou no erro')
        raise KeyError(
            'Essa escala não existe ou não foi implementada. '
            f'Tente uma dessas {list(ESCALAS.keys())}'
        )
    except ValueError:
        raise ValueError(f'Esta nota não existe, tente uma dessas: {NOTAS}')

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}