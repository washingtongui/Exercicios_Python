from pygame import mixer
print('Rap dos Hokages (Naruto) - A VONTADE DO FOGO | NERD HITS')
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
while mixer.music.get_busy():
    pass