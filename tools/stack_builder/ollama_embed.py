"""Shared helper: embed text via local Ollama nomic-embed-text (768-dim, fast, no torch)."""
import requests

OLLAMA_BASE = "http://127.0.0.1:11434"


def embed(text: str) -> list[float]:
    r = requests.post(
        f"{OLLAMA_BASE}/api/embed",
        json={"model": "nomic-embed-text", "input": text},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["embeddings"][0]
