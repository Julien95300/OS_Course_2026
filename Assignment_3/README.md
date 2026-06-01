# Assignment 3 - Process Creation & IPC

## Chosen IPC Mechanism
I chose a **Pipe** (`multiprocessing.Pipe`) as the Inter-Process Communication (IPC) mechanism. 

### Why it is appropriate:
A Pipe sets up a direct, bidirectional, point-to-point communication channel between exactly two processes (one parent and one child). Because this assignment only requires passing a simple string back and forth between one parent and one child, a Pipe is the most lightweight, efficient, and direct solution without the overhead of shared queues or sockets.
