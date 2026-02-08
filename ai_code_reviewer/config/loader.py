from pathlib import Path
import tomllib


def load_pyproject(path: Path | None = None) -> dict:
    if path is None:
        path = Path("pyproject.toml")

    if not path.exists():
        return {}

    with open(path, "rb") as f:
        return tomllib.load(f)
