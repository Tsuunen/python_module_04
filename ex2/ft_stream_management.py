import sys

if (__name__ == "__main__"):
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    print("Input Stream active. Enter archivist ID: ", end="", flush=True)
    id: str = sys.stdin.readline().strip()
    print("Input Stream active. Enter status report: ", end="", flush=True)
    status: str = sys.stdin.readline().strip()
    print("\n{[}STANDARD{]} Archive status from",
          f"{id}: {status}", file=sys.stdout)
    print("{[}ALERT{]} System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("{[}STANDARD{]} Data transmission complete", file=sys.stdout)
    print("\nThree-channel communication test successful.")
