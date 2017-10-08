import engineer_number

esv = engineer_number.constants.E_SERIES_VALUES

# tup = (6, 12, 24)
# for n in tup:
#   for i in range(n):
#     v = round(pow(10, i / n), 1)
#     print("10 ** ({} / {}) = {}".format(i, n, v))
#   print()

tup = (48, 96, 192)
L = []
for n in tup:
  for i in range(n):
    v = round(10 * round(pow(10, i / n), 2), 1)
    L.append(v)
  e_series_name = "E{}".format(n)
  bool_ = set(esv[e_series_name]) == set(L)
  print("set[esv[{}]] == set(L) is {}".format(e_series_name, bool_))
  if n == 192:
    st_L = set(L)
    st_L.remove(91.9)
    st_L.add(92.0)
    bool_ = set(esv[e_series_name]) == st_L
    print("set[esv[{}]] == st_L is {}".format(e_series_name, bool_))
    print(set(esv[e_series_name]) - st_L)
    print(st_L - set(esv[e_series_name]))
# set[esv[E48]] == set(L) is True
# set[esv[E96]] == set(L) is True
# set[esv[E192]] == set(L) is False
# {92.0}
# {91.9}
