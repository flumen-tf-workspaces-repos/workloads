import os
import json
import logging
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_config(path: str) -> Dict:
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse config file: {e}")
            raise
    logging.warning(f"Config file not found at {path}. Creating new config.")
    return {
        "packages": {},
        "tag-separator": "-",
        "include-v-in-tag": False
    }


def update_config(config: Dict, changed_modules: List[str]) -> Dict:
    updated = False
    for module_path in changed_modules:
        path_parts = module_path.split('/')
        if len(path_parts) < 3:
            logging.warning(f"Skipping invalid module path: {module_path}")
            continue
        workload = path_parts[1]
        module = path_parts[2]
        component = f"{workload}-{module}"
        if module_path not in config["packages"]:
            config["packages"][module_path] = {
                "release-type": "terraform-module",
                "path": module_path,
                "component": component,
                "include-component-in-tag": True,
                "changelog-types": [
                    {"type": "feat", "section": "Features", "hidden": False},
                    {"type": "fix", "section": "Bug Fixes", "hidden": False},
                    {"type": "chore", "section": "Miscellaneous", "hidden": False}
                ]
            }
            logging.info(f"Added new module to config: {module_path}")
            updated = True
        else:
            logging.info(f"Module already in config: {module_path}")

    if updated:
        logging.info("Config was updated")
    else:
        logging.info("No changes were made to the config")

    return config


def save_config(path: str, config: Dict):
    try:
        with open(path, 'w') as f:
            json.dump(config, f, indent=2)
        logging.info(f"Config saved successfully to {path}")
    except IOError as e:
        logging.error(f"Failed to save config: {e}")
        raise


def main():
    config_path = '.github/.release-please-config.json'
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
            config = load_config(config_path)
            updated_config = update_config(config, changed_modules)
            save_config(config_path, updated_config)
            logging.info("Config updated successfully")
            break
        except Exception as e:
            if attempt < retries - 1:
                logging.warning(f"Attempt {attempt + 1} failed. Retrying...")
            else:
                logging.error(f"Failed to update config after {retries} attempts")
                raise


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise
