# Toca musica com uma função de uma biblioteca
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('agora vc escuta')

#import playsound
#playsound.playsound('ex02.mp3')