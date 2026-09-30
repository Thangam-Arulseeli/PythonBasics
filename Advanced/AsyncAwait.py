import asyncio


async def download_report():

    print("Downloading report...")

    await asyncio.sleep(3)

    print("Report downloaded")


async def send_email():

    print("Sending email...")

    await asyncio.sleep(2)

    print("Email sent")


async def main():

    await asyncio.gather(
        download_report(),
        send_email()
    )


asyncio.run(main())

