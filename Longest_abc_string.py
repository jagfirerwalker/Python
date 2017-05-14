s = "aaagdfajfaslfajsdofiwev"

longest_abc_string = ''
letter_place_holder = ''


for char in s:
    if (letter_place_holder == ''):
        letter_place_holder = char
    elif (letter_place_holder[-1] <= char):
        letter_place_holder += char
    elif (letter_place_holder[-1] > char):
        if (len(longest_abc_string) < len(letter_place_holder)):
            longest_abc_string = letter_place_holder
            letter_place_holder = char
        else:
            letter_place_holder = char
if (len(letter_place_holder) > len(longest_abc_string)):
    longest_abc_string = letter_place_holder
print(longest_abc_string)