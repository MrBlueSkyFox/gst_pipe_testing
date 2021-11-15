import argparse
import os
import subprocess
import sys
from pathlib import Path

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument(
    "-i", "--input_dir", default="test_1", help="Input dir where gst .dot files"
)
parser.add_argument(
    "-o",
    "--output_dir",
    default="test_1_out",
    help="Output dir where gst pipe will be png converted",
)
args = parser.parse_args()
if not os.path.exists(args.input_dir):
    print(f"Dir input: {args.input_dir} doesn't exist!")
    print("aborting")
    sys.exit()

Path(args.output_dir).mkdir(parents=True, exist_ok=True)

print(f"Dir input: {args.input_dir} ")
print(f"Dir output: {args.output_dir} ")

MAIN_DIR = os.getcwd()
entries = os.scandir(args.input_dir)
for dor_file_name in entries:
    name = dor_file_name.name
    path_from = os.path.join(MAIN_DIR, args.input_dir, name)
    out_name = name.replace("dot", "png")
    path_to = os.path.join(MAIN_DIR, args.output_dir, out_name)
    bashCommand = f"dot -Tpng {path_from} -o {path_to}"
    print(f"Bash command :{bashCommand}")
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
