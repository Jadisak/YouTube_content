from gtts import gTTS
txt = 'Like and SUBSCRIBE'
speech = gTTS(text = txt, lang = 'en', slow = False, tld = 'com.au')
speech.save('/storage/emulated/0/Python_for_shorts/TexttoAudio/speech.mp3')