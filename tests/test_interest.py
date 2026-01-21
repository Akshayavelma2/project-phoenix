from src.bank.interest import calculate_interest

def test_interest_calculation():
    amount = 1000
    rate = 0.05
    expected = 50
    assert calculate_interest(amount, rate) == expected
