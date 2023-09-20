#!/usr/bin/python3
""""Define MyInt class"""


class MyInt(int):
    """
    An inherited int class

    """
    def __eq__(self, value):
        """Override == operator with != behaviour."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return super().__eq__(value)
