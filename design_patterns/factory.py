from abc import ABC, abstractmethod
from pathlib import Path
from dataclasses import dataclass
from typing import Type

# factory using abstract base class


class ProteinDataExporter(ABC):
    """Base class for protein data export"""

    @abstractmethod
    def preprocess_data(self, path: Path) -> None:
        """Preprocess data from FASTA file"""

    @abstractmethod
    def export_data(self, path: Path) -> None:
        """Export data to file"""


class PDBExporter(ProteinDataExporter):
    """Exporter to PDB file format"""

    def preprocess_data(self, path: Path) -> None:
        print("Preparing data for PDB format...")

    def export_data(self, path: Path) -> None:
        print(f"Exporting data to PDB file {path}...")


class EMBLExporter(ProteinDataExporter):
    """Exporter to EMBL file format"""

    def preprocess_data(self, path: Path) -> None:
        print("Preparing data for EMBL format...")

    def export_data(self, path: Path) -> None:
        print(f"Exporting data to EMBL file {path}")


@dataclass
class ProteinExporter:
    exporter: ProteinDataExporter


@dataclass
class ProteinExporterFactory:
    format_exporter_class: Type[ProteinExporter]

    def __call__(self) -> ProteinExporter:
        return ProteinExporter(self.format_exporter_class())


FACTORIES = {"pdb": ProteinExporterFactory(PDBExporter), "embl": ProteinExporterFactory(EMBLExporter)}


def get_factory() -> ProteinExporterFactory:
    """Create data exporter for chosen format"""

    export_format = input(f"Choose export format ({','.join(['PDB','EMBL'])}): ")
    print(f"You have selected {export_format.upper()} format.")
    try:
        return FACTORIES[export_format]
    except KeyError:
        print(f"Entered file format is not supported.")


def export_data(exporter: ProteinExporter):
    """Export data to output file"""

    # preprocess data
    exporter.exporter.preprocess_data("placeholder")
    # create output file
    output_path = Path("./export")
    exporter.exporter.export_data(output_path)


def main():
    # create factory
    factory = get_factory()

    data_exporter = factory()
    # export data with appropriate factory
    export_data(data_exporter)


if __name__ == "__main__":
    main()
