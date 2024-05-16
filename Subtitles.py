import os
import math
from faster_whisper import WhisperModel
from moviepy.editor import VideoFileClip
from googletrans import Translator
from httpcore import ReadTimeout

# Define input and output folders
input_folder = "input_folder"
output_folder = "output"

english_subtitles_folder = os.path.join(output_folder, "english_subtitles")
hindi_subtitles_folder = os.path.join(output_folder, "hindi_subtitles")

# Create output folders if they don't exist
os.makedirs(english_subtitles_folder, exist_ok=True)
os.makedirs(hindi_subtitles_folder, exist_ok=True)


def extract_audio(video_file):
    input_video_name = os.path.splitext(os.path.basename(video_file))[0]
    audio_file = os.path.join(output_folder, f"{input_video_name}.wav")
    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file, codec='pcm_s16le', fps=44100)
    video_clip.close()
    return audio_file


def transcribe(audio):
    model = WhisperModel("small")
    segments, info = model.transcribe(audio)
    language = info[0]
    print("Transcription language:", info[0])
    segments = list(segments)
    return language, segments


def format_time(seconds):
    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
    return formatted_time


def translate_to_hindi(text):
    translator = Translator()
    try:
        translated_text = translator.translate(text, src='en', dest='hi')
        return translated_text.text
    except ReadTimeout:
        print("Translation request timed out. Retrying...")
        return translate_to_hindi(text)


def generate_subtitle_file(subtitles, language_code, video_name):
    subtitle_file = f"{video_name}_{language_code}_subtitles.srt"
    text = ""
    for index, subtitle in enumerate(subtitles):
        segment_start = format_time(subtitle.start)
        segment_end = format_time(subtitle.end)
        translated_text = translate_to_hindi(subtitle.text) if language_code == 'hi' else subtitle.text
        text += f"{str(index + 1)}\n"
        text += f"{segment_start} --> {segment_end}\n"
        text += f"{translated_text}\n"
        text += "\n"

    with open(subtitle_file, "w", encoding='utf-8') as f:
        f.write(text)
    return subtitle_file


def process_video(video_file):
    extracted_audio = extract_audio(video_file)
    language, segments = transcribe(audio=extracted_audio)

    video_name = os.path.splitext(os.path.basename(video_file))[0]

    # Generate English subtitle file
    english_subtitle_file = generate_subtitle_file(segments, 'en', video_name)
    print(f"English SRT file generated: {english_subtitle_file}")

    # Generate Hindi subtitle file
    hindi_subtitle_file = generate_subtitle_file(segments, 'hi', video_name)
    print(f"Hindi SRT file generated: {hindi_subtitle_file}")

    return english_subtitle_file, hindi_subtitle_file


def process_videos_in_folder(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".mp4"):
            video_file = os.path.join(folder, filename)
            english_subtitle_file, hindi_subtitle_file = process_video(video_file)

            # Move generated subtitle files to respective output folders
            os.rename(english_subtitle_file,
                      os.path.join(english_subtitles_folder, os.path.basename(english_subtitle_file)))
            os.rename(hindi_subtitle_file, os.path.join(hindi_subtitles_folder, os.path.basename(hindi_subtitle_file)))
            print("Subtitle files moved to output folders.")


# Process videos in the input folder
process_videos_in_folder(input_folder)
