import re

materias = []
_pattern = re.compile('([2-7]{1,5})([MTN])([1-6]{1,5})')

traduz_dias = {
    '2': 'SEG',
    '3': 'TER',
    '4': 'QUA',
    '5': 'QUI',
    '6': 'SEX',
    '7': 'SAB'
}

traduz_periodo = {
    'M': 'Manha',
    'T': 'Tarde',
    'N': 'Noite'
}

traduz_horario = {
    'M': {
        '1': '08:00',
        '2': '09:00',
        '3': '10:00',
        '4': '11:00',
        '5': '12:00'
    },
    'T': {
        '1': '13:00',
        '2': '14:00',
        '3': '15:00',
        '4': '16:00',
        '5': '17:00',
        '6': '18:00'
    },
    'N': {
        '1': '19:00',
        '2': '20:00',
        '3': '21:00',
        '4': '22:00'
    }
}

def valida_horario(horario: str):
    ret = True if _pattern.match(horario.strip()) else False
    return ret

def prepara_input():
    while True:
        try:                
            horario = input('Insira o horário do SIGAA:          ').upper()    
            nome = input('Insira o nome da matéria:           ')
            prioridade = int(input('Insira a prioridade para a matéria: '))
            obj = {
                'horario': horario,
                'materia': nome,
                'prioridade': prioridade
            }
            
            check = False
            if valida_horario(horario):
                materias.append(obj)
                check = True
           
            print('------------------------------------------------------')
            if not check:
                print('Não foi possível colocar a matéria na sua lista')
                print('porque o horário tava errado :c')
            print('Caso cê já tenha terminado a sua listinha,')
            print('Aperta "CTRL" + "D"')
            input('Caso o contrário, aperta "ENTER"')
            print('------------------------------------------------------')
        
        except EOFError:
            print('\n------------------------------------------------------')
            break
        
    materias.sort(key=lambda materia: materia['prioridade'])


def separa_em_grupos(horario: str):
    _match = _pattern.match(horario.strip())
    return _match.group(1), _match.group(2), _match.group(3)

def estrutura_horarios():
    '''Essa função vai precisar da lista de matérias já preenchida'''
    pass

def prepara_planilha():
    '''Essa função vai criar o objeto de planilha e vai deixar ele bonitinho.'''
    pass

def preenche_planilha():
    '''Essa função vai preencher os horários da planilha a partir da lista (que já está ordenada a partir da prioridade)'''
    pass

def salva_planilha():
    '''Essa função vai ser responsável por persistir a planilha'''
    pass

def tchau_tchaau():
    print('\nSua planilha já tá ficando prontinha :3')

def final_ruim():
    print('\n EU SOU UMA PIADA PRA VOCÊ?!??')

def gateway():
    prepara_input()
    if len(materias) >= 1:
        estrutura_horarios()
        prepara_planilha()
        preenche_planilha()
        salva_planilha()
        tchau_tchaau()
    else:
        final_ruim()


if __name__ == '__main__':
    gateway()