# main.py
import asyncio
import sys


import os
import sys

import os
import sys
import ctypes

# ၁။ လက်ရှိ main.py ရှိနေတဲ့ Folder လမ်းကြောင်းကို အလိုအလျောက် ယူခြင်း
current_dir = os.path.dirname(os.path.abspath(__file__))

# ၂။ Python ရဲ့ လမ်းကြောင်းထဲ ထည့်ပေးခြင်း
sys.path.append(current_dir)

# ၃။ yourgod.so ကို လက်ရှိ folder ထဲကနေပဲ တိုက်ရိုက်ခေါ်ခြင်း
so_path = os.path.join(current_dir, "yourgod.so")
lib = ctypes.CDLL(so_path)

# ၄။ ပြီးမှ start function ကို လှမ်းခေါ်ပါ
lib.start.argtypes = []



from yourgod import start  # yourgod.so ဖိုင်ထဲက start function ကို လှမ်းခေါ်ခြင်း

if __name__ == '__main__':
    try:
        # Event Loop တစ်ခုတည်းကနေ tool တစ်ခုလုံးကို မောင်းနှင်သွားပါမယ်
        asyncio.run(start())
    except KeyboardInterrupt:
        print(f"\n\n\033[1;31m[!] ABORTED: Core Execution Halted by YourGod.\033[0m\n")
        sys.exit(0)
