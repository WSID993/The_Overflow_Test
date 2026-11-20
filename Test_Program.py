import math, time, sys, ctypes, platform

SUF = ["","k","M","B","T","Qd","Qn","Sx","Sp","Oc","No"] + [p+t for t in ["De","Tg","qg","Qg","og","Og","sg","Sg","ng","Ng"] for p in ["","U","D","T","Qd","Qn","Sx","Sp","Oc","No"]][1:] + ["Ce","UCe"]
fmt = lambda v: "INFINITY" if math.isinf(v) else (f"{v:.2f}" if v < 1000 else (f"{v/(10.0**(int(math.log10(v))//3*3)):.2f}{SUF[int(math.log10(v))//3]}" if int(math.log10(v))//3 < len(SUF) else f"{v:.2e}"))

def main():
    print("="*55 + "\n   REAL HARDWARE & PYTHON OVERFLOW BENCHMARK v4.4\n")
    print("\n created by eve(WSID993). This overflow test uses the number suffixes from the Roblox game The Difficulty Upgrade Tree: Classic. \n")
    print("\n Starting the overflow test. It doesn't take long and will show your system's float, integer, and big integer limits. \n")
    print("\n [INFO] System info:This have to be run on a 64-bit system. What's more, it doesn't harm the system. enjoy :D \n")
    print("="*55 + "\n Starting...")
    time.sleep(1.5)
    spd = {"1":10.0, "2":25.0}.get(input("Select Speed [1: Normal / 2: Fast] (Default 1): ").strip(), 10.0)
    print(f"\n[SYSTEM] OS: {platform.system()} {platform.machine()} | Python: {platform.python_version()}\n")

    val, raw_last, last_val, steps, t0 = 1000.0, 1000.0, "1.00k", 0, time.perf_counter()
    while not math.isinf(val):
        raw_last, last_val = val, fmt(val)
        print(f"[FLOAT TEST] Current Value: {last_val}")
        val *= (10.0 ** spd) if val < 1e295 else (1.5 if val < 1e308 else 1.0005)
        steps += 1
        time.sleep(max(0.002, 0.04 / spd))
    elapsed = time.perf_counter() - t0

    c_max = ctypes.c_int64(9223372036854775807)
    c_ovf = ctypes.c_int64(c_max.value + 1).value
    lim = getattr(sys, "get_int_max_str_digits", lambda: 4300)()
    try: _ = str(10 ** lim); bg_ok, bg_err = False, "None"
    except ValueError: bg_ok, bg_err = True, f"ValueError (Exceeded {lim} digits limit)"

    acc = min(100.0, (raw_last / sys.float_info.max) * 100)
    rank, title = ("S+ (SSS Hardware Limit)", "Break Infinity Master") if acc >= 99.9 and c_ovf < 0 and bg_ok else (("S (High Precision)", "Void Walker") if acc >= 95.0 else ("A (Standard)", "Limit Breaker"))

    print(f"\n{'!'*55}\n [OVERFLOW DETECTED] REAL HARDWARE & RUNTIME REPORT\n{'!'*55}\n1. 64-bit Float (IEEE 754) Limit Reached:\n   - TDUT Notation Limit : {last_val}\n   - Exact Decimal Value : {sys.float_info.max:.15e}\n   - Binary Exponent Cap : 2^1024 (11-bit Exponent Max)\n   - Time Elapsed        : {elapsed:.4f}s ({steps} operations)\n{'-'*55}\n2. 64-bit Signed Integer (CPU Register) Test:\n   - Max Positive Value  : {c_max.value:,} (~9.22 Qn)\n   - Value After (+1)    : {c_ovf:,} (Sign-bit wrap-around)\n{'-'*55}\n3. Python BigInt (Dynamic Memory) Security Limit:\n   - Max String Digits   : {lim:,} digits (~10^{lim})\n   - Overflow Result     : {bg_err}\n{'='*55}\n [BENCHMARK SCOREBOARD]\n   - Hardware Precision  : {acc:.2f}% of Theoretical Max\n   - Final Grade         : {rank}\n   - Unlocked Title      : [{title}]\n{'!'*55}")

if __name__ == "__main__":
    main()
