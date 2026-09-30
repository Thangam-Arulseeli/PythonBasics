from multiprocessing import Process

def process_data(name):
    print(f"Processing {name}")

print ("Starting data processing tasks...")
print("This is a CPU-bound task, so we can use multiprocessing to speed it up." )
print("We will create two separate processes to handle different datasets concurrently. ")
print("This is particularly useful for CPU-bound tasks, as it allows us to utilize multiple CPU cores effectively.  ")
print("Each process will run independently, and we will wait for both to complete before proceeding.  ")    

if __name__ == "__main__":

    p1 = Process(
        target=process_data,
        args=("Dataset A",)
    )

    p2 = Process(
        target=process_data,
        args=("Dataset B",)
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes completed")
    print("This demonstrates how multiprocessing can be used to handle CPU-bound tasks efficiently, allowing for better performance and resource utilization.    ")
