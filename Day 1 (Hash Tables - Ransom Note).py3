def ransom_note(magazine, ransom):
    note_words={}
    mag_words={}
    for note_word in ransom: # Total up counts of unique words
        if note_word in note_words:
            note_words[note_word]+=1
        else:
            note_words[note_word]=1
    for mag_word in magazine:
        if mag_word in mag_words:
            mag_words[mag_word]+=1
        else:
            mag_words[mag_word]=1
    for note_word in note_words:
        if not note_word in mag_words:
            return False # If there's a word in ransom that isn't in magazine
        if note_words[note_word]>mag_words[note_word]:
            return False # If there's more of a word in ransom than in magazine
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
