import math
import numpy as np
import random

treatment_outcome = []  # a
treatment_total_group = []  # a + b
control_outcome = []  # c
control_total_group = []  # c + d

for i in treatment_outcome:
    for j in treatment_total_group:
        for k in control_outcome:
            for o in control_total_group:

                treatment_absent_outcome = treatment_total_group - treatment_outcome  # b
                control_absent_outcome = control_total_group - control_outcome  # d

                treatment_risk = treatment_outcome / treatment_total_group  # a / a+b
                control_risk = control_outcome / control_total_group  # c / c+d

                relative_risk = treatment_risk / control_risk  # (a * (c+d)) / (b *  (a+b))

                relative_risk_reduction = 1 - relative_risk

                absolute_risk_reduction = treatment_risk - control_risk

                NNT = 1 / absolute_risk_reduction

                treatment_odds = treatment_outcome / treatment_absent_outcome  # a/b
                control_odds = control_outcome / control_absent_outcome  # c/d

                odds_ratio = treatment_odds / control_odds  # ad/bc
