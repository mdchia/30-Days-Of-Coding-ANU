#include <iostream>

// Technically fits the parameters, but there's probs a better way
char firstNotRepeatingCharacter(std::string s) {
    int i;
    char nonRepeat;
    std::string alphabet;
    std::map<char, int> alphabetCounts;
    std::map<char, int> alphabetPos;
    char curr_letter;
    char best_letter;
    int best_pos;
    alphabet="abcdefghijklmnopqrstuvwxyz";
    best_letter='_';
    // just a really high number, should probs be a variable
    best_pos=1000000;
    for(i = 0; i < 26; i++){
        curr_letter=alphabet[i];
        alphabetCounts[curr_letter]=0;
    }
    for(i = 0; i < s.length(); i++){
        alphabetCounts[s[i]]+=1;
        alphabetPos[s[i]]=i;
    }
    for(i = 0; i < 26; i++){
        curr_letter=alphabet[i];
        if(alphabetCounts[curr_letter]>1){
            continue;
        }
        if(alphabetCounts[curr_letter]==0){
            continue;
        }
        else if(alphabetPos[curr_letter]<best_pos){
            best_letter=curr_letter;
            best_pos=alphabetPos[curr_letter];
        }
    }
    return best_letter;
}
