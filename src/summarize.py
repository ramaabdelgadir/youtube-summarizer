from transformers import pipeline
from src.utils import split_text

# Load summarizer once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_chunk(chunk: str) -> str:
    """
    Summarize a single chunk of text.
    We use a shorter max_length to get dense "key points".
    """
    summary = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

def summarize_final_summary(text: str) -> str:
    """
    Summarizes the combined "summary of summaries" into a final paragraph.
    We give this a longer max_length to allow the model to
    create a more coherent, flowing narrative.
    """
    summary = summarizer(text, max_length=300, min_length=75, do_sample=False)
    return summary[0]['summary_text']

def summarize_long_text(text: str) -> str:
    """Hierarchical summarization for long transcripts."""
    
    chunks = split_text(text, max_tokens=700)
    chunk_summaries = [summarize_chunk(chunk) for chunk in chunks]
    combined = " ".join(chunk_summaries)
    final_summary = summarize_final_summary(combined)
    
    return final_summary