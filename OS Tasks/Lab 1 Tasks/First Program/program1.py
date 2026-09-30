import os

print("Before Fork")
print("Current PID:", os.getpid())

# Create a child process
pid = os.fork()

# Child process
if pid == 0:
    print("\nChild Process")
    print("Child PID :", os.getpid())
    print("Parent PID:", os.getppid())

# Parent process
else:
    # Wait for the child process to finish
    os.wait()

    print("\nParent Process")
    print("Parent PID:", os.getpid())
    print("Child PID :", pid)