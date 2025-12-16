
# Finding the Largest of Three Numbers
defmodule MathDemo do
  def largest(a, b, c) do
    cond do
      a >= b and a >= c -> a
      b >= a and b >= c -> b
      true -> c
    end
  end
end

IO.puts(MathDemo.largest(20, 15, 30))


# Boolean Function
defmodule BooleanDemo do
  def all_true(a, b, c) do
    a and b and c
  end
end

IO.inspect(BooleanDemo.all_true(true, false, true))

# Sum of Unique Elements in a List
defmodule SumUnique do
  def sum_unique(nums) do
    nums
    |> Enum.filter(fn x -> Enum.count(nums, fn y -> y == x end) == 1 end)
    |> Enum.sum()
  end
end

IO.puts(SumUnique.sum_unique([1, 2, 2, 3, 4, 4, 5]))

# Unique Numbers in a List
numbers = [10, 20, 35, 81, 10, 99, 45, 78, 45]
unique_numbers = Enum.uniq(numbers)
IO.inspect(unique_numbers)

# Collatz Sequence (Recursive)
defmodule Collatz do
  def next_collatz(n) do
    if rem(n, 2) == 0 do
      div(n, 2)
    else
      3 * n + 1
    end
  end

  def sequence(1), do: [1]

  def sequence(n) do
    [n | sequence(next_collatz(n))]
  end
end

IO.inspect(Collatz.sequence(27))



















