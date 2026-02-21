import os
from elevenlabs.client import ElevenLabs
import elevenlabs

ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )

    elevenlabs.save(audio, output_filepath)
