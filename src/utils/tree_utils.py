from pathlib import Path

from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree


class DirectoryTreeBuilder:
    def __init__(self, directory: str):
        self.directory = Path(directory)
        self.tree = Tree(
            f":open_file_folder: [link file://{directory}]{directory}",
            guide_style="bold bright_blue",
        )

    def walk_directory(self, directory: Path, tree: Tree) -> None:
        """Recursively build a Tree with directory contents."""
        paths = sorted(
            Path(directory).iterdir(),
            key=lambda path: (path.is_file(), path.name.lower()),
        )
        for path in paths:
            # Remove hidden files
            if path.name.startswith("."):
                continue
            if path.is_dir():
                if path.name == "__pycache__":
                    continue
                style = "dim" if path.name.startswith("__") else ""
                branch = tree.add(
                    f"[bold magenta]:open_file_folder: [link file://{path}]{escape(path.name)}",
                    style=style,
                    guide_style=style,
                )
                self.walk_directory(path, branch)
            else:
                text_filename = Text(path.name, "green")
                text_filename.highlight_regex(r"\..*$", "bold red")
                text_filename.stylize(f"link file://{path}")
                file_size = path.stat().st_size
                text_filename.append(f" ({decimal(file_size)})", "blue")
                icon = "🐍 " if path.suffix == ".py" else "📄 "
                tree.add(Text(icon) + text_filename)

    def build(self) -> Tree:
        """Build and return the directory tree."""
        self.walk_directory(self.directory, self.tree)
        return self.tree


if __name__ == "__main__":
    from rich import print

    tree_builder = DirectoryTreeBuilder("src/")
    tree = tree_builder.build()
    print(tree)
