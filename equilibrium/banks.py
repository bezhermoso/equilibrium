import transaction
import csv
import numutil
import datetime

class Bank(transaction.TransactionList):
  def __init__(self, filename):
    with open(filename) as fcsv:
      txns = list(csv.reader(fcsv, **self.csvOptions()))
      self.transactions = sorted(map(self.hydrate, txns[7:]), key=lambda t: t.amount)

  def csvOptions(self):
    return dict(delimiter=',')

  def hydrate(self, row):
    raise TypeError('hydrate method is not overidden.')
    pass

class Citibank(Bank):
  def hydrate(self, row):
    date = datetime.datetime.strptime(row[1], '%m/%d/%Y')
    if len(row[3]) > 0:
      amt = 0 - numutil.parsefloat(row[3])
    else:
      amt = numutil.parsefloat(row[4])
    return transaction.Transaction(date, amt, row[2])

class BankofAmerica(Bank):
  def hydrate(self, row):
    date = datetime.datetime.strptime(row[0], '%m/%d/%Y')
    if len(row[2]) > 0:
      amt = numutil.parsefloat(row[2])
    else:
      amt = 0 - numutil.parsefloat(row[3])
    return transaction.Transaction(date, amt, row[1])
