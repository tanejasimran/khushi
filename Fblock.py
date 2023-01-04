from gtts import gTTS
import os
myText="The f-block consists of elements in which 4 f and 5 f orbitals are progressively filled. They are placed in a separate panel at the bottom of the periodic table. The names transition metals and inner transition metals are often used to refer to the elements of d-and f-blocks respectively."
language='en'
output=gTTS(text=myText,lang=language)
output.save('Fblock.mp3')
os.system('start Fblock.mp3')