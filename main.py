import sys
from analyzer import analyze_log


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    results = analyze_log(logfile)

    print("Log summary:")
    for level, count in results.items():
        print(f"{level}: {count}")


if __name__ == "__main__":
    main()
