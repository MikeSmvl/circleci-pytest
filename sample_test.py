import csv
import urllib.request
import codecs

url = 'https://raw.githubusercontent.com/MikeSmvl/circleci-pytest/master/sample.csv'
ftpstream = urllib.request.urlopen(url)
csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))

def inc(x):
    return x + 1

def test_answer():
  for line in csvfile:
    print(line)
  assert inc(4) == 5
