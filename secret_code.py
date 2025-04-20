# 🎮 Palavra Secreta com Vidas / Secret Word with Lives
# Autor / Author: RomuloCifer
# Um jogo de adivinhação onde o jogador tenta descobrir a palavra secreta antes que as vidas acabem.
# A guessing game where the player tries to discover the secret word before the lives run out.

secret_code = 'Secret Santa'.lower()  # Palavra ou frase secreta / Secret word or phrase
attempts = 0  # Número de tentativas permitidas / Number of allowed attempts / will ask the diffulty for the user.
checked_letters = ''  # Letras já acertadas / Letters the player has already guessed
final_word = ''  # Palavra que mostra o progresso / Word that shows player's progress

print('🎉 Bem-vindo ao jogo: PALAVRA SECRETA COM VIDAS 🎉')
print('🎉 Welcome to the game: SECRET WORD WITH LIVES 🎉')
print('Dica / Hint: A palavra tem', len(secret_code)) 
if ' ' in secret_code:
    print('letras (incluindo espaços) / letters (including spaces)')
else:
    print('letras (não incluindo espaços) / not including spaces')
print('-' * 40)
level_user = input('Choose the difficulty: \n /' \
 'Hard:5 attempts / tentativas   \n /' \
 ' Medium: 7 attempts / tentativas \n /' \
 ' Easy: 10 attempts / tentativas \n') 

level_check = False
while level_check == False:
    level_user = level_user.lower().strip()
    if level_user == 'h' or level_user == 'hard':
        attempts = 5
        level_check = True
    elif level_user == 'm' or level_user == 'medium':
        attempts = 7
        level_check = True
    elif level_user == 'e' or level_user == 'easy':
        attempts = 10
        level_check = True
    else:
        print('⚠️ Digite uma dificuldade válida (H)ARD / (M)EDIUM / (E)ASY')
        level_user = input('Choose difficulty again: ')
    
print(f'You have {attempts} attempts, Good Luck! / Boa sorte!')
while attempts > 0:
    final_word = ''    
    user_guess = input('🔤 Tente uma letra / Try a letter: ').lower()

    # Verifica se o jogador digitou mais de uma letra
    # Checks if the player typed more than one letter
    if len(user_guess) != 1:
        print('⚠️ Por favor, digite apenas UMA letra. / Please type only ONE letter.')
        continue

    # Verifica se a letra já foi usada
    # Checks if the letter was already guessed
    if user_guess in checked_letters:
        print('🔁 Você já tentou essa letra. / You already tried this letter.')
        continue

    # Verifica se a letra está correta
    # Checks if the guessed letter is in the secret word
    if user_guess in secret_code.lower():
        print('✅ Boa! Essa letra está na palavra. / Nice! That letter is in the word.')
        checked_letters += user_guess
    else:
        attempts -= 1
        print(f'❌ Letra errada! Você ainda tem {attempts} tentativa(s). / Wrong letter! You still have {attempts} attempt(s).')

    # Monta a palavra revelando apenas letras corretas
    # Builds the word showing only correct letters
    for letter in secret_code:
        if letter in checked_letters or letter == ' ':
            final_word += letter
        else:
            final_word += '*'

    print('\n🔎 Palavra / Word:', final_word)
    print('-' * 40)

    # Verifica se o jogador ganhou
    # Checks if the player has won
    if final_word == secret_code:
        print('🎊 Parabéns! Você descobriu a palavra secreta! / Congrats! You discovered the secret word!')
        break
else:
    print('😢 Fim de jogo! Suas tentativas acabaram. / Game over! You ran out of attempts.')
    print('A palavra secreta era / The secret word was:', secret_code)