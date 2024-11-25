import pytest
from task1.solution import check_annotation


@check_annotation
def check_f(a: str, b: int, c: list, *args: int, **kwargs: int):
    return True

@pytest.mark.parametrize(
    'a, b, c, args, kwargs',
    [
        ('str', 1, [1, 3, 'str'], (1, 2), {'kwarg1': 3, 'kwarg2': 4}),
        ('s', 2, [123, 22], (1, ), {}),
        ('st', 4, [12, 33], (), {}),
    ]
)
def test_annotation_correct(a, b, c, args, kwargs):
    assert check_f(a, b, c, *args, **kwargs) == True 


@pytest.mark.parametrize(
    'a, b, c, args, kwargs',
    [
        ('str', 1, [1, 3, 'str'], (1, 2), {'kwarg1': 3, ('kwarg2', ): 1}),
        ('str', 1, [1, 3, 'str'], (1, '2'), {'kwarg1': 3, 'kwarg2': 4}),
        ('str', 1, (1, 3, 'str'), (1, 2), {'kwarg1': 3, 'kwarg2': 4}),
        ('s', 'str', [123, 22], (1, ), {}),
        (3, 4, [12, 33], (), {}),
    ]
)
def test_annotation_incorrect(a, b, c, args, kwargs):
    with pytest.raises(TypeError):
        check_f(a, b, c, *args, **kwargs)


