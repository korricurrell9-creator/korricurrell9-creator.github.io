#!/usr/bin/env python3

import sys
import json
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# Silence TLS warnings (many VPN portals use broken certs)
requests.packages.urllib3.disable_warnings()

URLS_FILE = "urls.txt"
OUTPUT_FILE = "results.json"
WORKERS = 5
TIMEOUT = 10


def _read_urls(path: str | Path) -> list[str]:
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def _make_request(url: str) -> dict:
    try:
        resp = requests.get(
            url,
            timeout=TIMEOUT,
            allow_redirects=True,
            verify=False,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
            },
        )

        return {
            "url": url,
            "final_url": resp.url,
            "status_code": resp.status_code,
            "body": resp.text[:5000],
            "error": None,
        }

    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "final_url": None,
            "status_code": None,
            "body": None,
            "error": str(e),
        }


def _collect_results(urls: list[str]) -> list[dict]:
    results: list[dict] = []

    with ThreadPoolExecutor(max_workers=WORKERS) as exe:
        for result in exe.map(_make_request, urls):
            results.append(result)

    return results


def _write_results(path: str | Path, results: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


def main():
    if not Path(URLS_FILE).is_file():
        print(f"ERROR: {URLS_FILE} not found", file=sys.stderr)
        sys.exit(1)

    urls = _read_urls(URLS_FILE)

    if not urls:
        print("ERROR: urls.txt is empty", file=sys.stderr)
        sys.exit(1)

    results = _collect_results(urls)
    _write_results(OUTPUT_FILE, results)

    print(f"✅  {len(results)} requests completed – output written to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
