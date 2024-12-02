import os
import json
import logging
from typing import Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_manifest(path: str) -> Dict:
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse manifest file: {e}")
            raise
    logging.warning(f"Manifest file not found at {path}. Creating new manifest.")
    return {}


def update_manifest(manifest: Dict, changed_modules: list) -> Dict:
    updated = False
    for module in changed_modules:
        if module not in manifest:
            manifest[module] = "0.1.0"
            logging.info(f"Added new module to manifest: {module}")
            updated = True
        else:
            logging.info(f"Module already in manifest: {module}")

    if "." not in manifest:
        manifest["."] = "0.0.0"
        logging.info("Added root entry to manifest")
        updated = True
    else:
        logging.info("Root entry already in manifest")

    if updated:
        logging.info("Manifest was updated")
    else:
        logging.info("No changes were made to the manifest")

    return manifest


def save_manifest(path: str, manifest: Dict):
    try:
        with open(path, 'w') as f:
            json.dump(manifest, f, indent=2)
        logging.info(f"Manifest saved successfully to {path}")
    except IOError as e:
        logging.error(f"Failed to save manifest: {e}")
        raise


def main():
    manifest_path = '.github/.release-please-manifest.json'
    try:
        changed_modules = json.loads(os.environ['CHANGED_MODULES'])
    except KeyError:
        logging.error("CHANGED_MODULES environment variable not set")
        raise
    except json.JSONDecodeError:
        logging.error("Failed to parse CHANGED_MODULES environment variable")
        raise

    retries = 3
    for attempt in range(retries):
        try:
            manifest = load_manifest(manifest_path)
            updated_manifest = update_manifest(manifest, changed_modules)
            save_manifest(manifest_path, updated_manifest)
            logging.info("Manifest updated successfully")
            break
        except Exception as e:
            if attempt < retries - 1:
                logging.warning(f"Attempt {attempt + 1} failed. Retrying...")
            else:
                logging.error(f"Failed to update manifest after {retries} attempts")
                raise


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise
