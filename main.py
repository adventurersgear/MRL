import curses
import random
import threading
import time

def update_bit_stream(window, y, x):
    bit_stream = []
    while True:
        bit = random.choice([0, 1])
        bit_stream.append(str(bit))
        if len(bit_stream) > 20:
            bit_stream.pop(0)
        window.addstr(y, x, "BIT STREAM =[" + "".join(bit_stream) + "]")
        window.refresh()
        time.sleep(0.5)

def update_memory_space(window, y, x):
    memory_space = []
    while True:
        element = random.choice(['U', '0'])
        memory_space.append(element)
        if len(memory_space) > 10:
            memory_space.pop(0)
        window.addstr(y, x, "Most Recent Elements: " + ", ".join(memory_space))
        window.refresh()
        time.sleep(1)

def main(window):
    # Initialize curses environment
    curses.curs_set(0)
    window.clear()
    window.refresh()

    # Start threads for real-time updates
    bit_stream_thread = threading.Thread(target=update_bit_stream, args=(window, 0, 0))
    memory_space_thread = threading.Thread(target=update_memory_space, args=(window, 2, 0))
    
    bit_stream_thread.start()
    memory_space_thread.start()

    window.addstr(4, 0, "Press 'q' to quit...")
    window.refresh()

    while True:
        c = window.getch()
        if c == ord('q'):
            break

    # Stop threads
    bit_stream_thread.join()
    memory_space_thread.join()

# Run the curses application
curses.wrapper(main)
