import os
from multiprocessing import Process, Pipe

def child_task(child_conn):
    child_pid = os.getpid()
    print(f"Child [PID {child_pid}] waiting for data...")
    
    # Receive data from parent
    data = child_conn.recv()
    print(f"Child [PID {child_pid}] received: '{data}'")
    
    # Transform data (convert to uppercase)
    transformed = data.upper()
    print(f"Child [PID {child_pid}] sending transformed data back...")
    
    # Send back to parent
    child_conn.send(transformed)
    child_conn.close()

if __name__ == "__main__":
    parent_pid = os.getpid()
    print(f"Parent [PID {parent_pid}] starting.")
    
    # Setup IPC mechanism (Pipe)
    parent_conn, child_conn = Pipe()
    
    # Spawn child process
    p = Process(target=child_task, args=(child_conn,))
    p.start()
    
    message = "hello cloud architecture"
    print(f"Parent [PID {parent_pid}] sending data: '{message}'")
    parent_conn.send(message)
    
    # Receive response from child
    result = parent_conn.recv()
    print(f"Parent [PID {parent_pid}] received back from child: '{result}'")
    
    p.join()

