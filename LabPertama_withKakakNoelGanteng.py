# the secret word
secret_word = 'cute'

# input the secret word
input_user = input("guess the letter! ")

# make sure the input is a word, not a number
if len(input_user) == 1 and input_user.isalpha():
    # ignore lower upper cases
    if input_user.lower() in secret_word.lower():
        print('you did it !!!')
    else:
        print('incorrect ! please try again')
else:
    print('invalid input, only one letter allowed.')

