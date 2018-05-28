from typing import *

if TYPE_CHECKING:
    print('we are typechecking')
else:
    print('we are not typechecking')

RequestId = TypeVar('RequestId', int, int)
"""Stuff"""

if __name__ == "__main__":
    def it(i: RequestId) -> None:
        """
        :param i:
        :type i: RequestId
        """
        print(i)

    it(1)

