from typer_cli.helpers import error 
''' Dictation
In order to get playback:
Python's pyttsx3 library must be installed.
On Linux, eSpeak must be installed, on MacOS, AVSpeech, eSpeak or NSSpeechSynthesizer must be installed.
# Options
| Option | Description | Default | Data Type |
| rate | The rate of playback of the dictation | 40 | Int |
| voice | The voice with which the dictation is played back, list out espeak voices with `espeak-ng --voices` | "gmw/en" | String |
'''
def main(target, options):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate',options.get("rate", 40))
        engine.setProperty('voice',options.get("voice", "gmw/en"))
        engine.say(target)
        engine.runAndWait()
        try:
            engine.stop()
        except:
            pass
        del engine
        return 0
    except:
        return 1
