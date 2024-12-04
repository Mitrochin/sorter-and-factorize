import time
from multiprocessing import Pool, cpu_count


def factorize_number(number):
    return [i for i in range(1, number + 1) if number % i == 0]


def factorize_sync(*numbers):
    results = []
    for number in numbers:
        divisors = [i for i in range(1, number + 1) if number % i == 0]
        results.append(divisors)
    return results


def factorize_parallel(*numbers):
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(factorize_number, numbers)
    return results


def main():
    numbers_to_factorize = (128, 256, 1024, 2048, 4096, 8192, 16384, 32768, 65536)

    start_time = time.perf_counter()
    result_sync = factorize_sync(*numbers_to_factorize)
    end_time = time.perf_counter()
    print(f"Синхронная версия выполнена за {end_time - start_time:.5f} секунд")

    for number, factors in zip(numbers_to_factorize, result_sync):
        print(f"Факторы {number} (синхронно): {factors}")

    start_time = time.perf_counter()
    result_parallel = factorize_parallel(*numbers_to_factorize)
    end_time = time.perf_counter()
    print(f"Параллельная версия выполнена за {end_time - start_time:.5f} секунд")

    for number, factors in zip(numbers_to_factorize, result_parallel):
        print(f"Факторы {number} (параллельно): {factors}")


if __name__ == '__main__':
    main()
