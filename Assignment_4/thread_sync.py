import threading

counter = 0
mutex = threading.Lock()

def increment_without_sync():
    global counter
    for _ in range(1000000):
        counter += 1

def increment_with_sync():
    global counter
    for _ in range(1000000):
        with mutex:  # Acquires lock, modifies variable, releases lock
            counter += 1

# --- Part 1: The Problem (Race Condition) ---
counter = 0
threads = [threading.Thread(target=increment_without_sync) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()

print("--- PART 1: UNSYNCHRONIZED ---")
print(f"Expected: 4000000")
print(f"Actual:   {counter}")

# --- Part 2: The Solution (Mutex / Lock) ---
counter = 0
threads = [threading.Thread(target=increment_with_sync) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()

print("\n--- PART 2: SYNCHRONIZED ---")
print(f"Expected: 4000000")
print(f"Actual:   {counter}")
