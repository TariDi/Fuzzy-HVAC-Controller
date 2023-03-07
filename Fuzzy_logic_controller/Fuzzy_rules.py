import numpy as np
import skfuzzy.control as ctrl
import Fuzzy_variables as fv


variables = fv.FVariable()
variables.set_mf()
error = variables.get_te()
rate_change = variables.get_tc()
output = variables.get_output()


rule0 = ctrl.Rule(antecedent=((error['NM'] & rate_change['NM']) |
                              (error['NL'] & rate_change['ZR'])),
                  consequent=output['NL'], label='rule NL')

rule1 = ctrl.Rule(antecedent=((error['NS'] & rate_change['NS']) |
                              (error['NM'] & rate_change['ZR'])),
                  consequent=output['NM'], label='rule NM')

rule2 = ctrl.Rule(antecedent=((error['ZR'] & rate_change['NS']) |
                              (error['NS'] & rate_change['ZR'])),
                  consequent=output['NS'], label='rule NS')

rule3 = ctrl.Rule(antecedent=((error['PS'] & rate_change['NS']) |
                              (error['ZR'] & rate_change['ZR']) |
                              (error['NS'] & rate_change['PS'])),
                  consequent=output['ZR'], label='rule ZR')

rule4 = ctrl.Rule(antecedent=((error['PS'] & rate_change['ZR']) |
                              (error['ZR'] & rate_change['PS'])),
                  consequent=output['PS'], label='rule PS')

rule5 = ctrl.Rule(antecedent=((error['PM'] & rate_change['ZR']) |
                              (error['PS'] & rate_change['PS'])),
                  consequent=output['PM'], label='rule PM')

rule6 = ctrl.Rule(antecedent=((error['PL'] & rate_change['ZR']) |
                              (error['PM'] & rate_change['PM'])),
                  consequent=output['PL'], label='rule PL')


