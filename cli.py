import argparse
import os
from my_project.vowel_counter import count_vowels


def main():
    parser = argparse.ArgumentParser(
        description="Count vowels in a given string or file.",
        epilog="Usage examples:\n"
        "  python cli.py 'Sample Text'\n"
        "  python cli.py -f sample.txt\n"
        "  python cli.py 'Sample Text' -c\n"
        "  python cli.py -f sample.txt -v\n"
        "  python cli.py -f sample.txt -vv -c",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # Define CLI arguments
    parser.add_argument(
        "string",
        nargs="?",
        type=str,
        help="The string to analyze (leave empty to use a file).",
    )

    parser.add_argument(
        "--file",
        "-f",
        type=str,
        help="Path to a file containing the string to analyze (.txt only).",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        help="Enable detailed output: -v for verbose, -vv for extra detailed output.",
    )

    parser.add_argument(
        "--vowels",
        type=str,
        help="Custom set of vowels to count (default: 'aeiou')",
        default="aeiou",
    )

    parser.add_argument(
        "--case-sensitive",
        "-c",
        action="store_true",
        help="Enable case-sensitive vowel counting.",
    )

    parser.add_argument(
        "--chunk-size",
        "-cs",
        type=int,
        default=1000,
        help="Set the chunk size for processing the string. Default is 1000 characters.",
    )

    args = parser.parse_args()

    # Validate vowels argument
    if not args.vowels or not isinstance(args.vowels, str):
        print("Error: Vowels must be a non-empty string.")
        return

    # Validate file input
    if args.file and not args.file.endswith(".txt"):
        print("Error: Only .txt files are supported.")
        return

    # Validate chunk_size argument
    if args.chunk_size <= 0:
        print("Error: Chunk size must be a positive integer.")
        return

    # Handle input: either string or file content
    input_string = None
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as file:
                input_string = file.read().strip()
        except UnicodeDecodeError:
            print(f"Error: Could not decode file '{args.file}' using UTF-8 encoding.")
            return
        except FileNotFoundError:
            print(f"Error: File '{os.path.abspath(args.file)}' not found.")
            return
    else:
        input_string = args.string

    # Validate input content
    if input_string is None or input_string.strip() == "":
        source = (
            f"File '{os.path.abspath(args.file)}'" if args.file else "Provided string"
        )
        print(f"Error: {source} is empty or contains no valid content.")
        return

    if not isinstance(input_string, str):
        print("Error: Input must be a string.")
        return

    # Perform vowel counting
    try:
        result = count_vowels(
            input_string,
            vowels=args.vowels,
            case_sensitive=args.case_sensitive,
            chunk_size=args.chunk_size,
        )
    except TypeError as e:
        print(f"Error: {e}")
        return

    # Handle verbose output
    if args.verbose >= 2:
        # Extra detailed output
        source = os.path.abspath(args.file) if args.file else "Provided string input"
        print(f"Analyzing: {source}")
        print(f"Input: {input_string}")
        print(f"Vowel count: {result}")
    elif args.verbose == 1:
        # Standard verbose output
        print(f"Vowel count: {result}")
    else:
        # Minimal output
        print(result)


if __name__ == "__main__":
    main()
