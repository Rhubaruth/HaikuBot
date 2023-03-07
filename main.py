import bot

import os
import sys
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if TOKEN is None:
        print("Token is None")
        sys.exit()
    # print_hi('PyCharm')
    bot.bot.run(TOKEN)
