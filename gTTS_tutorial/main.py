from gtts import gTTS


value = ['한놈','두식이','석삼','너구리','너무 아저씨 같은건 아닐까?']

with open("hello.txt","w") as f:
    f.write("문장을 적어서 저장한 뒤에 읽어볼겁니다.\n")
    for i in value:
        f.write("반갑다 {}. \n".format(i))

s=None

with open("hello.txt","r") as f:
    s = f.read()

file = "read_my_file.mp3"
tts = gTTS(s,'ko')
tts.save(file)