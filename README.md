# Vowel Counter CLI

This is a simple Python project that counts the vowels in a given string or file. It supports both case-sensitive and case-insensitive vowel counting with a simple and flexible command-line interface.

## Project Structure

my_project/ # Main project directory
│
├── my_project/ # Source code package
│ ├── init.py # Makes the folder a package
│ ├── vowel_counter.py # Core module
├── cli.py # Command-line interface
│
├── tests/ # Unit tests
│ └── test_vowel_counter.py
│
├── venv/ # Virtual environment (ignored by Git)
├── .gitignore # Files to ignore in Git
├── requirements.txt # Dependencies
└── README.md # Project overview and instructions

## Features:

- **Count vowels** in strings or text files.
- **Case-sensitive and case-insensitive options** for flexible vowel counting.
- **Chunks** support for large files or strings.
- **Verbose output** for debugging and better visibility of the process.
- **Handles non-text files** by providing meaningful error messages.

## Installation

1. Clone the repository:
   `$ git clone https://github.com/grotari/vowel-counter-cli.git`
   `$ cd vowel-counter-cli`
2. Install dependencies:
   Ensure that you have Python 3.6+ installed. Then, install the required dependencies by running:
   `$ pip install -r requirements.txt`

3. Verify installation:
   Once dependencies are installed, you can check if the application works by running:
   `$ python cli.py --help`

## Usage

### Vowel Counting from a String

To count vowels in a string, run the following command:
`$ python cli.py "Your sample string here"`

### Vowel Counting from a File

To count vowels in a .txt file, use the --file argument:
`$ python cli.py --file yourfile.txt`

### Options

- **--verbose or -v**: Enable verbose output. Use -vv for extra detailed output.
  - -v: Displays only the result.
  - -vv: Displays detailed analysis, including the input string and its vowel count.
- **--case-sensitive or -c**: Enable case-sensitive vowel counting (default: case-insensitive [False]).
- **--file or -f**: Specify the path to a .txt file instead of providing a string.
- **--chunk-size or cs**: Set the chunk size for processing the string (default: [1000] characters).
- **--vowels** (_optional_): Customize the set of characters considered vowels (default: ["aeiou"]).

### Error Handling

- **Empty string, file or vowels**: If the input string, file, or custom vowel set is empty, the program will show an appropriate error message and terminate the process.
- **Invalid file extension**: The program only accepts .txt files. If another type is provided, an error message will be shown.
- **Non-text files**: The program will handle binary or unsupported files gracefully with error messages.
- **Invalid chunk size**: If the --chunk-size value is not a positive integer, the program will raise an error and terminate.

## Testing

This project includes unit tests to ensure the correctness of the vowel counting functionality. You can run the tests with:
`$ python -m unittest discover`

## Contributing

If you’d like to contribute to this project, please fork the repository, make your changes, and submit a pull request. Make sure to include tests for any new features or bug fixes you introduce.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
