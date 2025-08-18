def test_fizzbuzz():
    from fizzbuzz_2 import fizzbuzz

    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(7) == 7