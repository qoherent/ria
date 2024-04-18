import numpy as np
import pytest

import utils.helpers.array_conversion as array_conversion

ARRAY_2XN_1 = np.array(
    [
        [
            -3.0518509e-05,
            2.7466659e-04,
            -6.1037019e-05,
            -1.8311106e-04,
            -9.1555528e-05,
            -2.7466659e-04,
            -4.2725913e-04,
            -3.0518509e-04,
            -1.5259255e-04,
            -4.2725913e-04,
            0.0000000e00,
            -6.1037019e-05,
            3.6622211e-04,
            5.4933317e-04,
            -9.1555528e-05,
            -3.6622211e-04,
            -1.8311106e-04,
            -1.2207404e-04,
            0.0000000e00,
            3.9674062e-04,
        ],
        [
            3.6622211e-04,
            2.1362957e-04,
            6.1037019e-05,
            1.5259255e-04,
            -9.1555528e-05,
            -6.1037019e-05,
            3.0518509e-04,
            9.1555528e-05,
            -6.1037019e-05,
            3.9674062e-04,
            2.7466659e-04,
            9.1555528e-05,
            -9.1555528e-05,
            3.0518509e-05,
            1.8311106e-04,
            3.3570360e-04,
            5.7985168e-04,
            5.7985168e-04,
            5.4933317e-04,
            3.9674062e-04,
        ],
    ]
)

ARRAY_2XN_2 = np.array(
    [
        [
            -1.2207404e-04,
            -2.1362957e-04,
            3.9674062e-04,
            3.3570360e-04,
            6.1037019e-05,
            2.7466659e-04,
            3.0518509e-04,
            0.0000000e00,
            0.0000000e00,
            2.7466659e-04,
            1.2207404e-04,
            -1.8311106e-04,
            -1.5259255e-04,
            -1.2207404e-04,
            6.1037019e-05,
            6.1037019e-05,
            -9.1555528e-05,
            -3.6622211e-04,
            -6.1037019e-04,
            -1.8311106e-04,
        ],
        [
            2.7466659e-04,
            3.0518509e-05,
            3.9674062e-04,
            7.9348125e-04,
            8.5451826e-04,
            7.0192572e-04,
            5.1881466e-04,
            3.0518509e-04,
            5.4933317e-04,
            5.7985168e-04,
            5.4933317e-04,
            4.2725913e-04,
            5.7985168e-04,
            -2.1362957e-04,
            -3.0518509e-05,
            1.8311106e-04,
            2.4414808e-04,
            6.1037019e-04,
            4.5777764e-04,
            -2.1362957e-04,
        ],
    ]
)

ARRAY_2XN_3 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])

ARRAY_3XN_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

ARRAY_COMPLEX_1 = np.array([1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j])

ARRAY_COMPLEX_2 = np.array(
    [1 + 2j, 3 - 4j, -5 + 6j, 7 + 8j, -9 - 10j, 11 - 12j, 13 + 14j, -15 + 16j, 17 - 18j, 19 + 20j]
)

ARRAY_COMPLEX_3 = np.array([5 + 5j, 6 + 6j, 7 + 7j, 8 + 8j])

ARRAY_2XN_4 = np.array([[5, 6, 7, 8], [5, 6, 7, 8]])


def test_is_real_2xn_np_array1():
    array = ARRAY_2XN_1
    result = array_conversion.is_real_2xn_np_array(array)
    assert result is True


def test_is_real_2xn_np_array2():
    array = ARRAY_2XN_2
    result = array_conversion.is_real_2xn_np_array(array)
    assert result is True


def test_is_real_2xn_np_array3():
    array = ARRAY_2XN_3
    result = array_conversion.is_real_2xn_np_array(array)
    assert result is True


def test_is_real_2xn_np_array4():
    array = ARRAY_3XN_1
    result = array_conversion.is_real_2xn_np_array(array)
    assert result is False


def test_is_real_2xn_np_array5():
    array = "hello"
    result = array_conversion.is_real_2xn_np_array(array)
    assert result is False


def test_is_real_2xn_np_array6():
    array = ARRAY_COMPLEX_1
    result = array_conversion.is_real_2xn_np_array(array)
    assert result is False


def test_is_real_2xn_np_array7():
    array = ARRAY_COMPLEX_2
    result = array_conversion.is_real_2xn_np_array(array)
    assert result is False


def test_is_complex_1xn_np_array1():
    array = ARRAY_COMPLEX_1
    result = array_conversion.is_complex_1xn_np_array(array)
    assert result is True


def test_is_complex_1xn_np_array2():
    array = ARRAY_COMPLEX_2
    result = array_conversion.is_complex_1xn_np_array(array)
    assert result is True


def test_is_complex_1xn_np_array3():
    array = "hello world"
    result = array_conversion.is_complex_1xn_np_array(array)
    assert result is False


def test_is_complex_1xn_np_array4():
    array = np.array("hello world")
    result = array_conversion.is_complex_1xn_np_array(array)
    assert result is False


def test_convert_to_2xn_1():
    array = ARRAY_COMPLEX_1
    converted = array_conversion.convert_to_2xn(array)

    assert np.array_equal(converted, ARRAY_2XN_3)


def test_convert_to_2xn_2():
    # check that it returns if it is already 2xn
    array = ARRAY_2XN_3
    converted = array_conversion.convert_to_2xn(array)
    assert np.array_equal(converted, ARRAY_2XN_3)


def test_convert_to_2xn_3():
    with pytest.raises(ValueError):
        array = np.array("hello")
        array_conversion.convert_to_2xn(array)


def test_convert_to_complex_1():
    array = ARRAY_2XN_3
    converted = array_conversion.convert_to_complex(array)
    assert np.array_equal(converted, ARRAY_COMPLEX_1)


def test_convert_to_complex_2():
    array = ARRAY_COMPLEX_1
    converted = array_conversion.convert_to_complex(array)
    assert np.array_equal(converted, ARRAY_COMPLEX_1)


def test_convert_to_2xn_and_back_1():
    array = ARRAY_COMPLEX_1
    converted = array_conversion.convert_to_2xn(array)
    converted_back = array_conversion.convert_to_complex(converted)
    assert np.array_equal(array, converted_back)
