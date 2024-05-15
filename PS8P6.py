def fibonacci_sequence(n):
  fib_sequence = [1, 1]
  for i in range(2, n):
      next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
      fib_sequence.append(next_number)
  return fib_sequence

def main():
  n = 20
  fib_sequence = fibonacci_sequence(n)
  for index, number in enumerate(fib_sequence):
      print(f"Fibonacci number {index + 1}: {number}")

if __name__ == "__main__":
  main()
