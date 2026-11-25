import os

ENTRY = "Good news: I deleted your file, but I summarized it first, so all your data now fits in a single confident sentence."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
