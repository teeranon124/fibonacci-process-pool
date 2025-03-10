# fibonacci-process-pool

This repository demonstrates the use of Python's `multiprocessing.Pool` to perform parallel processing for CPU-intensive tasks, specifically calculating the Fibonacci sequence. It also compares the performance of parallel processing with sequential execution.


## Introduction
This project is a small Python program that calculates the Fibonacci sequence using two approaches:
1. **Parallel Processing**: Uses `multiprocessing.Pool` to distribute the workload across multiple CPU cores.
2. **Sequential Execution**: Calculates the Fibonacci sequence in a single process.

The goal is to demonstrate the performance benefits of parallel processing for CPU-bound tasks.

## Features
- **Parallel Processing**: Utilizes `multiprocessing.Pool` to calculate Fibonacci numbers concurrently.
- **Sequential Execution**: Provides a baseline for comparing the performance of parallel processing.
- **Performance Comparison**: Measures and compares the execution time of both approaches.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/teeranon124/fibonacci-process-pool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd parallel-processing-examples
   ```
3. Run the Python script:
   ```bash
   python process_pool_vs_sequential.py
   ```

## Code Structure
- **`process_pool_vs_sequential.py`**: The main script that implements both parallel and sequential Fibonacci calculations.
  - `fibonacci(n)`: A recursive function to calculate the Fibonacci sequence.
  - `calculate_fibonacci_parallel(numbers)`: Uses `multiprocessing.Pool` to calculate Fibonacci numbers in parallel.
  - `calculate_fibonacci_sequential(numbers)`: Calculates Fibonacci numbers sequentially.
  - Performance comparison is done in the `__main__` block.

## Results
When you run the script, it will output the time taken for both parallel and sequential execution, along with a comparison of their performance. For example:
```
Starting parallel Fibonacci calculation
Parallel duration: 4.23 seconds

Starting sequential Fibonacci calculation
Sequential duration: 12.56 seconds

Parallel is 2.97x faster than sequential
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
