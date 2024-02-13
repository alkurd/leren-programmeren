from test_lib import test, report
def get_value(date:str, separator:str, position:int)->str:
  
  value = date.split(separator)
  if 0 <= position< len(value):
        return   value [position] # read value at position of split_values
  else:
        
        return  None
data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','
    # Test 1: Positieve index
position = 8
expected_result = "Bram:6"
result = get_value(data, separator, position)
test("Test 1", expected_result, result)
    # Test 2: Negatieve index (buiten bereik)
position = -3
expected_result = None
result = get_value(data, separator, position)
test("Test 2", expected_result, result)
    # Voeg hier meer testgevallen toe zoals bovenstaand voorbeeld...
# Voer de test uit

report()


import re
from test_lib import test, report
# replace alle separators "." , ",", " en ", "omdat ", "zodat ", "want ", " wanneer " en "dat ”by a marker "|"
def word_splitter(text:str)->list:
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|") # split de text on marker "|"
    return sub_sentences


def splits_counter(sub_sentences):
    ego_score = 0
    for sentence in sub_sentences:
        # if not isinstance(sentence, str):
        #     continue
        sentence = sentence.strip()
        sentence = sentence.lower()
        if len (sentence) > 0:
            words = sentence.split(' ')
            if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
                ego_score += 1
    return ego_score


text= '''Geachte heer/mevrouw,Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat  voor deze functie omdat ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren. Ik ben buitengewoon slim en in staat om snel nieuwe  informatie te verwerken en te gebruiken om de beste beslissingen te nemen voor het bedrijf. Ik ben er zeker van dat ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf, en ik zal in staat zijn om snel resultaten te boeken en uw bedrijf naar de top te brengen. Mijn CV is overtuigend! Mijn referenties zijn heel positief over mij. Ik verdien daarom een plek in uw team.Ik kijk er naar uit om te horen wanneer ik op gesprek mag komen, zodat ik u persoonlijk kan overtuigen  van mijn geschiktheid voor deze functie.'''

    # Testen van de text_splitser functie
text = word_splitter(text)
expacted_resultaat =['Geachte heer/mevrouw', 'Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf', ' Ik ben de beste kandidaat  voor deze functie ', 'ik al jaren ervaring heb in deze branche', 'ik weet ', 'niemand anders mijn niveau van kennis', 'vaardigheden kan evenaren', ' Ik ben buitengewoon slim', 'in staat om snel nieuwe  informatie te verwerken', 'te gebruiken om de beste beslissingen te nemen voor het bedrijf', ' Ik ben er zeker van ', 'ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf', '', 'ik zal in staat zijn om snel resultaten te boeken', 'uw bedrijf naar de top te brengen', ' Mijn CV is overtuigend', ' Mijn referenties zijn heel positief over mij', ' Ik verdien daarom een plek in uw team', 'Ik kijk er naar uit om te horen ', 'ik op gesprek mag komen', ' ', 'ik u persoonlijk kan overtuigen  van mijn geschiktheid voor deze functie', '']
# print (text)
test("Test of text_splitser",expacted_resultaat ,text )

    # Testen van de count_ego_words_in_sentences functie
aantal_ego_zinnen = splits_counter(text)
test("Test of count_ego_words_in_sentences", splits_counter(text), aantal_ego_zinnen)

    # Rapporteer de resultaten
report()
   

import math

# ['Geachte heer/mevrouw', 'Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf', ' Ik ben de beste kandidaat  voor deze functie ', 'ik al jaren ervaring heb in deze branche', 'ik weet ', 'niemand anders mijn niveau van kennis', 'vaardigheden kan evenaren', ' Ik ben buitengewoon slim', 'in staat om snel nieuwe  informatie te verwerken', 'te gebruiken om de beste beslissingen te nemen voor het bedrijf', ' Ik ben er zeker van ', 'ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf', '', 'ik zal in staat zijn om snel resultaten te boeken', 'uw bedrijf naar de top te brengen', ' Mijn CV is overtuigend', ' Mijn referenties zijn heel positief over mij', ' Ik verdien daarom een plek in uw team', 'Ik kijk er naar uit om te horen ', 'ik op gesprek mag komen', ' ', 'ik u persoonlijk kan overtuigen  van mijn geschiktheid voor deze functie', '']
returned = print(round(12.56,1) + int(13.9))

