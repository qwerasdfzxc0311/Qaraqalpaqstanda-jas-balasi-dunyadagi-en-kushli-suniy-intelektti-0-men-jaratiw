from __future__ import annotations

import argparse
from pathlib import Path

from .pipeline import CognitivePipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Qaraqalpaq local synthetic-core demo")
    parser.add_argument("query", help="Question for the bundled synthetic fixture")
    args = parser.parse_args()
    fixture = Path(__file__).resolve().parents[2] / "fixtures" / "knowledge.json"
    result = CognitivePipeline(fixture).answer(args.query)
    print(result.answer)
    print(f"\nstatus={result.status.value}")
    print(f"task_id={result.task_id}")


if __name__ == "__main__":
    main()
