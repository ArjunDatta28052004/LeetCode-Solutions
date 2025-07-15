class Solution:
    def isValid(self, word: str) -> bool:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        num = ['0','1','2','3','4','5','6','7','8','9']
        alphabets = [chr(i) for i in range(97,123)]
        alphabets = alphabets.append(chr(i) for i in range(65,91))
        vowel = set(vowel)
        num = set(num)
        consonent = False
        has_vowels = False
        has_num = False
        if(len(word)>=3):
            
            for i in word:
                if(i.isalpha()):
                    if(i in vowel):
                        has_vowels= True
                    else:
                        consonent = True
                elif(i.isdigit()):
                    continue
                else:
                    return False
            return consonent and has_vowels

        else:
            return False
                




        
