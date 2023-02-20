from time import sleep
alfabeto1 = ['a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z']

simbolos1 = ['!','#','|','%','*','@','$','?','&',
            ')','+','(','-','_','"',']','/','[',
            '{','}','^','`','£','¬','ª','¢']

alfabeto2 = ['A','B','C','D','E','F','G','H','I',
             'J','K','L','M','N','O','P','Q','R',
             'S','T','U','V','W','X','Y','Z']

simbolos2 = ['§','¶','₩','Σ','⊄','♁','∾','⍵','⌀',
            'ƒ','ž','¡','¿','»','ß','þ','φ','ƃ',
            'त','₳','ᑔ','ᔒ','८','ᐁ','ᔩ','š']

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

simbolos_num = ['ß', 'ᖵ', 'ᙁ', 'ᛯ', 'ᛞ', 'Þ', 'ᥦ', 'ᥱ', 'ᴞ', '€']

acentos = ['Á', 'á', 'Â', 'â', 'À', 'à', 'Ã', 'ã',
           'É', 'é', 'Ê', 'ê', 'Í', 'í', 'Ó', 'ó',
           'Ô', 'ô', 'Õ', 'õ', 'Ú', 'ú', 'Ç', 'ç' ]

simbolos_acen = ['©', 'ᘦ', 'ᛒ', '∅', '∌', 'ᛙ', '↟', '√',
                 '∱', '≤', '℄', '⊾', '⋊', '⋔', '⍤', '⊿',
                 '⋵', '⌅', '☧', '⟴', '⟟', '⊧', '⥲', '⧴']
print('\n')
print('\033[1;35m─\033[m'*50)
print(f'\033[1m{"C R I P T O G R A F I A":^50}\033[m')
print('\033[1;35m─\033[m'*50)

while True:
    crip = (str(input('\nInsira uma frase para \033[4mCriptografar\033[m: ')))
    print('─'*50)


    print('\033[1;35mCriptografando...\033[m')
    sleep(3)

    print(crip.replace(alfabeto1[0], simbolos1[0])
        .replace(alfabeto1[1], simbolos1[1])
        .replace(alfabeto1[2], simbolos1[2])
        .replace(alfabeto1[3], simbolos1[3])
        .replace(alfabeto1[4], simbolos1[4])
        .replace(alfabeto1[5], simbolos1[5])
        .replace(alfabeto1[6], simbolos1[6])
        .replace(alfabeto1[7], simbolos1[7])
        .replace(alfabeto1[8], simbolos1[8])
        .replace(alfabeto1[9], simbolos1[9])
        .replace(alfabeto1[10], simbolos1[10])
        .replace(alfabeto1[11], simbolos1[11])
        .replace(alfabeto1[12], simbolos1[12])
        .replace(alfabeto1[13], simbolos1[13])
        .replace(alfabeto1[14], simbolos1[14])
        .replace(alfabeto1[15], simbolos1[15])
        .replace(alfabeto1[16], simbolos1[16])
        .replace(alfabeto1[17], simbolos1[17])
        .replace(alfabeto1[18], simbolos1[18])
        .replace(alfabeto1[19], simbolos1[19])
        .replace(alfabeto1[20], simbolos1[20])
        .replace(alfabeto1[21], simbolos1[21])
        .replace(alfabeto1[22], simbolos1[22])
        .replace(alfabeto1[23], simbolos1[23])
        .replace(alfabeto1[24], simbolos1[24])
        .replace(alfabeto1[25], simbolos1[25])
        .replace(alfabeto2[0], simbolos2[0])   
        .replace(alfabeto2[1], simbolos2[1])
        .replace(alfabeto2[2], simbolos2[2])
        .replace(alfabeto2[3], simbolos2[3])
        .replace(alfabeto2[4], simbolos2[4])
        .replace(alfabeto2[5], simbolos2[5])
        .replace(alfabeto2[6], simbolos2[6])
        .replace(alfabeto2[7], simbolos2[7])
        .replace(alfabeto2[8], simbolos2[8])
        .replace(alfabeto2[9], simbolos2[9])
        .replace(alfabeto2[10], simbolos2[10])
        .replace(alfabeto2[11], simbolos2[11])
        .replace(alfabeto2[12], simbolos2[12])
        .replace(alfabeto2[13], simbolos2[13])
        .replace(alfabeto2[14], simbolos2[14])
        .replace(alfabeto2[15], simbolos2[15])
        .replace(alfabeto2[16], simbolos2[16])
        .replace(alfabeto2[17], simbolos2[17])
        .replace(alfabeto2[18], simbolos2[18])
        .replace(alfabeto2[19], simbolos2[19])
        .replace(alfabeto2[20], simbolos2[20])
        .replace(alfabeto2[21], simbolos2[21])
        .replace(alfabeto2[22], simbolos2[22])
        .replace(alfabeto2[23], simbolos2[23])
        .replace(alfabeto2[24], simbolos2[24])
        .replace(alfabeto2[25], simbolos2[25])
        .replace(numeros[0], simbolos_num[0])
        .replace(numeros[1], simbolos_num[1])
        .replace(numeros[2], simbolos_num[2])
        .replace(numeros[3], simbolos_num[3])
        .replace(numeros[4], simbolos_num[4])
        .replace(numeros[5], simbolos_num[5])
        .replace(numeros[6], simbolos_num[6])
        .replace(numeros[7], simbolos_num[7])
        .replace(numeros[8], simbolos_num[8])
        .replace(numeros[9], simbolos_num[9])
        .replace(acentos[0], simbolos_acen[0])   
        .replace(acentos[1], simbolos_acen[1])
        .replace(acentos[2], simbolos_acen[2])
        .replace(acentos[3], simbolos_acen[3])
        .replace(acentos[4], simbolos_acen[4])
        .replace(acentos[5], simbolos_acen[5])
        .replace(acentos[6], simbolos_acen[6])
        .replace(acentos[7], simbolos_acen[7])
        .replace(acentos[8], simbolos_acen[8])
        .replace(acentos[9], simbolos_acen[9])
        .replace(acentos[10], simbolos_acen[10])
        .replace(acentos[11], simbolos_acen[11])
        .replace(acentos[12], simbolos_acen[12])
        .replace(acentos[13], simbolos_acen[13])
        .replace(acentos[14], simbolos_acen[14])
        .replace(acentos[15], simbolos_acen[15])
        .replace(acentos[16], simbolos_acen[16])
        .replace(acentos[17], simbolos_acen[17])
        .replace(acentos[18], simbolos_acen[18])
        .replace(acentos[19], simbolos_acen[19])
        .replace(acentos[20], simbolos_acen[20])
        .replace(acentos[21], simbolos_acen[21])
        .replace(acentos[22], simbolos_acen[22])
        .replace(acentos[23], simbolos_acen[23]))
    print('─'*50)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer criptografar outra frase? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\n\033[1;35m{"APS - 2º Período":^50}\033[m')
print('''LUIZ FELIPE BORGES SIQUEIRA - N9309D1
ÍTALO HENRIQUE GOMES E SILVA - N9259A3
FHILIPE RODRIGUES DANTAS - N040025
RODNEY ROQUE SILVA FRANÇA - N8462A5''')
print(f'\033[1;35m{"UNIP - 29/10/2022":^50}\033[m')