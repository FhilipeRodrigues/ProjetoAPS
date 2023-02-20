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
print('\033[1;32m─\033[m'*50)
print(f'\033[1m{"D E S C R I P T O G R A F I A":^50}\033[m')
print('\033[1;32m─\033[m'*50)
while True:
    
    crip = (str(input('\nInsira uma frase para \033[4mDescriptografar\033[m: ')))
    print('─'*50)


    print('\033[1;32mDescriptografando...\033[m')
    sleep(3)

    print(crip.replace(simbolos1[0], alfabeto1[0])
        .replace(simbolos1[1], alfabeto1[1])
        .replace(simbolos1[2], alfabeto1[2])
        .replace(simbolos1[3], alfabeto1[3])
        .replace(simbolos1[4], alfabeto1[4])
        .replace(simbolos1[5], alfabeto1[5])
        .replace(simbolos1[6], alfabeto1[6])
        .replace(simbolos1[7], alfabeto1[7])
        .replace(simbolos1[8], alfabeto1[8])
        .replace(simbolos1[9], alfabeto1[9])
        .replace(simbolos1[10], alfabeto1[10])
        .replace(simbolos1[11], alfabeto1[11])
        .replace(simbolos1[12], alfabeto1[12])
        .replace(simbolos1[13], alfabeto1[13])
        .replace(simbolos1[14], alfabeto1[14])
        .replace(simbolos1[15], alfabeto1[15])
        .replace(simbolos1[16], alfabeto1[16])
        .replace(simbolos1[17], alfabeto1[17])
        .replace(simbolos1[18], alfabeto1[18])
        .replace(simbolos1[19], alfabeto1[19])
        .replace(simbolos1[20], alfabeto1[20])
        .replace(simbolos1[21], alfabeto1[21])
        .replace(simbolos1[22], alfabeto1[22])
        .replace(simbolos1[23], alfabeto1[23])
        .replace(simbolos1[24], alfabeto1[24])
        .replace(simbolos1[25], alfabeto1[25])
        .replace(simbolos2[0], alfabeto2[0])
        .replace(simbolos2[1], alfabeto2[1])
        .replace(simbolos2[2], alfabeto2[2])
        .replace(simbolos2[3], alfabeto2[3])
        .replace(simbolos2[4], alfabeto2[4])
        .replace(simbolos2[5], alfabeto2[5])
        .replace(simbolos2[6], alfabeto2[6])
        .replace(simbolos2[7], alfabeto2[7])
        .replace(simbolos2[8], alfabeto2[8])
        .replace(simbolos2[9], alfabeto2[9])
        .replace(simbolos2[10], alfabeto2[10])
        .replace(simbolos2[11], alfabeto2[11])
        .replace(simbolos2[12], alfabeto2[12])
        .replace(simbolos2[13], alfabeto2[13])
        .replace(simbolos2[14], alfabeto2[14])
        .replace(simbolos2[15], alfabeto2[15])
        .replace(simbolos2[16], alfabeto2[16])
        .replace(simbolos2[17], alfabeto2[17])
        .replace(simbolos2[18], alfabeto2[18])
        .replace(simbolos2[19], alfabeto2[19])
        .replace(simbolos2[20], alfabeto2[20])
        .replace(simbolos2[21], alfabeto2[21])
        .replace(simbolos2[22], alfabeto2[22])
        .replace(simbolos2[23], alfabeto2[23])
        .replace(simbolos2[24], alfabeto2[24])
        .replace(simbolos2[25], alfabeto2[25])
        .replace(simbolos_num[0], numeros[0])
        .replace(simbolos_num[1], numeros[1])
        .replace(simbolos_num[2], numeros[2])
        .replace(simbolos_num[3], numeros[3])
        .replace(simbolos_num[4], numeros[4])
        .replace(simbolos_num[5], numeros[5])
        .replace(simbolos_num[6], numeros[6])
        .replace(simbolos_num[7], numeros[7])
        .replace(simbolos_num[8], numeros[8])
        .replace(simbolos_num[9], numeros[9])
        .replace(simbolos_acen[0], acentos[0])
        .replace(simbolos_acen[1], acentos[1])
        .replace(simbolos_acen[2], acentos[2])
        .replace(simbolos_acen[3], acentos[3])
        .replace(simbolos_acen[4], acentos[4])
        .replace(simbolos_acen[5], acentos[5])
        .replace(simbolos_acen[6], acentos[6])
        .replace(simbolos_acen[7], acentos[7])
        .replace(simbolos_acen[8], acentos[8])
        .replace(simbolos_acen[9], acentos[9])
        .replace(simbolos_acen[10], acentos[10])
        .replace(simbolos_acen[11], acentos[11])
        .replace(simbolos_acen[12], acentos[12])
        .replace(simbolos_acen[13], acentos[13])
        .replace(simbolos_acen[14], acentos[14])
        .replace(simbolos_acen[15], acentos[15])
        .replace(simbolos_acen[16], acentos[16])
        .replace(simbolos_acen[17], acentos[17])
        .replace(simbolos_acen[18], acentos[18])
        .replace(simbolos_acen[19], acentos[19])
        .replace(simbolos_acen[20], acentos[20])
        .replace(simbolos_acen[21], acentos[21])
        .replace(simbolos_acen[22], acentos[22])
        .replace(simbolos_acen[23], acentos[23]))
    print('─'*50)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer descriptografar novamente? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\n\033[1;32m{"APS - 2º Período":^50}\033[m')
print('''LUIZ FELIPE BORGES SIQUEIRA - N9309D1
ÍTALO HENRIQUE GOMES E SILVA - N9259A3
FHILIPE RODRIGUES DANTAS - N040025
RODNEY ROQUE SILVA FRANÇA - N8462A5''')
print(f'\033[1;32m{"UNIP - 29/10/2022":^50}\033[m')