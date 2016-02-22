import argparse
import datetime
from equilibrium import moneylover
from equilibrium.banks import Citibank, BankofAmerica

parser = argparse.ArgumentParser(description="Restore balance to MoneyLover")
parser.add_argument('--money_lover', metavar='M')
parser.add_argument('--bank', metavar='B')
parser.add_argument('--transactions', metavar='T')
parser.add_argument('--start', metavar='T')
parser.add_argument('--end', metavar='T')

args = parser.parse_args()


def compare(mlover, bank, start, end):
  mtxns = mlover.get_transactions(start=start, end=end)
  btxns = bank.get_transactions(start=start, end=end)

  print("%d from MoneyLover, %d from bank" % (len(mtxns), len(btxns)))

  mdiff = list()
  bdiff = list()

  while(len(mtxns) > 0 and len(btxns) > 0):
    if (mtxns[0].amount == btxns[0].amount):
      mtxns.pop(0)
      btxns.pop(0)
      continue
    elif (mtxns[0].amount < btxns[0].amount):
      mdiff.append(mtxns.pop(0))
    else:
      bdiff.append(btxns.pop(0))

  print 'Output:'
  print 'There are %d items in MoneyLover that are not present in transactions' % len(mdiff)
  print_txns(mdiff)
  print ''
  print 'There are %d transactions that arent on MoneyLover' % len(bdiff)
  print_txns(bdiff)
  print ''

def print_txns(txns):
  lines = ['%.02f - %s on %s' % (t.amount, t.to, t.date) for t in txns]
  for l in lines:
    print ' ', l


if __name__ == '__main__':

  mlover = moneylover.MoneyLover(args.money_lover)
  if args.bank == 'citibank':
    bank = Citibank(args.transactions)
  elif args.bank == 'boa':
    bank = BankofAmerica(args.transactions)
  else:
    raise ValueError('Unrecognized bank source')

  start = None
  end = None

  if (len(args.start) > 0):
    start = datetime.datetime.strptime(args.start, '%Y-%m-%d')

  if (len(args.end) > 0):
    end = datetime.datetime.strptime(args.end, '%Y-%m-%d')

  compare(mlover, bank, start, end)
