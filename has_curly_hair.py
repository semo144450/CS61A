"""
This function should only return True
if both the father allele and the mother allele are "C".
"""
def has_curly_hair(father_allele, mother_allele):
  """
  >>> has_curly_hair("C", "c")
  False
  >>> has_curly_hair("c", "C")
  False
  >>> has_curly_hair("s", "s")
  False
  >>> has_curly_hair("C", "C")
  True
  """
  return (father_allele == 'C') and (mother_allele == 'C')