from gtts import gTTS
import os
myText="D block elements are the elements that can be found from the third group to the twelfth group of the modern periodic table. The valence electrons of these elements fall under the d orbital. D block elements are also referred to as transition elements or transition metals."
language='en'
output=gTTS(text=myText,lang=language)
output.save('Dblock.mp3')
os.system('start Dblock.mp3')