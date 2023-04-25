import random
import string
import urllib.request
import socket
import os
import signal
import sys
import time

session_id_status_file_handle = open("session_id_status.txt", "a")
successful_session_id_file_handle = open("existing_sessions.txt", "a") 

# Define a signal handler function
def signal_handler(sig, frame):
    print("Aborting...")
    if session_id_status_file_handle is not None:
        session_id_status_file_handle.close()
    if successful_session_id_file_handle is not None:
        successful_session_id_file_handle.close()        
    # Perform cleanup operations here
    # For example, close file handles, terminate threads, etc.
    sys.exit(0)

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

def handle_exception(exc_type, exc_value, exc_traceback):
    """
    Custom exception handler function.
    """
    # Replace this with your own error handling logic
    print("Uncaught exception occurred:")
    print("Type:", exc_type)
    print("Value:", exc_value)
    print("Traceback:", exc_traceback)

    if session_id_status_file_handle is not None:
        session_id_status_file_handle.close()
    if successful_session_id_file_handle is not None:
        successful_session_id_file_handle.close()        
    # Perform cleanup operations here
    # For example, close file handles, terminate threads, etc.
    sys.exit(0)

# Register the custom exception handler
sys.excepthook = handle_exception

# Function to generate shared session IDs
def generate_shared_session_id():
    chars = string.ascii_lowercase + string.digits  # Characters to choose from
    session_id = ''.join(random.choice(chars) for _ in range(7))
    return session_id

# Function to write session ID status to file
def write_status_to_file(session_id, status, file_handle):
    file_handle.write(session_id + " " + status + " " + (base_url + session_id) + "\n")

# Function to check session ID status from file
def load_tested_sessions():
    sessions = set()
    if os.path.exists("session_id_status.txt"):
        with open("session_id_status.txt", "r") as f:
            for line in f:
                line = line.strip().split()
                sessions.add(line[0].lower())
    return sessions

# Base URL
base_url = "https://sharegpt.com/c/"

tested_sessions = load_tested_sessions()

def check_url(session_id):
    url = base_url + session_id
    try:
        req = urllib.request.Request(url, method='HEAD')  # Use HEAD request
        response = urllib.request.urlopen(req, timeout=3)
        print(f"{session_id}: Exists")  # Print if exists
        return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"{session_id}: Does not exist")  # Print if does not exist
            return False
    except urllib.error.URLError as e:
        return None
    except socket.timeout:
        print(f"{session_id}: Timed out")
        return None
    except Exception as e:
        print(f"{session_id}: Error - {e}")
        return None

# Generate shared session IDs and check their status
minimum_successful = 100
max_errors = 100
success = 0
count = len(tested_sessions)
error = 0

print(f"{len(tested_sessions)} sessions found")

while success < minimum_successful and error < max_errors :
    count += 1    
    print(f"count: {count} error: {error} success: {success}") 
    session_id = generate_shared_session_id()
    if not session_id in tested_sessions:
        # New session ID, mark as generated and test it
        print(f"Generated shared session ID: {session_id}")
        test_result = check_url(session_id)
        if test_result is None:
            error += 1
            time.sleep(5)
        else:
            tested_sessions.add(session_id)
            if test_result:
                print(f"Test result for session ID {session_id}: Passed")
                write_status_to_file(session_id, "exists", session_id_status_file_handle)
                write_status_to_file(session_id, "exists", successful_session_id_file_handle)
                success += 1    
            else:
                print(f"Test result for session ID {session_id}: Failed")
                write_status_to_file(session_id, "failed", session_id_status_file_handle)
    else:
        # Session ID already tested or marked as generated
        print(f"Session ID {session_id} already exists")        