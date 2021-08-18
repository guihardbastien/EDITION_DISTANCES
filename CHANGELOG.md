# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)

## [V1] - 16-03-2021

All 7 questions have been answered, no testing has been done yet.

### Added
- distance 1 function
- distance 2 function
- closer function
- closer_mem function
- lauch_test function
- main function using argparse

### Changed

### Fixed

## [V2] - 30-03-2021

Mainly fixing issues raised in test log
Some issues have voluntaily not been adressed for I found it would make the code hard to maintain

### Added
- MemoisationOpt enum

### Changed
- closer_mem function now refers to enum values 
- documentation is more explicit 

### Fixed
- Unbounded exception was raised with default memoisation, added global dict only referenced to when default
