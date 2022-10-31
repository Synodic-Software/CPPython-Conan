"""Conan provider for CPPython"""

from pathlib import Path
from typing import Any

from cppython_core.plugin_schema.provider import Provider
from cppython_core.schema import SyncData


class ConanProvider(Provider):
    """Conan provider implementation"""

    @staticmethod
    def name() -> str:
        """_summary_

        Returns:
            _description_
        """
        return "conan"

    def activate(self, data: dict[str, Any]) -> None:
        """_summary_

        Args:
            data: _description_
        """

    def sync_data(self, name: str) -> SyncData:
        """_summary_

        Args:
            name: _description_

        Returns:
            _description_
        """

        return SyncData(name=self.name(), data=None)

    @classmethod
    async def download_tooling(cls, path: Path) -> None:
        """_summary_

        Args:
            path: _description_
        """

    @classmethod
    def tooling_downloaded(cls, path: Path) -> bool:
        """_summary_

        Args:
            path: _description_

        Returns:
            _description_
        """

        return True

    def install(self) -> None:
        """_summary_"""

    def supports_generator(self, name: str) -> bool:
        """_summary_

        Args:
            name: _description_

        Returns:
            _description_
        """

        return name == "cmake"

    def update(self) -> None:
        """_summary_"""
