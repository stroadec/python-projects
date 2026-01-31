import argparse
from utils.processor import process_file

def main():
    parser = argparse.ArgumentParser(description="CLI Automation Tool")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")

    args = parser.parse_args()
    process_file(args.input, args.output)

    print("✅ Processing completed")

if __name__ == "__main__":
    main()
