# main.py
import asyncio
import sys


import os
import sys

# လက်ရှိ main.py ရှိတဲ့ folder ထဲက .so ဖိုင်ကို တိုက်ရိုက် ဆွဲသုံးခိုင်းခြင်း
sys.path.append(os.path.dirname(os.path.abspath(__file__)))




from yourgod import start  # yourgod.so ဖိုင်ထဲက start function ကို လှမ်းခေါ်ခြင်း

if __name__ == '__main__':
    try:
        # Event Loop တစ်ခုတည်းကနေ tool တစ်ခုလုံးကို မောင်းနှင်သွားပါမယ်
        asyncio.run(start())
    except KeyboardInterrupt:
        print(f"\n\n\033[1;31m[!] ABORTED: Core Execution Halted by YourGod.\033[0m\n")
        sys.exit(0)
