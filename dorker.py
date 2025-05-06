#!/usr/bin/env python3
import argparse
import webbrowser
import time
import os
import queue
import threading
from datetime import datetime
from urllib.parse import quote
from colorama import Fore, init

init(autoreset=True)

# --- Configuration ---
DEFAULT_DELAY = 1.0
MAX_THREADS = 5
MAX_TABS = 10

# --- Browser Setup ---
def get_browser():
    try:
        # Try to use Chrome with a specific profile
        chrome_path = '/usr/bin/google-chrome'
        if os.path.exists(chrome_path):
            return webbrowser.get(chrome_path)
    except:
        pass
    return webbrowser.get()  # Fallback to default browser

browser = get_browser()

# --- Dork Processing ---
def process_dork(dork, domain=None, engine="google"):
    """Process dork based on search engine"""
    if not domain:
        return dork
        
    if engine == "google":
        if 'site:' not in dork.lower():
            return f'site:{domain} {dork}'
    elif engine == "github":
        return f'{dork} {domain}'  # GitHub doesn't use site: operator
    elif engine == "shodan":
        return f'{dork} hostname:{domain}'  # Shodan uses hostname:
        
    return dork

def build_url(dork, engine):
    """Build search URL for the given engine"""
    encoded = quote(dork)
    return {
        "google": f"https://www.google.com/search?q={encoded}",
        "github": f"https://github.com/search?q={encoded}&type=code",
        "shodan": f"https://www.shodan.io/search?query={encoded}"
    }.get(engine)

# --- Worker Thread ---
def worker(dork_queue, results, delay, engine):
    while True:
        try:
            dork = dork_queue.get_nowait()
        except queue.Empty:
            break

        try:
            url = build_url(dork, engine)
            if not url:
                results.append((dork, "INVALID_ENGINE"))
                continue
                
            browser.open_new_tab(url)
            results.append((dork, "SUCCESS"))
            time.sleep(delay)
        except Exception as e:
            results.append((dork, f"ERROR: {str(e)}"))
        finally:
            dork_queue.task_done()

# --- Main Execution ---
def main():
    print(f"{Fore.CYAN}🔥 Dork Hunter - Processing {args.file}")

    if not os.path.isfile(args.file):
        print(f"{Fore.RED}❌ File not found: {args.file}")
        return

    with open(args.file, 'r', encoding='utf-8') as f:
        raw_dorks = [line.strip() for line in f if line.strip()]

    processed_dorks = [process_dork(d, args.domain, args.engine) for d in raw_dorks]
    print(f"{Fore.BLUE}ℹ️  Loaded {len(processed_dorks)} dorks for {args.engine}")

    dork_queue = queue.Queue()
    for dork in processed_dorks:
        dork_queue.put(dork)

    results = []
    threads = []

    for _ in range(min(args.threads, len(processed_dorks))):
        t = threading.Thread(
            target=worker,
            args=(dork_queue, results, args.delay, args.engine)
        )
        t.start()
        threads.append(t)

    try:
        while any(t.is_alive() for t in threads):
            time.sleep(0.5)
            print(f"{Fore.MAGENTA}ℹ️  Processed: {len(results)}/{len(processed_dorks)}", end='\r')
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}⚠️  Stopping...")

    for t in threads:
        t.join(timeout=1)

    with open("dork_results.log", "a", encoding='utf-8') as log:
        for dork, status in results:
            log.write(f"[{datetime.now()}] {status}: {dork}\n")

    success_count = sum(1 for r in results if r[1] == "SUCCESS")
    print(f"\n{Fore.GREEN}✅ Completed! {success_count}/{len(processed_dorks)} tabs opened")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Dork Hunter")
    parser.add_argument('-f', '--file', required=True, help="File containing dorks")
    parser.add_argument('-e', '--engine', choices=['google', 'github', 'shodan'], default='google')
    parser.add_argument('-d', '--delay', type=float, default=DEFAULT_DELAY, help="Delay between tabs (seconds)")
    parser.add_argument('-t', '--threads', type=int, default=MAX_THREADS, help="Number of threads")
    parser.add_argument('--domain', help="Target domain/hostname")
    args = parser.parse_args()

    if args.delay < 0.1:
        print(f"{Fore.RED}❌ Delay must be ≥ 0.1 seconds")
        exit(1)

    if args.domain and args.engine == "shodan":
        print(f"{Fore.BLUE}ℹ️  Using hostname filtering for Shodan")

    main()