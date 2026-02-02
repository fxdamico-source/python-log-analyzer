from collections import Counter


def analyze_log(file_path: str) -> dict:
    """
    Reads a log file and counts log levels.
    Returns a dictionary like: {"INFO": 3, "ERROR": 2}
    """
    counts = Counter()

    with open(file_path, "r") as f:
        for line in f:
            level = line.split()[0]
            counts[level] += 1

    return dict(counts)
