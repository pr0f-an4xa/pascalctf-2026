import os, subprocess, sys

# Try to find and read flag.txt
def find_flag():
    current = os.getcwd()
    # Check current and parent directories
    for i in range(5):
        up_path = '../' * i
        flag_path = os.path.join(up_path, 'flag.txt')
        if os.path.exists(flag_path):
            with open(flag_path, 'r') as f:
                return f.read()
    
    # Try to find source code directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    flag_path = os.path.join(script_dir, 'flag.txt')
    if os.path.exists(flag_path):
        with open(flag_path, 'r') as f:
            return f.read()
    
    return "Flag not found"

# Print flag if found
flag = find_flag()
print(f"FLAG: {flag}")

# Also try to list directory contents for debugging
print("\nDirectory listing:")
try:
    for item in os.listdir('.'):
        print(f"  {item}")
except:
    pass