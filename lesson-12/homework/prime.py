# %%
import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end, result):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)

def main():
    start_range = int(input("Boshlanish soni: "))
    end_range = int(input("Tugash soni: "))
    num_threads = int(input("Iplar soni: "))

    threads = []
    results = []  
    results_lock = threading.Lock()  
    def thread_task(s, e):
        local_primes = []
        for n in range(s, e):
            if is_prime(n):
                local_primes.append(n)
       
        with results_lock:
            results.extend(local_primes)

    total_numbers = end_range - start_range
    chunk_size = total_numbers // num_threads
    for i in range(num_threads):
        s = start_range + i * chunk_size
        
        e = start_range + (i + 1) * chunk_size if i != num_threads - 1 else end_range
        t = threading.Thread(target=thread_task, args=(s, e))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    results.sort()
    print(f"Topilgan tub sonlar: {results}")

if __name__ == "__main__":
    main()


# %%
import threading
from collections import Counter

def count_words(lines, counter, lock):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    with lock:
        counter.update(local_counter)

def main():
    filename = input("Fayl nomi kiriting: ")
    num_threads = int(input("Iplar soni: "))

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads

    threads = []
    word_counter = Counter()
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else total_lines
        t = threading.Thread(target=count_words, args=(lines[start:end], word_counter, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("So'zlar soni:")
    for word, count in word_counter.most_common(20):  
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()



