import subprocess

# run external command
result = subprocess.run(['C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'], capture_output=True, encoding='UTF-8')

print(result)

# run python3 and give input code to run
pythonCode= print(f"Hello world")
result2 = subprocess.run(['python3'], input= pythonCode, capture_output=True, encoding='UTF-8')
print(result2.stdout)

# be aware of command injection with user input with semicolons;
# User input is always dangerous