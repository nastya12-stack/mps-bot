from pathlib import Path


def path_to(name: str) -> Path:
    project_root = Path(__file__).parent.parent
    assets_dir = project_root.joinpath("assets")
    return assets_dir.joinpath(name)
