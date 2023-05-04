import itertools
import re
         
def remover_acentos(palavras_chave):
    palavras_chave_sem_acentos = []
    for palavra in palavras_chave:
        palavra_sem_acentos = re.sub(r'[^\w\s]', '', palavra)
        palavra_sem_acentos = re.sub(r'[ãáàâä]', 'a', palavra_sem_acentos)
        palavra_sem_acentos = re.sub(r'[éêë]', 'e', palavra_sem_acentos)
        palavra_sem_acentos = re.sub(r'[íï]', 'i', palavra_sem_acentos)
        palavra_sem_acentos = re.sub(r'[óôöõ]', 'o', palavra_sem_acentos)
        palavra_sem_acentos = re.sub(r'[úüû]', 'u', palavra_sem_acentos)
        palavra_sem_acentos = re.sub(r'ç', 'c', palavra_sem_acentos)
        palavra_sem_acentos = re.sub(r'\s', '', palavra_sem_acentos)
        palavras_chave_sem_acentos.append(palavra_sem_acentos)
    return palavras_chave_sem_acentos

def permutacoes(palavras_chave):
    permutations = set()
    for perm in itertools.permutations(palavras_chave):
        palavra_permutada = ''.join(perm)
        if palavra_permutada not in palavras_chave:
            permutations.add(palavra_permutada)
    return permutations

def combinacoes(palavras_chave):
    combinations = set()
    for r in range(2, len(palavras_chave)+1):
        for combi in itertools.combinations(palavras_chave, r):
            palavra_combinada = ''.join(combi)
            if palavra_combinada not in palavras_chave:
                combinations.add(palavra_combinada)
    return combinations

def mesclagens(palavras_chave):
    merges = set()
    for r in range(1, len(palavras_chave)+1):
        for merge in itertools.product(palavras_chave, repeat=r):
            palavra_mesclada = ''.join(merge)
            if palavra_mesclada not in palavras_chave:
                merges.add(palavra_mesclada)
    return merges

def insercoes(palavras_chave):
    insertions = set()
    caracteres_especiais = ['@', '!', '$', '%', '&']
    for r in range(1, len(palavras_chave)+1):
        for combi in itertools.combinations(palavras_chave, r):
            for perm in itertools.permutations(combi):
                for i in range(len(perm)+1):
                    for c in caracteres_especiais:
                        palavra_inserida = ''.join(list(perm[:i]) + [c] + list(perm[i:]))
                        if palavra_inserida not in palavras_chave:
                            insertions.add(palavra_inserida)
    return insertions

def main():
    palavras = input("Digite as palavras-chave separadas por vírgulas: ")
    palavras = palavras.split(",")
    palavras_chave_sem_acentos = remover_acentos(palavras)
    
    wordlist = set()
    wordlist |= permutacoes(palavras_chave_sem_acentos)
    wordlist |= combinacoes(palavras_chave_sem_acentos)
    wordlist |= mesclagens(palavras_chave_sem_acentos)
    wordlist |= insercoes(palavras_chave_sem_acentos)

    wordlist = sorted(wordlist, key=len)

    with open('wordlist.txt', 'w') as f:
        for w in wordlist:
            f.write(w + '\n')
            
if __name__ == '__main__':
    main()
