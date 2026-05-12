import os
import re

def parse_dialog_script(script_text):
    """
    Parses a screenplay dialog script.
    Looks for Female indicator 'F:' or standard character dialogue.
    Locks in high-quality female and male voice profiles.
    """
    lines = script_text.split('\n')
    dialog_track = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("F:"):
            # Female Dialogue -> Lock Chinese Female voice profile seed_313
            dialog_track.append({
                "voice": "seed_313",
                "text": line[2:].strip(),
                "language": "zh"
            })
        elif line.startswith("M:"):
            # Male Dialogue -> Lock Chinese Male voice profile seed_2222
            dialog_track.append({
                "voice": "seed_2222",
                "text": line[2:].strip(),
                "language": "zh"
            })
        else:
            # Standard English Dialogue -> Kokoro-v0 (High-Speed Engine)
            dialog_track.append({
                "voice": "kokoro_v0",
                "text": line,
                "language": "en"
            })
            
    return dialog_track

def generate_srt_timestamps(dialog_track, words_per_minute=130):
    """
    Generates standard SRT timestamp subtitle sequences based on text length.
    """
    srt_output = []
    current_time_ms = 0
    
    for index, item in enumerate(dialog_track):
        text = item["text"]
        word_count = len(text.split()) if item["language"] == "en" else len(text)
        duration_ms = max(1500, int((word_count / words_per_minute) * 60 * 1000))
        
        start_ms = current_time_ms
        end_ms = current_time_ms + duration_ms
        current_time_ms = end_ms + 200 # Add brief pause
        
        start_str = format_srt_time(start_ms)
        end_str = format_srt_time(end_ms)
        
        srt_output.append(f"{index + 1}\n{start_str} --> {end_str}\n{text}\n")
        
    return "\n".join(srt_output)

def format_srt_time(ms):
    """Helper to convert milliseconds to standard SRT format HH:MM:SS,mmm"""
    hours = ms // 3600000
    minutes = (ms % 3600000) // 60000
    seconds = (ms % 60000) // 1000
    milliseconds = ms % 1000
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

if __name__ == "__main__":
    sample_script = """
    F: 这一切都是你计划好的，对吗？
    M: 我别无选择。为了家族的生存，我只能这么做。
    This is the ultimate confrontation of our destiny.
    """
    print("Parsing Drama Dialogue Script...")
    tracks = parse_dialog_script(sample_script)
    print(f"Successfully loaded {len(tracks)} dialogue sequences.")
    
    print("\nGenerating synchronized SRT subtitle tracks...")
    srt_content = generate_srt_timestamps(tracks)
    print(srt_content)
