# 1BRC: One Billion Row Challenge in Python (using DuckDB)

Python + DuckDB implementation of Gunnar's 1 billion row challenge:
- https://www.morling.dev/blog/one-billion-row-challenge
- https://github.com/gunnarmorling/1brc

## Creating the measurements file with 1B rows

First install the Python requirements:
```shell
python3 -m pip install -r requirements.txt
```

The script `createMeasurements.py` will create the measurement file:
```
usage: createMeasurements.py [-h] [-o OUTPUT] [-r RECORDS]

Create measurement file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Measurement file name (default is "measurements.txt")
  -r RECORDS, --records RECORDS
                        Number of records to create (default is 1_000_000_000)
```

Example:
```
% python3 createMeasurements.py
Creating measurement file 'measurements.txt' with 1,000,000,000 measurements...
100%|█████████████████████████████████████████| 100/100 [01:15<00:00,  1.32it/s]
Created file 'measurements.txt' with 1,000,000,000 measurements in 75.86 seconds
```

Be patient as it can take more than a minute to have the file generated.

Maybe as another challenge is to speed up the generation of the measurements file :slightly_smiling_face:

## Running the script
To run the script on the full dataset
```bash
./run
```

To run the script on a subset of the full dataset
```bash
./run 100 # runs the script on the first 100 rows of the dataset
```
`./run` executes the 1brc.py script with optional command line arguments.\
If no argument is provided, it runs the 1brc.py script with the default input file "measurements.txt".\
If an argument is provided, it creates a temporary file with the specified number of rows from "measurements.txt", runs the 1brc.py script with the temporary file as input, and then deletes the temporary file.
