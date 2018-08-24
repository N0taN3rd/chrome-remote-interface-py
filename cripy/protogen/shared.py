from typing import Iterable, Optional, Set, Union

ForeignRefs = Optional[Set[str]]

__all__ = ["FRefCollector"]


class FRefCollector(object):
    def __init__(self) -> None:
        self.foreign_refs: Optional[Set[str]] = None

    def prune(self, remove_me: Iterable[str]) -> None:
        if self.has_foreign_refs:
            self.foreign_refs.difference_update(remove_me)
            if len(self.foreign_refs) == 0:
                self.foreign_refs = None

    @property
    def has_foreign_refs(self) -> bool:
        return self.foreign_refs is not None

    def _if_foreign_ref_add(self, it: Optional) -> None:
        if it is None:
            return
        if getattr(it, "is_foreign_ref", False):
            self._add_foreign_ref(it.foreign_ref)
        if getattr(it, "has_foreign_refs", False):
            self._add_foreign_ref(it.foreign_refs)

    def _add_foreign_ref(self, ref: Union[str, Iterable[str]]) -> None:
        if self.foreign_refs is None:
            self.foreign_refs = set()
        if isinstance(ref, str):
            self.foreign_refs.add(ref)
        else:
            self.foreign_refs.update(ref)
