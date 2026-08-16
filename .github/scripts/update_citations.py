import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path


DATA_PATH = Path("data/citations.json")
API_URL = (
    "https://api.semanticscholar.org/graph/v1/paper/batch"
    "?fields=paperId,citationCount"
)


def fetch_counts(paper_ids: list[str]) -> list[dict | None]:
    payload = json.dumps({"ids": paper_ids}).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Awesome-Embodied-Memory/1.0",
    }
    api_key = os.environ.get("S2_API_KEY")
    if api_key:
        headers["x-api-key"] = api_key

    request = urllib.request.Request(API_URL, data=payload, headers=headers)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == 3:
                raise
            time.sleep(15 * (2**attempt))

    raise RuntimeError("Semantic Scholar request failed after retries")


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    tracked = [
        (key, entry["semanticScholarId"])
        for key, entry in data.items()
        if entry.get("semanticScholarId")
    ]

    results = fetch_counts([paper_id for _, paper_id in tracked])
    for (key, _), result in zip(tracked, results, strict=True):
        if result and isinstance(result.get("citationCount"), int):
            data[key]["citationCount"] = result["citationCount"]

    DATA_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
