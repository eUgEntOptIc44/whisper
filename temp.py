import whisper

model = whisper.load_model("base")
result = model.transcribe("AU-20220922-0825-1900.mp3") #  tests/jfk.flac
print(result["text"])
