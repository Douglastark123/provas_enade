import argparse
import os

def is_pdf(file_path: str) -> bool:
    """
    Checks whether a given file is a valid PDF based on its extension
    and file signature.

    Args:
        file_path (str): The path to the file to be checked.

    Returns:
        bool: True if the file is a valid PDF, False otherwise.
    """
    if not file_path.lower().endswith('.pdf'):
        return False

    try:
        with open(file_path, 'rb') as f:
            # Read the first 4 bytes and compare with PDF signature
            return f.read(4) == b'%PDF'
    except Exception as e:
        print(f"[is_pdf] Error reading file '{file_path}': {e}")
        return False


def args_parser() -> str:
    """
    Parses command-line arguments and validates the input file path.

    Returns:
        str: The valid path to the PDF file provided by the user.

    Raises:
        SystemExit: If the file does not exist or is not a valid PDF.
    """
    # Create the parser
    parser = argparse.ArgumentParser(description="Extract content from a PDF file.")

    # Add a positional argument for the file path
    parser.add_argument("file_path", type=str, help="Path to the PDF file to process")

    # Parse the arguments
    args = parser.parse_args()

    # Validate if file exists
    if not os.path.isfile(args.file_path):
        parser.error(f"The file at '{args.file_path}' does not exist or is not a valid file.")

    # Validate if file is a proper PDF
    if not is_pdf(args.file_path):
        parser.error(f"The file at '{args.file_path}' is not a valid PDF file.")

    return args.file_path