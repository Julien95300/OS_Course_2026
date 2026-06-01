# Assignment 4 - Threads & Synchronization

## What is a Race Condition?
Based on my observations in Part 1, a **race condition** occurs when multiple execution threads access and modify a shared global resource (the counter variable) simultaneously without synchronization. 

Because the operation `counter += 1` is not atomic at the CPU level (it involves reading, incrementing, and writing back), threads interrupt each other mid-step. They overwrite each other's updates, causing the final calculated value to be lower than the expected 4,000,000.

## How the Mutex Solved the Problem
In Part 2, a **Mutex (threading.Lock)** was implemented. The lock ensures **mutual exclusion**. Only one thread can acquire the lock and access the counter at any given time. Other threads are forced to wait until the current thread finishes its cycle and releases the lock. This keeps the data safe and results in exactly 4,000,000.
