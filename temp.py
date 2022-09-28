from pprint import pprint
import json

import whisper

model = whisper.load_model("small")
result = model.transcribe("AU-20220922-0825-1900.mp3")

with open('whisper-output.json', 'w+', encoding='utf-8') as fh:
    fh.write(json.dumps(result))

print(result['text'])

# TODO: find option to run task 'translate'
# result2 = model.translate("AU-20220922-0825-1900.mp3")
# print(result2)
