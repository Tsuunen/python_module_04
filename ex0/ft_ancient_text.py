if (__name__ == "__main__"):
    file_name: str = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault:", file_name)

    try:
        with open(file_name, "r") as file:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(file.read())
            print("\nData recovery complete. Storage unit disconnected.")
    except Exception:
        print("ERROR: Storage vault not found")
