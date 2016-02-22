import csv
import transaction
import datetime
import numutil

class MoneyLover(transaction.TransactionList):
  def __init__(self, filename):
    with open(filename) as fcsv:
      txns = list(csv.reader(fcsv, delimiter=','))
      self.transactions = sorted(map(self.hydrate, txns[1:]), key=lambda t: t.amount)

  def hydrate(self, row):
    date = datetime.datetime.strptime(row[6],'%d/%m/%Y')
    return transaction.Transaction(date, numutil.parsefloat(row[2]), row[1])

