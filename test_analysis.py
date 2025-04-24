import open_atmos_jupyter_utils
from pathlib import Path
import pytest
import numpy as np

def my_simple_function(n, l, h, x_0):
    x = np.zeros(n)
    x[0] = x_0
    for i in range(1, n):
        x[i] = x[i-1]*(l*h+1)
    return x

@pytest.mark.parametrize(
    "n, x_0, expected", (
            (10, 0.0, 0.0),
            (100, 0.0, 0.0),
            (1, 1.0, 1.0)
    )
)
def test_simple_function(n, x_0, expected):
    # Arrange
    time_step = 1
    x_step = 1
    sut = my_simple_function

    # Act
    actual = sut(
        n=n,
        x_0=x_0,
        l=x_step,
        h=time_step,
    )

    # Assert
    np.testing.assert_almost_equal(actual=actual, desired=expected, decimal=3)

