
"""
    Даны формулы: ¬((A ∨ B) ∧ (C ∨ D)) и ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)).
    Используя закон Де Моргана, докажите, что эти формулы эквивалентны.

    ¬((A ∨ B) ∧ (C ∨ D)) =
    not ((A or B) and (C or D)) =
    not (A or B) or not (C or D) =
    (not A and not B) or (not C and not D) =
    (¬A ∧ ¬B) ∨ (¬C ∧ ¬D)
"""
A = True
B = False
C = True
D = False

print((not ((A or B) and (C or D))) == (not A and not B) or (not C and not D))
