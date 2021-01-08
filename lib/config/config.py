import platform
import os

import toml

def get_configuration_dir():
    os_name = platform.system().lower()
    config_dir_ident = "dc_discord_cli_client"

    if os_name == "":
        os_name == "<Even name of platform cannot be determined!>"

    if os_name == "windows":
        config_dir = os.environ["userprofile"] + "\\AppData\\local\\"
    elif os_name == "darwin":
        config_dir = os.environ["HOME"] + "/Library"
    elif os_name == "linux":
        config_dir = os.environ["HOME"] + "/.config"
    else:
        config_dir = os.getcwd() + os.sep + "config"

    config_dir += os.sep + config_dir_ident
    if not os.path.isdir(config_dir):
        print(f"[i] Configuration directory is not found.")
        print(f"    Created in this directory: {config_dir}")
        os.mkdir(config_dir)

    return config_dir + os.sep


class Configuration:
    FILE_PATH = get_configuration_dir() + "config.toml"

    def __init__(self):
        self.discord_token: str = ""
        self.load_config()

    def load_config(self):
        if not os.path.isfile(Configuration.FILE_PATH):
            with open(Configuration.FILE_PATH, mode="w") as f:
                self.save_config()

        config = toml.load(Configuration.FILE_PATH)

        try:
            self.discord_token = config["credentials"]["discord_token"]
        except KeyError:
            print("[!] Failed to load configuration!")
            print("    Maybe some essentail configuration is gone.")
            raise RuntimeError("Cannot load configuration")

    def save_config(self):
        config_data = {
            "credentials": {
                "discord_token": self.discord_token
            }
        }
        path = get_configuration_dir() + "config.ini"
        with open(Configuration.FILE_PATH, mode="w") as f:
            toml.dump(config_data, f)
