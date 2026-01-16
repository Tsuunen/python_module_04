if (__name__ == "__main__"):
    file_name: str = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    if (file_name != "new_discovery.txt"):
        print("ERROR: You may be overwritting sensible data, double check")
    else:
        try:
            with open(file_name, "w") as file:
                print("Initializing new storage unit: new_discovery.txt")
                print("Storage unit created successfully...\n")
                print("[ENTRY 001] New quantum algorithm discovered")
                file.write("New quantum algorithm discovered\n")
                print("[ENTRY 002] Efficiency increased by 347%")
                file.write("Efficiency increased by 347%\n")
                print("[ENTRY 003] Archived by Data Archivist trainee")
                file.write("Archived by Data Archivist trainee\n")
                print("\nData inscription complete. Storage unit sealed.")
                print(
                    f"Archive '{file_name}' ready for long-term preservation.")
        except Exception:
            print("You may not have the write permission")
