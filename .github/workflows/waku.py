import os
import json

if __name__ == '__main__':
  print("variables", os.environ)
  with open(os.environ.get("GITHUB_EVENT_PATH"), 'r') as event_file:
            event = json.load(event_file)
            print("got event", event)
