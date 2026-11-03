from logic import (
    calculate_discount
)


# 4. Test dla calculate_discount (w tym test na wyjątek ValueError)
def test_calculate_discount():
    assert calculate_discount(100.0, 0.2) == 80.0
    assert calculate_discount(50.0, 0.0) == 50.0
    assert calculate_discount(200.0, 1.0) == 0.0
    assert calculate_discount(100.0, -0.1) == 0.0
    assert calculate_discount(100.0, 1.5) == 0.0
