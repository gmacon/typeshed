# Stubs for itertools

# Based on https://docs.python.org/2/library/itertools.html

from typing import (Iterator, TypeVar, Iterable, overload, Any, Callable, Tuple,
                    Union, Sequence, Generic, Optional)

_T = TypeVar('_T')
_S = TypeVar('_S')

def count(start: int = ...,
          step: int = ...) -> Iterator[int]: ...  # more general types?
def cycle(iterable: Iterable[_T]) -> Iterator[_T]: ...

def repeat(object: _T, times: int = ...) -> Iterator[_T]: ...

def accumulate(iterable: Iterable[_T]) -> Iterator[_T]: ...

class chain(Iterator[_T], Generic[_T]):
    def __init__(self, *iterables: Iterable[_T]) -> None: ...
    def next(self) -> _T: ...
    def __iter__(self) -> Iterator[_T]: ...
    @staticmethod
    def from_iterable(iterable: Iterable[Iterable[_S]]) -> Iterator[_S]: ...

def compress(data: Iterable[_T], selectors: Iterable[Any]) -> Iterator[_T]: ...
def dropwhile(predicate: Callable[[_T], Any],
              iterable: Iterable[_T]) -> Iterator[_T]: ...
def ifilter(predicate: Callable[[_T], Any],
            iterable: Iterable[_T]) -> Iterator[_T]: ...
def ifilterfalse(predicate: Callable[[_T], Any],
                 iterable: Iterable[_T]) -> Iterator[_T]: ...

@overload
def groupby(iterable: Iterable[_T]) -> Iterator[Tuple[_T, Iterator[_T]]]: ...
@overload
def groupby(iterable: Iterable[_T],
            key: Callable[[_T], _S]) -> Iterator[Tuple[_S, Iterator[_T]]]: ...

@overload
def islice(iterable: Iterable[_T], stop: int) -> Iterator[_T]: ...
@overload
def islice(iterable: Iterable[_T], start: int, stop: Optional[int],
           step: int = ...) -> Iterator[_T]: ...

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_T6 = TypeVar('_T6')

@overload
def imap(func: Callable[[_T1], _S], iter1: Iterable[_T1]) -> Iterator[_S]: ...
@overload
def imap(func: Callable[[_T1, _T2], _S],
        iter1: Iterable[_T1],
        iter2: Iterable[_T2]) -> Iterator[_S]: ...  # TODO more than two iterables

def starmap(func: Any, iterable: Iterable[Any]) -> Iterator[Any]: ...
def takewhile(predicate: Callable[[_T], Any],
              iterable: Iterable[_T]) -> Iterator[_T]: ...
def tee(iterable: Iterable[Any], n: int = ...) -> Iterator[Any]: ...

@overload
def izip(iter1: Iterable[_T1]) -> Iterator[Tuple[_T1]]: ...
@overload
def izip(iter1: Iterable[_T1],
         iter2: Iterable[_T2]) -> Iterator[Tuple[_T1, _T2]]: ...
@overload
def izip(iter1: Iterable[_T1], iter2: Iterable[_T2],
         iter3: Iterable[_T3]) -> Iterator[Tuple[_T1, _T2, _T3]]: ...
@overload
def izip(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3],
         iter4: Iterable[_T4]) -> Iterator[Tuple[_T1, _T2,
                                           _T3, _T4]]: ...
@overload
def izip(iter1: Iterable[_T1], iter2: Iterable[_T2],
         iter3: Iterable[_T3], iter4: Iterable[_T4],
         iter5: Iterable[_T5]) -> Iterator[Tuple[_T1, _T2,
                                                 _T3, _T4, _T5]]: ...
@overload
def izip(iter1: Iterable[_T1], iter2: Iterable[_T2],
         iter3: Iterable[_T3], iter4: Iterable[_T4],
         iter5: Iterable[_T5], iter6: Iterable[_T6]) -> Iterator[Tuple[_T1, _T2, _T3,
                                                                 _T4, _T5, _T6]]: ...
def izip(*iter: Iterable[Any]) -> Iterator[tuple]: ...
# TODO izip loses type information for 6 arguments and more

def izip_longest(*p: Iterable[Any],
                 fillvalue: Any = ...) -> Iterator[Any]: ...

# TODO: Return type should be Iterator[Tuple[..]], but unknown tuple shape.
#       Iterator[Sequence[_T]] loses this type information.
def product(*p: Iterable[_T], repeat: int = ...) -> Iterator[Sequence[_T]]: ...

def permutations(iterable: Iterable[_T],
                 r: int = ...) -> Iterator[Sequence[_T]]: ...
def combinations(iterable: Iterable[_T],
                 r: int) -> Iterator[Sequence[_T]]: ...
def combinations_with_replacement(iterable: Iterable[_T],
                                  r: int) -> Iterator[Sequence[_T]]: ...
