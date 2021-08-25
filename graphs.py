import matplotlib.pyplot as plt
import numpy as np

# Runtime graph: 1-5 scenarios

w = 0.2
x = ["Scenario1", "Scenario2", "Scenario3", "Scenario4", "Scenario5"]
xbar1 = np.array(x)
xbar2 = [i + w for i in range(len(xbar1))]
xbar3 = [i + 2 * w for i in range(len(xbar1))]
y1_1 = [0.1874370574951172, 0.15621209144592285, 0.25931549072265625,
        0.13866329193115234, 0.1316819190979004]
y1_2 = [0.0, 0.0, 0.00099945068359375, 0.0009615421295166016, 0.0]
y2 = [0.004960060119628906, 0.015620946884155273, 0.031249046325683594,
      0.003992319107055664, 0.015657901763916016]
y3 = [0.001994609832763672, 0.0, 0.015606880187988281, 0.00196075439453125,
      0.0019960403442382812]
plt.bar(xbar1, y1_1, width=w, label="CSP + Qlearning (learning time)")
plt.bar(xbar1, y1_2, width=w, label="CSP + Qlearning (predicting time",
        color="red")
plt.bar(xbar2, y2, width=w, label="CSP + Choose Best Match", color="orange")
plt.bar(xbar3, y3, width=w, label="CSP only (with Random Choice)",
        color="green")
plt.xlabel("Scenarios")
plt.ylabel("Running Time [sec]")
plt.legend()
plt.show()

# Performances - Matching score: 1-5 scenarios
w = 0.2
x = ["Scenario1", "Scenario2", "Scenario3", "Scenario4", "Scenario5"]
xbar1 = np.array(x)
xbar2 = [i + w for i in range(len(xbar1))]
xbar3 = [i + 2 * w for i in range(len(xbar1))]
y1 = [33.0 / 33, 28.000149857635247 / 33, 32.4 / 33, 32.5 / 33,
      33.0 / 33]
y2 = [33.0 / 33, 28.000149857635247 / 33, 32.4 / 33, 32.5 / 33, 33.0 / 33]
y3 = [28.0000153787005 / 33, 22.600071994925194 / 33, 21.800182374788044 / 33,
      23.000101378012506 / 33, 18.000030703619423 / 33]
plt.bar(xbar1, y1, width=w, label="CSP + Qlearning (learning time)")
plt.bar(xbar2, y2, width=w, label="CSP + Choose Best Match", color="orange")
plt.bar(xbar3, y3, width=w, label="CSP only (with Random Choice)",
        color="green")
plt.xlabel("Scenarios")
plt.ylabel("Matching Scores [Percentage]")
plt.legend()
plt.show()
# ##############################################################################
# Runtime graph: 6-10 scenarios

w = 0.2
x = ["Scenario6", "Scenario7", "Scenario8", "Scenario9", "Scenario10"]
xbar1 = np.array(x)
xbar2 = [i + w for i in range(len(xbar1))]
xbar3 = [i + 2 * w for i in range(len(xbar1))]
y1_1 = [0.21869921684265137, 0.24998831748962402, 0.147169828414917,
        0.14055490493774414, 0.20844268798828125]
y1_2 = [0.000997304916381836, 0.0, 0.0, 0.0, 0.0]
y2 = [0.009964704513549805, 0.004986286163330078, 0.015572071075439453,
      0.01562190055847168, 0.010970592498779297]
y3 = [0.004987001419067383, 0.0020275115966796875, 0.0009968280792236328, 0.001972198486328125,
      0.01564764976501465]
plt.bar(xbar1, y1_1, width=w, label="CSP + Qlearning (learning time)")
plt.bar(xbar1, y1_2, width=w, label="CSP + Qlearning (predicting time",
        color="red")
plt.bar(xbar2, y2, width=w, label="CSP + Choose Best Match", color="orange")
plt.bar(xbar3, y3, width=w, label="CSP only (with Random Choice)",
        color="green")
