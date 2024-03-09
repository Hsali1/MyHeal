import sys
import os

def main():
    if len(sys.argv) != 5:
        print(f"argc = {len(sys.argv)} => usage: myheal <source> <prefix> <chunk size (K)> <number of chunks>\n")
        sys.exit(1)

    # making sure chunks are valid
    chunks = int(sys.argv[4])
    if (chunks <= 0) or (chunks > (8192 * 16)):
        print(f"Chunks error. {chunks} needs to be between 1 (1 KB) and {8192 * 16}")
        sys.exit(1)

    chunk_size = 1024 * int(sys.argv[3])
    if chunk_size <= 0 or chunk_size > (1024 * 1024 * 1024):
        print(f"Chunk size error. {chunk_size} needs to be between 1 (1 KB) and {1024 * 1024} (1 GB)")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'wb') as output_file:
            for i in range(chunks):
                chunk_filename = f"{sys.argv[2]}.{str(i).zfill(32)}"
                with open(chunk_filename, 'rb') as chunk_file:
                    chunk_data = chunk_file.read()
                    output_file.write(chunk_data)
                    print(f"Chunk {i + 1} merged successfully.")
            print("All chunks merged successfully.")
    except FileNotFoundError:
        print("Error: One or more chunk files are not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()