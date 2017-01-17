# Open Syllabus Project Spiders
=========================================================
Specialty Spiders for those hard-to-reach databases
Written by Jonathan Lesser for the Open Syllabus Project
=========================================================

Last update: January 16, 2017

*This readme will primarily serve as a place to document which spiders are completed and which are in progress

HCCS - functioning
TAMU - in progress
UTexas - in progress
Lonestar - in progress

UFL - marked as easy, created for practice

ASU - functioning
UCF - not necessary
PSU - functioning

## Getting started
Create a Python 3 environment and initialize it
```
python3 -m venv env
```
This needs to be done every time you open a new terminal
```
source env/bin/activate
```
Install Scrapy
```
pip install scrapy
```
Install Syllascrape
```
cd ..
git clone https://github.com/wearpants/syllascrape.git
python syllascrape/setup.py install
```