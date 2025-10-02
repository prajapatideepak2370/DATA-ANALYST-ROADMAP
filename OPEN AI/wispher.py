import whisper
model = whisper.load_model("small")
result = model.transcribe(r"OPEN AI\audio.mp3.mp3")

print(result["text"])