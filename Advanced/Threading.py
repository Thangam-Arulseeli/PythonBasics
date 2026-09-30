import threading

def download_report():
    print("Downloading report...")


def send_email():
    print("Sending email...")


thread1 = threading.Thread(
    target=download_report
)

thread2 = threading.Thread(
    target=send_email
)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All tasks completed")
