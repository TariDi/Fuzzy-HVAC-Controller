import numpy as np
import skfuzzy.control as ctrl
import skfuzzy as sf
import Fuzzy_rules as fr
import Fuzzy_variables as fv
import matplotlib.pyplot as plt

system = ctrl.ControlSystem(rules=[fr.rule0, fr.rule1, fr.rule2, fr.rule3,
                                   fr.rule4, fr.rule5, fr.rule6])

sim = ctrl.ControlSystemSimulation(system)

def main():
    fr.output.view()
    fr.error.view()
    fr.rate_change.view()

    f = open("tempreadings", "r")
    while True:
        first = f.readline()
        if first == '':
            break
        reference_temp = float(first)
        #reference_temp = float(input("Enter reference temp"))
        current_temp = float(f.readline())
        past_temp = float(f.readline())
        te = current_temp - reference_temp
        tc = past_temp - current_temp
        sim.input['te'] = te
        sim.input['tc'] = tc
        sim.compute()
        system_output = sim.output['output']
        fr.output.view(sim= sim)
        if system_output < 5 and system_output > -5:
            final_output = 0
        else:
            final_output = np.round(system_output)
        print("Voltage increase to driver for current cycle(%)= "+str(final_output))
        print("\n")
        #plt.show()

if __name__=="__main__":
    main()
    plt.show()




