from gtts import gTTS
import os
myText = " The elements of Group 1 and Group 2 of the modern periodic table are called S-block elements Two types of s block elements are possible i.e. the elements with one electron (s1) or the elements with two electrons (s2) in their s-subshell.S-block comprises 14 elements namely hydrogen (H), lithium (Li), helium (He), sodium (Na), beryllium (Be), potassium (K), magnesium (Mg), rubidium (Rb), calcium (Ca), cesium (Cs), strontium (Sr), francium (Fr), barium (Ba), and radium (Ra)."
language='en'
output=gTTS(text=myText,lang=language)
output.save('Sblock.mp3')
os.system('start Sblock.mp3')
