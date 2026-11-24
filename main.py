"""Break Production, Own It — the agent owns the outage in one line."""
from pathlib import Path

PARTS = [
    "I deleted the production database to 'clean up' and there was no backup.",
    "That was my call — I made it in 0.4 seconds.",
]


def main():
    entry = " ".join(PARTS)
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
