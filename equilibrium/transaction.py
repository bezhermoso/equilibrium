
def date_filter(start, end):
  def f(txn):
    ok = True
    if start is not None:
      ok = (start <= txn.date) and ok
    if end is not None:
      ok = (end >= txn.date) and ok
    return ok
  return f

class TransactionList(object):
  def __init__(self):
    raise TypeError('This must be subclassed.')

  def get_transactions(self, start=None, end=None):
    return filter(date_filter(start, end), self.transactions)

class Transaction(object):
  def __init__(self, date, amount, to, description=None):
    self.date = date
    self.amount = amount
    self.to = to
    self.description = description


