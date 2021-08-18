# EDITION_DISTANCES

## Description

Script able to find edition distance between two strings

## Overview

### Directory structure

```bash
.
├── CHANGELOG.md
├── README.md
├── renommage_series.py
├── series_2000-2019.txt
└── tests
    └── tests_v1_tp2.md
```

### Features



### How to use ?
```bash
python renommage_series.py  --memoisation "global" series_2000-2019.txt "ternell"
# or
python renommage_series.py  --memoisation "global" --question 7a series_2000-2019.txt "ternell"
```

```bash
usage: renommage_series.py [-h]
                           [--memoisation <none | default | by_arg  | by_target | global>]
                           [--test <test_index>]
                           [--memo-file <path_to_memoisation_file>]
                           [--question <answer_index>]
                           path titles [titles ...]

Find closest title

positional arguments:
  path                  Absolute path to the file you want to test
  titles                List of titles you want to find.ex: python
                        renommage_series.py assets/series_2000-2019.txt "12
                        Mon" "ternell"...

optional arguments:
  -h, --help            show this help message and exit
  --memoisation <none | default | by_arg  | by_target | global>
                        Set memoisation (--memoisation none,i --memoisation
                        by_target, by_arg --memoisation default, --memoisation
                        global)
  --test <test_index>   --test 0 launches a basic test--test 1 launches.. TBA
  --memo-file <path_to_memoisation_file>
                        --memo-file ./<file_name>
  --question <answer_index>
                        --question 7a | 7b
```

## Other/Optional considerations

Please follow the folowing template for tests:

```
 # Report X

 ## Id: #X

 **Title:** Template

 **Version:** VX.X

 **Category:** XXX XXX

 **Priority:** [1, 2, 3, 4]

 **Description:** Lorem ipsum

 -------------------------------------------------------------------------------
```

## Ressources

- https://docs.python.org/3/library/argparse.html#module-argparse

