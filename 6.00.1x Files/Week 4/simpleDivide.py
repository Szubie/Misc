def SimpleDivide(item, denom):
    try:
      item / denom
    except ZeroDivisionError, e:
        return 0
    else:
        return item/denom