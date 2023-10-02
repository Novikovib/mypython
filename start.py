import time
import multiprocessing
import concurrent.futures
import subprocess
from client import run_client


start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s) ...")
    time.sleep(seconds)
    print("Done sleeping...")
    run_client()
    print("Client is done...")


def run_server():
    subprocess.Popen("python3 tcp_server.py", shell=True)


p1 = multiprocessing.Process(target=run_server)
p2 = multiprocessing.Process(target=do_something, args=[10])

p1.start()
p2.start()

p1.join()
p2.join()


# with concurrent.futures.ProcessPoolExecutor() as executor:
#     f1 = executor.submit(run_server)
#     f2 = executor.submit(do_something, 10)

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")