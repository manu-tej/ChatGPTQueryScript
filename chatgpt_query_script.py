import subprocess

# Define the AppleScript to activate ChatGPT, open a new chat, and send a query
query = "What is the capital of France?"
applescript = f"""
    tell application "ChatGPT"
        activate
        delay 1
        tell application "System Events"
            keystroke "n" using command down
            delay 1
            keystroke "{query}"
            keystroke return
        end tell
    end tell
"""

# Execute the AppleScript using subprocess
subprocess.run(["osascript", "-e", applescript])
