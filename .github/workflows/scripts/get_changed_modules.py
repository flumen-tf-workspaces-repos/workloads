import re
import json
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_changed_modules(file_paths: str) -> set:
    """
    Identify changed modules from a list of changed file paths.

    Args:
        file_paths (str): A string containing all modified file paths, separated by spaces.

    Returns:
        set: Set of unique module paths that have changed.
    """
    regex = r"(workloads/[^/]+/[^/]+)"
    matches = re.findall(regex, file_paths)
    return set(matches)


def main():
    """
    Main function to find changed modules and output the result.
    """
    try:
        all_modified_files = os.environ['MODIFIED_FILES']
    except KeyError:
        logging.error("MODIFIED_FILES environment variable not set")
        raise

    changed_modules = get_changed_modules(all_modified_files)
    result = json.dumps(list(changed_modules))
    print(f"result={result}")
    logging.info(f"Changed modules: {result}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise
