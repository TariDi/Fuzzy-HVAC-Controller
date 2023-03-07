import numpy as np
import skfuzzy.control as ctrl
import skfuzzy as sf


temp = np.linspace(-2.0, 2.0, num=7)
negative = np.linspace(-25.4, -2.0)
positive = np.linspace(2.0, 25.4)
antecedent_universe = np.union1d(np.union1d(temp, negative), positive)
consequent_universe = np.linspace(-15, 15, num=7)


class FVariable(object):

    def __init__(self):
        self.te = ctrl.Antecedent(antecedent_universe, 'te')
        self.tc = ctrl.Antecedent(antecedent_universe, 'tc')
        self.output = ctrl.Consequent(consequent_universe, 'output')



    def set_mf(self):
        self.te['NL'] = self.tc['NL'] = sf.membership.trapmf(antecedent_universe, [-25.4, -25.4, -2.0, -1.333])
        self.te['NM'] = self.tc['NM'] = sf.membership.trimf(antecedent_universe, [-2.0, -1.333, -0.667])
        self.te['NS'] = self.tc['NS'] = sf.membership.trimf(antecedent_universe, [-1.333, -0.667, 0])
        self.te['ZR'] = self.tc['ZR'] = sf.membership.trimf(antecedent_universe, [-0.667, 0, 0.667])
        self.te['PS'] = self.tc['PS'] = sf.membership.trimf(antecedent_universe, [0, 0.667, 1.333])
        self.te['PM'] = self.tc['PM'] = sf.membership.trimf(antecedent_universe, [0.667, 1.333, 2.0])
        self.te['PL'] = self.tc['PL'] = sf.membership.trapmf(antecedent_universe, [1.333, 2.0, 25.4, 25.4])

        self.output['NL'] = sf.membership.trimf(consequent_universe, [-15, -15, -10])
        self.output['NM'] = sf.membership.trimf(consequent_universe, [-15, -10, -5])
        self.output['NS'] = sf.membership.trimf(consequent_universe, [-10, -5, 0])
        self.output['ZR'] = sf.membership.trimf(consequent_universe, [-5, 0, 5])
        self.output['PS'] = sf.membership.trimf(consequent_universe, [0, 5, 10])
        self.output['PM'] = sf.membership.trimf(consequent_universe, [5, 10, 15])
        self.output['PL'] = sf.membership.trimf(consequent_universe, [10, 15, 15])


    def get_te(self):
        return self.te

    def get_tc(self):
        return self.tc

    def get_output(self):
        return self.output

    def show(self):
        self.te.view()
        self.tc.view()
        self.output.view()










