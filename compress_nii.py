import argparse
from pathlib import Path

from nibabel.loadsave import load, save


def compress_nii(input_file: Path, output_file: Path) -> None:
    img = load(input_file)
    save(img, output_file)


def main():
    parser = argparse.ArgumentParser(
        description="Compress NIfTI files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the input NIfTI file",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        type=Path,
        nargs="?",
        default=None,
        help="Path to the output NIfTI file. By default, same name as input file with different extension",
    )

    # get I/O arguments
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file or input_file.with_suffix(".nii.gz")

    # checks
    assert input_file.exists(), f"Input file {input_file} does not exist"
    assert input_file != output_file, (
        f"Input file {input_file} and output file {output_file} are the same"
    )
    assert output_file.suffix == ".gz"

    # create output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # compress NIfTI file
    print(f"Compressing {input_file} to {output_file}...")
    compress_nii(input_file, output_file)
    print("Compression complete!")


if __name__ == "__main__":
    main()
