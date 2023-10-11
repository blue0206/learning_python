from pathlib import Path
import json

path = Path("train/learn.json")
contents = path.read_text()
username = json.loads(contents)

print(f"Hey {username}! Good to have you back!")