plt.xlabel("Scenarios")
plt.ylabel("Running Time [sec]")
plt.legend()
plt.show()
#
# # Performances - Matching score: 6-10 scenarios
w = 0.2
x = ["Scenario6", "Scenario7", "Scenario8", "Scenario9", "Scenario10"]
xbar1 = np.array(x)
xbar2 = [i + w for i in range(len(xbar1))]
xbar3 = [i + 2 * w for i in range(len(xbar1))]
y1 = [33.0 / 33, 33.0 / 33, 22.687530757401 / 33, 28.000085999312006 / 33,
      32.2 / 33]
y2 = [33.0 / 33, 33.0/ 33, 27.6875153787005 / 33, 28.000085999312006/ 33, 32.2 / 33]
y3 = [28.000149857635247 / 33, 23.00002814050267 / 33, 22.687530757401 / 33,
      18.000041171642 / 33, 18.00006293087182/ 33]
plt.bar(xbar1, y1, width=w, label="CSP + Qlearning (learning time)")
plt.bar(xbar2, y2, width=w, label="CSP + Choose Best Match", color="orange")
plt.bar(xbar3, y3, width=w, label="CSP only (with Random Choice)",
        color="green")
plt.xlabel("Scenarios")
plt.ylabel("Matching Scores [Percentage]")
plt.legend()
plt.show()
##############################################################################
# # Runtime graph: 1-5 (new) scenarios
#
# w = 0.2
# x = ["Scenario1", "Scenario2", "Scenario3", "Scenario4", "Scenario5"]
# xbar1 = np.array(x)
# xbar2 = [i + w for i in range(len(xbar1))]
# xbar3 = [i + 2 * w for i in range(len(xbar1))]
# y1_1 = [0.22536444664001465, 0.2030792236328125, 0.5335988998413086,
#         0.17186784744262695, 0.23435258865356445]
# y1_2 = [0.0, 0.0, 0.0, 0.0, 0.0]
# y2 = [0.0, 0.010971307754516602, 0.04683804512023926,
#       0.005986213684082031, 0.015657901763916016]
# y3 = [0.0, 0.0, 0.015611648559570312, 0.0 ,
#       0.005984067916870117]
# plt.bar(xbar1, y1_1, width=w, label="CSP + Qlearning (learning time)")
# plt.bar(xbar1, y1_2, width=w, label="CSP + Qlearning (predicting time",
#         color="red")
# plt.bar(xbar2, y2, width=w, label="CSP + Choose Best Match", color="orange")
# plt.bar(xbar3, y3, width=w, label="CSP only (with Random Choice)",
#         color="green")
# plt.xlabel("Scenarios")
# plt.ylabel("Running Time [sec]")
# plt.legend()
# plt.show()
#
# # Performances - Matching score: 6-10 (new) scenarios
# w = 0.2
# x = ["Scenario1", "Scenario2", "Scenario3", "Scenario4", "Scenario5"]
# xbar1 = np.array(x)
# xbar2 = [i + w for i in range(len(xbar1))]
# xbar3 = [i + 2 * w for i in range(len(xbar1))]
# y1 = [33.0 / 33, 28.000149857635247 / 33, 28.000085999312006 / 33, 32.5 / 33,
#       33.0 / 33]
# y2 = [33.0 / 33, 33.0 / 33, 32.4 / 33, 32.5 / 33, 33.0 / 33]
# y3 = [28.0000051262335 / 33, 28.000006988217866 / 33, 27.4000153787005 / 33,
#       23.00001281558375 / 33, 28.0000051262335 / 33]
# plt.bar(xbar1, y1, width=w, label="CSP + Qlearning (learning time)")
# plt.bar(xbar2, y2, width=w, label="CSP + Choose Best Match", color="orange")
# plt.bar(xbar3, y3, width=w, label="CSP only (with Random Choice)",
#         color="green")
# plt.xlabel("Scenarios")
# plt.ylabel("Matching Scores [Percentage]")
# plt.legend()
# plt.show()


