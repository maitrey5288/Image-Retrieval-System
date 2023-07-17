# from spellchecker import SpellChecker

# spell = SpellChecker()  # loads default word frequency list
# spell.word_frequency.load_text_file('./my_free_text_doc.txt')

# if I just want to make sure some words are not flagged as misspelled
# spell.word_frequency.load_words(['microsoft', 'apple', 'google'])
# spell.known(['microsoft', 'google'])  # will return both now!

from spellchecker import SpellChecker

spell = SpellChecker()
# spell.word_frequency.load_words(['microsoft', 'apple', 'google'])

# find those words that may be misspelled
def load():
    spell.word_frequency.load_text_file('./data/dictonary.txt')

def correct(text):
    load()
    print("hi this is textxxtt",text)
    corrected_text ={"correct" : " " ,
                     "notindictonary" :[]}
    l= []
    for word in text.split():
        if(spell.correction(word) ==None ):
            corrected_text['notindictonary'].append(word)
        else:

           l.append((spell.correction(word)))
            # corrected_text['correct']+=' '  
    # print(hi",l)
      
    corrected_text['correct'] = " ".join(l)



    return corrected_text
# print(correct('youtube'))
# print(correct('netflix'))
# print(correct('instagam'))
# print(correct('maitrey'))
print(correct('vishwakarma'))


    # Get a list of `likely` options
    # print(spell.candidates(word))
