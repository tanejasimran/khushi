from gtts import gTTS
import os
myText="there are six groups of p–block elements in the periodic table numbering from 13 to 18. Boron, carbon, nitrogen, oxygen, fluorine and helium head the groups. Their valence shell electronic configuration is ns2np1-6(except for He)"
language='en'
output=gTTS(text=myText,lang=language)
output.save('Pblock.mp3')
os.system('start Pblock.mp3')