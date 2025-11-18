from src.extract_transcript import get_transcript
from src.summarize import summarize_long_text

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    print("\nFetching transcript...")
    transcript = get_transcript(url)
    print("\nGenerating summary...")
    summary = summarize_long_text(transcript)
    print("\nFinal Summary:\n")
    print(summary)
