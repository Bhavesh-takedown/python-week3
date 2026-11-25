from __future__ import annotations

import argparse

from etl.extract import DEFAULT_URL
from etl.pipeline import DEFAULT_OUTPUT, run_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch users, transform, save CSV")
    parser.add_argument("--url", default=DEFAULT_URL, help="REST API endpoint")
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="CSV destination path",
    )
    args = parser.parse_args()
    path = run_pipeline(url=args.url, output_path=args.output)
    print(f"Wrote {path.resolve()}")


if __name__ == "__main__":
    main()
