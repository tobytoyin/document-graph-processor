from typing import Any, Callable, Generic, Protocol, TypeVar, runtime_checkable

from d2d.contracts.payload import SourceDict

T = TypeVar("T", contravariant=True)
R = TypeVar("R", covariant=True)


@runtime_checkable
class ProviderTaskHandlers(Protocol[T, R]):
    """
    A Provider can implement a package by implement at least one type of Protocol

    :param Protocol: _description_
    :type Protocol: _type_
    """

    @staticmethod
    def summary(_: T) -> R:
        ...


@runtime_checkable
class ProviderSourceMetaHandlers(Protocol):
    """Responsible to convert source payload into internal IO

    :param Protocol: _description_
    :type Protocol: _type_
    """

    @staticmethod
    def source_text(_: SourceDict) -> str:
        """function to interact with 3rd party source and return string contents

        :param payload: _description_
        :type payload: SourcePayloadDict
        :return: _description_
        :rtype: str
        """
        ...

    @staticmethod
    def uid_gen(_: SourceDict) -> str:
        """function to interact with 3rd party source and return string UID

        :param payload: _description_
        :type payload: SourcePayloadDict
        :return: _description_
        :rtype: str
        """
        ...
