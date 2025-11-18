# src/utils.py
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

def split_text(text: str, max_tokens: int = 700) -> list:
    """Split text into chunks that fit within the model's token limit."""
    tokens = tokenizer.encode(text)
    chunks = []

    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunk_text = tokenizer.decode(chunk_tokens, skip_special_tokens=True)
        chunks.append(chunk_text)

    return chunks
