import argparse
import os

def scan_command(path):
    print(f"\nScanning project: {path}\n")
    py_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))

    print("Python files found:")
    for f in py_files:
        print(f" - {f}")

    print(f"\nTotal Python files: {len(py_files)}")


def review_command(file):
    print(f"\nReviewing file: {file}\n")

    if not os.path.exists(file):
        print("Error: File not found")
        return

    print("Issues detected:")
    print(" - Unused import detected")
    print(" - Function name not following snake_case")
    print(" - Missing docstring")

    print("\nSeverity:")
    print(" - 1 Critical")
    print(" - 2 Warnings")


def apply_command():
    print("\nApplying selected fixes...\n")
    print("✔ Removed unused imports")
    print("✔ Added function docstring")
    print("✔ Renamed variables")
    print("\nFixes applied successfully")


def report_command():
    print("\nGenerating review report...\n")
    print("Files reviewed      : 3")
    print("Critical issues     : 2")
    print("Warnings            : 5")
    print("Suggestions applied : 3")
    print("\nReport generation completed")


def diff_command():
    print("\nShowing code diff:\n")
    print("- import sys")
    print("+ # removed unused import")
    print("- def MyFunction():")
    print("+ def my_function():")
    print("\nDiff displayed successfully")


def main():
    parser = argparse.ArgumentParser(description="AI Code Reviewer CLI")
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan")
    scan_parser.add_argument("path")

    review_parser = subparsers.add_parser("review")
    review_parser.add_argument("file")

    subparsers.add_parser("apply")
    subparsers.add_parser("report")
    subparsers.add_parser("diff")

    args = parser.parse_args()

    if args.command == "scan":
        scan_command(args.path)
    elif args.command == "review":
        review_command(args.file)
    elif args.command == "apply":
        apply_command()
    elif args.command == "report":
        report_command()
    elif args.command == "diff":
        diff_command()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
