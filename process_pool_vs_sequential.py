# process_pool_vs_sequential.py
import multiprocessing
import time


def fibonacci(n):
    # คำนวณ Fibonacci sequence แบบ recursive
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def calculate_fibonacci_parallel(numbers):
    # ใช้ Process Pool เพื่อคำนวณ Fibonacci sequence แบบ process pool
    with multiprocessing.Pool() as pool:
        pool.map(fibonacci, numbers)


def calculate_fibonacci_sequential(numbers):
    # คำนวณ Fibonacci sequence แบบปกติตามลำดับ ใช้ loop
    for number in numbers:
        fibonacci(number)


if __name__ == "__main__":
    # สร้างลิสต์ของตัวเลขสำหรับการคำนวณ Fibonacci
    numbers = [
        int(i) for i in input("Enter your number :").split()
    ] * 2  # ใช้เลขซ้ำเพื่อเพิ่มภาระงาน

    # วัดเวลาการทำงานแบบprocess pool
    print("Starting parallel Fibonacci calculation")
    start = time.time()
    calculate_fibonacci_parallel(numbers)
    parallel_duration = time.time() - start
    print(f"Parallel duration: {parallel_duration} seconds")

    # วัดเวลาการทำงานแบบปกติตามลำดับ ใช้ loop
    print("Starting sequential Fibonacci calculation")
    start = time.time()
    calculate_fibonacci_sequential(numbers)
    sequential_duration = time.time() - start
    print(f"Sequential duration: {sequential_duration} seconds")

    # แสดงผลลัพธ์เปรียบเทียบ
    print(
        f"\nParallel is {sequential_duration / parallel_duration:.2f}x faster than sequential"
    )
