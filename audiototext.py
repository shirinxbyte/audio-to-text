import whisper

model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
result = model.transcribe("tagsieben.mp3")  # Replace with your file
print(result["text"])

