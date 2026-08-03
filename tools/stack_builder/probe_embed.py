#!/usr/bin/env python3
"""Runtime probe: sentence-transformers embed two strings, cosine similarity."""
import sys
from sentence_transformers import SentenceTransformer, util


def main() -> int:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    a = "Olrun observed the factory pipeline stalling overnight."
    b = "Last night the factory pipeline stopped making progress."
    c = "The weather in Reykjavik was cold and rainy."
    emb = model.encode([a, b, c])
    sim_similar = float(util.cos_sim(emb[0], emb[1]))
    sim_different = float(util.cos_sim(emb[0], emb[2]))
    print(f"sim(similar pair)={sim_similar:.4f}")
    print(f"sim(different pair)={sim_different:.4f}")
    ok = sim_similar > 0.7 and sim_similar > sim_different
    print(f"PROBE_PASS={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
