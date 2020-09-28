from pulp import*

#1
prob1 = LpProblem("OR_FINAL", pulp.LpMaximize)
Dest1 = ['X1_1', 'X2_1', 'X3_1','X4_1','X5_1','X6_1','X7_1','X1_2', 'X2_2', 'X3_2','X4_2','X5_2','X6_2','X7_2','X1_3', 'X2_3', 'X3_3','X4_3','X5_3','X6_3','X7_3']
costs1 = {'X1_1':35, 'X2_1':35, 'X3_1':35,'X4_1':23,'X5_1':42,'X6_1':32,'X7_1':20,'X1_2':45, 'X2_2':43, 'X3_2':45,'X4_2':33,'X5_2':32,'X6_2':22,'X7_2':30
          ,'X1_3':0, 'X2_3':0, 'X3_3':0,'X4_3':43,'X5_3':22,'X6_3':42,'X7_3':40}
x1_1 = {'X1_1':1, 'X2_1':1, 'X3_1':1,'X4_1':1,'X5_1':1,'X6_1':1,'X7_1':1,'X1_2':0, 'X2_2':0, 'X3_2':0,'X4_2':0,'X5_2':0,'X6_2':0,'X7_2':0
          ,'X1_3':0, 'X2_3':0, 'X3_3':0,'X4_3':0,'X5_3':0,'X6_3':0,'X7_3':0}
x1_2 = {'X1_1':0, 'X2_1':0, 'X3_1':0,'X4_1':0,'X5_1':0,'X6_1':0,'X7_1':0,'X1_2':1, 'X2_2':1, 'X3_2':1,'X4_2':1,'X5_2':1,'X6_2':1,'X7_2':1
          ,'X1_3':0, 'X2_3':0, 'X3_3':0,'X4_3':0,'X5_3':0,'X6_3':0,'X7_3':0}
x1_3 = {'X1_1':0, 'X2_1':0, 'X3_1':0,'X4_1':0,'X5_1':0,'X6_1':0,'X7_1':0,'X1_2':0, 'X2_2':0, 'X3_2':0,'X4_2':0,'X5_2':0,'X6_2':0,'X7_2':0
          ,'X1_3':1, 'X2_3':1, 'X3_3':1,'X4_3':1,'X5_3':1,'X6_3':1,'X7_3':1}

y1_1 = {'X1_1':1, 'X2_1':0, 'X3_1':0,'X4_1':0,'X5_1':0,'X6_1':0,'X7_1':0,'X1_2':1, 'X2_2':0, 'X3_2':0,'X4_2':0,'X5_2':0,'X6_2':0,'X7_2':0
          ,'X1_3':1, 'X2_3':0, 'X3_3':0,'X4_3':0,'X5_3':0,'X6_3':0,'X7_3':0}
y1_2 = {'X1_1':0, 'X2_1':1, 'X3_1':0,'X4_1':0,'X5_1':0,'X6_1':0,'X7_1':0,'X1_2':0, 'X2_2':1, 'X3_2':0,'X4_2':0,'X5_2':0,'X6_2':0,'X7_2':0
          ,'X1_3':0, 'X2_3':1, 'X3_3':0,'X4_3':0,'X5_3':0,'X6_3':0,'X7_3':0}
y1_3 = {'X1_1':0, 'X2_1':0, 'X3_1':1,'X4_1':0,'X5_1':0,'X6_1':0,'X7_1':0,'X1_2':0, 'X2_2':0, 'X3_2':1,'X4_2':0,'X5_2':0,'X6_2':0,'X7_2':0
          ,'X1_3':0, 'X2_3':0, 'X3_3':1,'X4_3':0,'X5_3':0,'X6_3':0,'X7_3':0}
y1_4 = {'X1_1':0, 'X2_1':0, 'X3_1':0,'X4_1':1,'X5_1':0,'X6_1':0,'X7_1':0,'X1_2':0, 'X2_2':0, 'X3_2':0,'X4_2':1,'X5_2':0,'X6_2':0,'X7_2':0
          ,'X1_3':0, 'X2_3':0, 'X3_3':0,'X4_3':1,'X5_3':0,'X6_3':0,'X7_3':0}
y1_5 = {'X1_1':0, 'X2_1':0, 'X3_1':0,'X4_1':0,'X5_1':1,'X6_1':0,'X7_1':0,'X1_2':0, 'X2_2':0, 'X3_2':0,'X4_2':0,'X5_2':1,'X6_2':0,'X7_2':0
          ,'X1_3':0, 'X2_3':0, 'X3_3':0,'X4_3':0,'X5_3':1,'X6_3':0,'X7_3':0}
y1_6 = {'X1_1':0, 'X2_1':0, 'X3_1':1,'X4_1':0,'X5_1':0,'X6_1':1,'X7_1':0,'X1_2':0, 'X2_2':0, 'X3_2':0,'X4_2':0,'X5_2':0,'X6_2':1,'X7_2':0
          ,'X1_3':0, 'X2_3':0, 'X3_3':0,'X4_3':0,'X5_3':0,'X6_3':1,'X7_3':0}
y1_7 = {'X1_1':0, 'X2_1':0, 'X3_1':0,'X4_1':0,'X5_1':0,'X6_1':0,'X7_1':1,'X1_2':0, 'X2_2':0, 'X3_2':0,'X4_2':0,'X5_2':0,'X6_2':0,'X7_2':1
          ,'X1_3':0, 'X2_3':0, 'X3_3':0,'X4_3':0,'X5_3':0,'X6_3':0,'X7_3':1}


dest1_vars = LpVariable.dicts("Dest1",Dest1,0)
prob1 += lpSum([costs1[i]*dest1_vars[i] for i in Dest1])

prob1 += lpSum([x1_1[i] * dest1_vars[i] for i in Dest1]) ==1
prob1 += lpSum([x1_2[i] * dest1_vars[i] for i in Dest1]) ==1
prob1 += lpSum([x1_3[i] * dest1_vars[i] for i in Dest1]) ==1

prob1 += lpSum([y1_1[i] * dest1_vars[i] for i in Dest1]) <=1
prob1 += lpSum([y1_2[i] * dest1_vars[i] for i in Dest1]) <=1
prob1 += lpSum([y1_3[i] * dest1_vars[i] for i in Dest1]) <=1
prob1 += lpSum([y1_4[i] * dest1_vars[i] for i in Dest1]) <=1
prob1 += lpSum([y1_5[i] * dest1_vars[i] for i in Dest1]) <=1
prob1 += lpSum([y1_6[i] * dest1_vars[i] for i in Dest1]) <=1
prob1 += lpSum([y1_7[i] * dest1_vars[i] for i in Dest1]) <=1

prob1 += lpSum([y1_1[i] * dest1_vars[i] for i in Dest1]) >=0
prob1 += lpSum([y1_2[i] * dest1_vars[i] for i in Dest1]) >=0
prob1 += lpSum([y1_3[i] * dest1_vars[i] for i in Dest1]) >=0
prob1 += lpSum([y1_4[i] * dest1_vars[i] for i in Dest1]) >=0
prob1 += lpSum([y1_5[i] * dest1_vars[i] for i in Dest1]) >=0
prob1 += lpSum([y1_6[i] * dest1_vars[i] for i in Dest1]) >=0
prob1 += lpSum([y1_7[i] * dest1_vars[i] for i in Dest1]) >=0


prob1.solve()
for v in prob1.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print('obj1=',value(prob1.objective))
print("")

#2
prob2 = LpProblem("OR_FINAL", pulp.LpMaximize)
Dest2 = ['X8_1', 'X9_1', 'X10_1','X11_1','X12_1','X13_1','X8_2', 'X9_2', 'X10_2','X11_2','X12_2','X13_2','X8_3', 'X9_3', 'X10_3','X11_3','X12_3','X13_3']
costs2 = {'X8_1':43, 'X9_1':43, 'X10_1':46,'X11_1':32,'X12_1':28,'X13_1':0,'X8_2':33, 'X9_2':33, 'X10_2':36,'X11_2':22,'X12_2':38,'X13_2':41,
          'X8_3':23, 'X9_3':23, 'X10_3':26,'X11_3':42,'X12_3':18,'X13_3':31}
x2_1 = {'X8_1':1, 'X9_1':1, 'X10_1':1,'X11_1':1,'X12_1':1,'X13_1':1,'X8_2':0, 'X9_2':0, 'X10_2':0,'X11_2':0,'X12_2':0,'X13_2':0,
          'X8_3':0, 'X9_3':0, 'X10_3':0,'X11_3':0,'X12_3':0,'X13_3':0}
x2_2 = {'X8_1':0, 'X9_1':0, 'X10_1':0,'X11_1':0,'X12_1':0,'X13_1':0,'X8_2':1, 'X9_2':1, 'X10_2':1,'X11_2':1,'X12_2':1,'X13_2':1,
          'X8_3':0, 'X9_3':0, 'X10_3':0,'X11_3':0,'X12_3':0,'X13_3':0}
x2_3 = {'X8_1':0, 'X9_1':0, 'X10_1':0,'X11_1':0,'X12_1':0,'X13_1':0,'X8_2':0, 'X9_2':0, 'X10_2':0,'X11_2':0,'X12_2':0,'X13_2':0,
          'X8_3':1, 'X9_3':1, 'X10_3':1,'X11_3':1,'X12_3':1,'X13_3':1}

y2_1 = {'X8_1':1, 'X9_1':0, 'X10_1':0,'X11_1':0,'X12_1':0,'X13_1':0,'X8_2':1, 'X9_2':0, 'X10_2':0,'X11_2':0,'X12_2':0,'X13_2':0,
          'X8_3':1, 'X9_3':0, 'X10_3':0,'X11_3':0,'X12_3':0,'X13_3':0}
y2_2 = {'X8_1':0, 'X9_1':1, 'X10_1':0,'X11_1':0,'X12_1':0,'X13_1':0,'X8_2':0, 'X9_2':1, 'X10_2':0,'X11_2':0,'X12_2':0,'X13_2':0,
          'X8_3':0, 'X9_3':1, 'X10_3':0,'X11_3':0,'X12_3':0,'X13_3':0}
y2_3 = {'X8_1':0, 'X9_1':0, 'X10_1':1,'X11_1':0,'X12_1':0,'X13_1':0,'X8_2':0, 'X9_2':0, 'X10_2':1,'X11_2':0,'X12_2':0,'X13_2':0,
          'X8_3':0, 'X9_3':0, 'X10_3':1,'X11_3':0,'X12_3':0,'X13_3':0}
y2_4 = {'X8_1':0, 'X9_1':0, 'X10_1':0,'X11_1':1,'X12_1':0,'X13_1':0,'X8_2':0, 'X9_2':0, 'X10_2':0,'X11_2':1,'X12_2':0,'X13_2':0,
          'X8_3':0, 'X9_3':0, 'X10_3':0,'X11_3':1,'X12_3':0,'X13_3':0}
y2_5 = {'X8_1':0, 'X9_1':0, 'X10_1':0,'X11_1':0,'X12_1':1,'X13_1':0,'X8_2':0, 'X9_2':0, 'X10_2':0,'X11_2':0,'X12_2':1,'X13_2':0,
          'X8_3':0, 'X9_3':0, 'X10_3':0,'X11_3':0,'X12_3':1,'X13_3':0}
y2_6 = {'X8_1':0, 'X9_1':0, 'X10_1':0,'X11_1':0,'X12_1':0,'X13_1':1,'X8_2':0, 'X9_2':0, 'X10_2':0,'X11_2':0,'X12_2':0,'X13_2':1,
          'X8_3':0, 'X9_3':0, 'X10_3':0,'X11_3':0,'X12_3':0,'X13_3':1}

dest2_vars = LpVariable.dicts("Dest2",Dest2,0)
prob2 += lpSum([costs2[i]*dest2_vars[i] for i in Dest2])

prob2 += lpSum([x2_1[i] * dest2_vars[i] for i in Dest2]) ==1
prob2 += lpSum([x2_2[i] * dest2_vars[i] for i in Dest2]) ==1
prob2 += lpSum([x2_3[i] * dest2_vars[i] for i in Dest2]) ==1

prob2 += lpSum([y2_1[i] * dest2_vars[i] for i in Dest2]) <=1
prob2 += lpSum([y2_2[i] * dest2_vars[i] for i in Dest2]) <=1
prob2 += lpSum([y2_3[i] * dest2_vars[i] for i in Dest2]) <=1
prob2 += lpSum([y2_4[i] * dest2_vars[i] for i in Dest2]) <=1
prob2 += lpSum([y2_5[i] * dest2_vars[i] for i in Dest2]) <=1
prob2 += lpSum([y2_6[i] * dest2_vars[i] for i in Dest2]) <=1

prob2 += lpSum([y2_1[i] * dest2_vars[i] for i in Dest2]) >=0
prob2 += lpSum([y2_2[i] * dest2_vars[i] for i in Dest2]) >=0
prob2 += lpSum([y2_3[i] * dest2_vars[i] for i in Dest2]) >=0
prob2 += lpSum([y2_4[i] * dest2_vars[i] for i in Dest2]) >=0
prob2 += lpSum([y2_5[i] * dest2_vars[i] for i in Dest2]) >=0
prob2 += lpSum([y2_6[i] * dest2_vars[i] for i in Dest2]) >=0

prob2.solve()
for v in prob2.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print('obj2=',value(prob2.objective))
print("")
#3
prob3 = LpProblem("OR_FINAL", pulp.LpMaximize)
Dest3 = ['X14_1', 'X15_1', 'X16_1','X17_1','X14_2', 'X15_2', 'X16_2','X17_2','X14_3', 'X15_3', 'X16_3','X17_3']
costs3 = {'X14_1':43, 'X15_1':26, 'X16_1':23,'X17_1':0,'X14_2':33, 'X15_2':46, 'X16_2':33,'X17_2':0,'X14_3':23, 'X15_3':36, 'X16_3':43,'X17_3':42}
x3_1 = {'X14_1':1, 'X15_1':1, 'X16_1':1,'X17_1':1,'X14_2':0, 'X15_2':0, 'X16_2':0,'X17_2':0,'X14_3':0, 'X15_3':0, 'X16_3':0,'X17_3':0}
x3_2 = {'X14_1':0, 'X15_1':0, 'X16_1':0,'X17_1':0,'X14_2':1, 'X15_2':1, 'X16_2':1,'X17_2':1,'X14_3':0, 'X15_3':0, 'X16_3':0,'X17_3':0}
x3_3 = {'X14_1':0, 'X15_1':0, 'X16_1':0,'X17_1':0,'X14_2':0, 'X15_2':0, 'X16_2':0,'X17_2':0,'X14_3':1, 'X15_3':1, 'X16_3':1,'X17_3':1}

y3_1 = {'X14_1':1, 'X15_1':0, 'X16_1':0,'X17_1':0,'X14_2':1, 'X15_2':0, 'X16_2':0,'X17_2':0,'X14_3':1, 'X15_3':0, 'X16_3':0,'X17_3':0}
y3_2 = {'X14_1':0, 'X15_1':1, 'X16_1':0,'X17_1':0,'X14_2':0, 'X15_2':1, 'X16_2':0,'X17_2':0,'X14_3':0, 'X15_3':1, 'X16_3':0,'X17_3':0}
y3_3 = {'X14_1':0, 'X15_1':0, 'X16_1':1,'X17_1':0,'X14_2':0, 'X15_2':0, 'X16_2':1,'X17_2':0,'X14_3':0, 'X15_3':0, 'X16_3':1,'X17_3':0}
y3_4 = {'X14_1':0, 'X15_1':0, 'X16_1':0,'X17_1':1,'X14_2':0, 'X15_2':0, 'X16_2':0,'X17_2':1,'X14_3':0, 'X15_3':0, 'X16_3':0,'X17_3':1}

dest3_vars = LpVariable.dicts("Dest3",Dest3,0)
prob3 += lpSum([costs3[i]*dest3_vars[i] for i in Dest3])

prob3 += lpSum([x3_1[i] * dest3_vars[i] for i in Dest3]) ==1
prob3 += lpSum([x3_2[i] * dest3_vars[i] for i in Dest3]) ==1
prob3 += lpSum([x3_3[i] * dest3_vars[i] for i in Dest3]) ==1

prob3 += lpSum([y3_1[i] * dest3_vars[i] for i in Dest3]) <=1
prob3 += lpSum([y3_2[i] * dest3_vars[i] for i in Dest3]) <=1
prob3 += lpSum([y3_3[i] * dest3_vars[i] for i in Dest3]) <=1
prob3 += lpSum([y3_4[i] * dest3_vars[i] for i in Dest3]) <=1

prob3 += lpSum([y3_1[i] * dest3_vars[i] for i in Dest3]) >=0
prob3 += lpSum([y3_2[i] * dest3_vars[i] for i in Dest3]) >=0
prob3 += lpSum([y3_3[i] * dest3_vars[i] for i in Dest3]) >=0
prob3 += lpSum([y3_4[i] * dest3_vars[i] for i in Dest3]) >=0

prob3.solve()
for v in prob3.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print('obj3=',value(prob3.objective))
print("")
#4
prob4 = LpProblem("OR_FINAL", pulp.LpMaximize)
Dest4 = ['X18_1', 'X19_1', 'X20_1','X21_1','X22_1','X23_1','X18_2', 'X19_2', 'X20_2','X21_2','X22_2','X23_2','X18_3', 'X19_3', 'X20_3','X21_3','X22_3','X23_3']
costs4 = {'X18_1':37, 'X19_1':42, 'X20_1':42,'X21_1':22,'X22_1':39,'X23_1':26,'X18_2':27, 'X19_2':32, 'X20_2':32,'X21_2':42,'X22_2':29,'X23_2':46,
          'X18_3':0, 'X19_3':0, 'X20_3':0,'X21_3':32,'X22_3':19,'X23_3':36}
x4_1 = {'X18_1':1, 'X19_1':1, 'X20_1':1,'X21_1':1,'X22_1':1,'X23_1':1,'X18_2':0, 'X19_2':0, 'X20_2':0,'X21_2':0,'X22_2':0,'X23_2':0,
          'X18_3':0, 'X19_3':0, 'X20_3':0,'X21_3':0,'X22_3':0,'X23_3':0}
x4_2 = {'X18_1':0, 'X19_1':0, 'X20_1':0,'X21_1':0,'X22_1':0,'X23_1':0,'X18_2':1, 'X19_2':1, 'X20_2':1,'X21_2':1,'X22_2':1,'X23_2':1,
          'X18_3':0, 'X19_3':0, 'X20_3':0,'X21_3':0,'X22_3':0,'X23_3':0}
x4_3 = {'X18_1':0, 'X19_1':0, 'X20_1':0,'X21_1':0,'X22_1':0,'X23_1':0,'X18_2':0, 'X19_2':0, 'X20_2':0,'X21_2':0,'X22_2':0,'X23_2':0,
          'X18_3':1, 'X19_3':1, 'X20_3':1,'X21_3':1,'X22_3':1,'X23_3':1}

y4_1 = {'X18_1':1, 'X19_1':0, 'X20_1':0,'X21_1':0,'X22_1':0,'X23_1':0,'X18_2':1, 'X19_2':0, 'X20_2':0,'X21_2':0,'X22_2':0,'X23_2':0,
          'X18_3':0, 'X19_3':0, 'X20_3':0,'X21_3':0,'X22_3':0,'X23_3':0}
y4_2 = {'X18_1':0, 'X19_1':1, 'X20_1':0,'X21_1':0,'X22_1':0,'X23_1':0,'X18_2':0, 'X19_2':1, 'X20_2':0,'X21_2':0,'X22_2':0,'X23_2':0,
          'X18_3':0, 'X19_3':1, 'X20_3':0,'X21_3':0,'X22_3':0,'X23_3':0}
y4_3 = {'X18_1':0, 'X19_1':0, 'X20_1':1,'X21_1':0,'X22_1':0,'X23_1':0,'X18_2':0, 'X19_2':0, 'X20_2':1,'X21_2':0,'X22_2':0,'X23_2':0,
          'X18_3':0, 'X19_3':0, 'X20_3':1,'X21_3':0,'X22_3':0,'X23_3':0}
y4_4 = {'X18_1':0, 'X19_1':0, 'X20_1':0,'X21_1':1,'X22_1':0,'X23_1':0,'X18_2':0, 'X19_2':0, 'X20_2':0,'X21_2':1,'X22_2':0,'X23_2':0,
          'X18_3':0, 'X19_3':0, 'X20_3':0,'X21_3':1,'X22_3':0,'X23_3':0}
y4_5 = {'X18_1':0, 'X19_1':0, 'X20_1':0,'X21_1':0,'X22_1':1,'X23_1':0,'X18_2':0, 'X19_2':0, 'X20_2':0,'X21_2':0,'X22_2':1,'X23_2':0,
          'X18_3':0, 'X19_3':0, 'X20_3':0,'X21_3':0,'X22_3':1,'X23_3':0}
y4_6 = {'X18_1':0, 'X19_1':0, 'X20_1':0,'X21_1':0,'X22_1':0,'X23_1':1,'X18_2':0, 'X19_2':0, 'X20_2':0,'X21_2':0,'X22_2':0,'X23_2':1,
          'X18_3':0, 'X19_3':0, 'X20_3':0,'X21_3':0,'X22_3':0,'X23_3':1}

dest4_vars = LpVariable.dicts("Dest4",Dest4,0)
prob4 += lpSum([costs4[i]*dest4_vars[i] for i in Dest4])
prob4 += lpSum([x4_1[i] * dest4_vars[i] for i in Dest4]) ==1
prob4 += lpSum([x4_2[i] * dest4_vars[i] for i in Dest4]) ==1
prob4 += lpSum([x4_3[i] * dest4_vars[i] for i in Dest4]) ==1

prob4 += lpSum([y4_1[i] * dest4_vars[i] for i in Dest4]) <=1
prob4 += lpSum([y4_2[i] * dest4_vars[i] for i in Dest4]) <=1
prob4 += lpSum([y4_3[i] * dest4_vars[i] for i in Dest4]) <=1
prob4 += lpSum([y4_4[i] * dest4_vars[i] for i in Dest4]) <=1
prob4 += lpSum([y4_5[i] * dest4_vars[i] for i in Dest4]) <=1
prob4 += lpSum([y4_6[i] * dest4_vars[i] for i in Dest4]) <=1

prob4 += lpSum([y4_1[i] * dest4_vars[i] for i in Dest4]) >=0
prob4 += lpSum([y4_2[i] * dest4_vars[i] for i in Dest4]) >=0
prob4 += lpSum([y4_3[i] * dest4_vars[i] for i in Dest4]) >=0
prob4 += lpSum([y4_4[i] * dest4_vars[i] for i in Dest4]) >=0
prob4 += lpSum([y4_5[i] * dest4_vars[i] for i in Dest4]) >=0
prob4 += lpSum([y4_6[i] * dest4_vars[i] for i in Dest4]) >=0

prob4.solve()
for v in prob4.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print('obj4=',value(prob4.objective))
print("")

#5
prob5 = LpProblem("OR_FINAL", pulp.LpMaximize)
Dest5 = ['X24_1', 'X25_1', 'X26_1','X27_1','X28_1','X29_1','X24_2', 'X25_2', 'X26_2','X27_2','X28_2','X29_2','X24_3', 'X25_3', 'X26_3','X27_3','X28_3','X29_3']
costs5 = {'X24_1':32, 'X25_1':41, 'X26_1':22,'X27_1':37,'X28_1':43,'X29_1':45,'X24_2':42, 'X25_2':31, 'X26_2':32,'X27_2':27,'X28_2':33,'X29_2':35,
          'X24_3':0, 'X25_3':0, 'X26_3':42,'X27_3':17,'X28_3':23,'X29_3':0}
x5_1 = {'X24_1':1, 'X25_1':1, 'X26_1':1,'X27_1':1,'X28_1':1,'X29_1':1,'X24_2':0, 'X25_2':0, 'X26_2':0,'X27_2':0,'X28_2':0,'X29_2':0,
          'X24_3':0, 'X25_3':0, 'X26_3':0,'X27_3':0,'X28_3':0,'X29_3':0}
x5_2 = {'X24_1':0, 'X25_1':0, 'X26_1':0,'X27_1':0,'X28_1':0,'X29_1':0,'X24_2':1, 'X25_2':1, 'X26_2':1,'X27_2':1,'X28_2':1,'X29_2':1,
          'X24_3':0, 'X25_3':0, 'X26_3':0,'X27_3':0,'X28_3':0,'X29_3':0}
x5_3 = {'X24_1':0, 'X25_1':0, 'X26_1':0,'X27_1':0,'X28_1':0,'X29_1':0,'X24_2':0, 'X25_2':0, 'X26_2':0,'X27_2':0,'X28_2':0,'X29_2':0,
          'X24_3':1, 'X25_3':1, 'X26_3':1,'X27_3':1,'X28_3':1,'X29_3':1}

y5_1 = {'X24_1':1, 'X25_1':0, 'X26_1':0,'X27_1':0,'X28_1':0,'X29_1':0,'X24_2':1, 'X25_2':0, 'X26_2':0,'X27_2':0,'X28_2':0,'X29_2':0,
          'X24_3':1, 'X25_3':0, 'X26_3':0,'X27_3':0,'X28_3':0,'X29_3':0}
y5_2 = {'X24_1':0, 'X25_1':1, 'X26_1':0,'X27_1':0,'X28_1':0,'X29_1':0,'X24_2':0, 'X25_2':1, 'X26_2':0,'X27_2':0,'X28_2':0,'X29_2':0,
          'X24_3':0, 'X25_3':1, 'X26_3':0,'X27_3':0,'X28_3':0,'X29_3':0}
y5_3 = {'X24_1':0, 'X25_1':0, 'X26_1':1,'X27_1':0,'X28_1':0,'X29_1':0,'X24_2':0, 'X25_2':0, 'X26_2':1,'X27_2':0,'X28_2':0,'X29_2':0,
          'X24_3':0, 'X25_3':0, 'X26_3':1,'X27_3':0,'X28_3':0,'X29_3':0}
y5_4 = {'X24_1':0, 'X25_1':0, 'X26_1':0,'X27_1':1,'X28_1':0,'X29_1':0,'X24_2':0, 'X25_2':0, 'X26_2':0,'X27_2':1,'X28_2':0,'X29_2':0,
          'X24_3':0, 'X25_3':0, 'X26_3':0,'X27_3':1,'X28_3':0,'X29_3':0}
y5_5 = {'X24_1':0, 'X25_1':0, 'X26_1':0,'X27_1':0,'X28_1':1,'X29_1':0,'X24_2':0, 'X25_2':0, 'X26_2':0,'X27_2':0,'X28_2':1,'X29_2':0,
          'X24_3':0, 'X25_3':0, 'X26_3':0,'X27_3':0,'X28_3':1,'X29_3':0}
y5_6 = {'X24_1':0, 'X25_1':0, 'X26_1':0,'X27_1':0,'X28_1':0,'X29_1':1,'X24_2':0, 'X25_2':0, 'X26_2':0,'X27_2':0,'X28_2':0,'X29_2':1,
          'X24_3':0, 'X25_3':0, 'X26_3':0,'X27_3':0,'X28_3':0,'X29_3':1}

dest5_vars = LpVariable.dicts("Dest5",Dest5,0)
prob5 += lpSum([costs5[i]*dest5_vars[i] for i in Dest5])
prob5 += lpSum([x5_1[i] * dest5_vars[i] for i in Dest5]) ==1
prob5 += lpSum([x5_2[i] * dest5_vars[i] for i in Dest5]) ==1
prob5 += lpSum([x5_3[i] * dest5_vars[i] for i in Dest5]) ==1

prob5 += lpSum([y5_1[i] * dest5_vars[i] for i in Dest5]) <=1
prob5 += lpSum([y5_2[i] * dest5_vars[i] for i in Dest5]) <=1
prob5 += lpSum([y5_3[i] * dest5_vars[i] for i in Dest5]) <=1
prob5 += lpSum([y5_4[i] * dest5_vars[i] for i in Dest5]) <=1
prob5 += lpSum([y5_5[i] * dest5_vars[i] for i in Dest5]) <=1
prob5 += lpSum([y5_6[i] * dest5_vars[i] for i in Dest5]) <=1

prob5 += lpSum([y5_1[i] * dest5_vars[i] for i in Dest5]) >=0
prob5 += lpSum([y5_2[i] * dest5_vars[i] for i in Dest5]) >=0
prob5 += lpSum([y5_3[i] * dest5_vars[i] for i in Dest5]) >=0
prob5 += lpSum([y5_4[i] * dest5_vars[i] for i in Dest5]) >=0
prob5 += lpSum([y5_5[i] * dest5_vars[i] for i in Dest5]) >=0
prob5 += lpSum([y5_6[i] * dest5_vars[i] for i in Dest5]) >=0

prob5.solve()
for v in prob5.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print('obj5=',value(prob5.objective))
print("")
#6
prob6 = LpProblem("OR_FINAL", pulp.LpMaximize)
Dest6 = ['X30_1', 'X31_1', 'X32_1','X33_1','X34_1','X30_2', 'X31_2', 'X32_2','X33_2','X34_2','X30_3', 'X31_3', 'X32_3','X33_3','X34_3']
costs6 = {'X30_1':42, 'X31_1':37, 'X32_1':0,'X33_1':30,'X34_1':43,'X30_2':32, 'X31_2':27, 'X32_2':39,'X33_2':40,'X34_2':33,
          'X30_3':22, 'X31_3':17, 'X32_3':0,'X33_3':0,'X34_3':0}
x6_1 = {'X30_1':1, 'X31_1':1, 'X32_1':1,'X33_1':1,'X34_1':1,'X30_2':0, 'X31_2':0, 'X32_2':0,'X33_2':0,'X34_2':0,
          'X30_3':0, 'X31_3':0, 'X32_3':0,'X33_3':0,'X34_3':0}
x6_2 = {'X30_1':0, 'X31_1':0, 'X32_1':0,'X33_1':0,'X34_1':0,'X30_2':1, 'X31_2':1, 'X32_2':1,'X33_2':1,'X34_2':1,
          'X30_3':0, 'X31_3':0, 'X32_3':0,'X33_3':0,'X34_3':0}
x6_3 = {'X30_1':0, 'X31_1':0, 'X32_1':0,'X33_1':0,'X34_1':0,'X30_2':0, 'X31_2':0, 'X32_2':0,'X33_2':0,'X34_2':0,
          'X30_3':1, 'X31_3':1, 'X32_3':1,'X33_3':1,'X34_3':1}

y6_1 = {'X30_1':1, 'X31_1':0, 'X32_1':0,'X33_1':0,'X34_1':0,'X30_2':1, 'X31_2':0, 'X32_2':0,'X33_2':0,'X34_2':0,
          'X30_3':1, 'X31_3':0, 'X32_3':0,'X33_3':0,'X34_3':0}
y6_2 = {'X30_1':0, 'X31_1':1, 'X32_1':0,'X33_1':0,'X34_1':0,'X30_2':0, 'X31_2':1, 'X32_2':0,'X33_2':0,'X34_2':0,
          'X30_3':0, 'X31_3':1, 'X32_3':0,'X33_3':0,'X34_3':0}
y6_3 = {'X30_1':0, 'X31_1':0, 'X32_1':1,'X33_1':0,'X34_1':0,'X30_2':0, 'X31_2':0, 'X32_2':1,'X33_2':0,'X34_2':0,
          'X30_3':0, 'X31_3':0, 'X32_3':1,'X33_3':0,'X34_3':0}
y6_4 = {'X30_1':0, 'X31_1':0, 'X32_1':0,'X33_1':1,'X34_1':0,'X30_2':0, 'X31_2':0, 'X32_2':0,'X33_2':1,'X34_2':0,
          'X30_3':0, 'X31_3':0, 'X32_3':0,'X33_3':1,'X34_3':0}
y6_5 = {'X30_1':0, 'X31_1':0, 'X32_1':0,'X33_1':0,'X34_1':1,'X30_2':0, 'X31_2':0, 'X32_2':0,'X33_2':0,'X34_2':1,
          'X30_3':0, 'X31_3':0, 'X32_3':0,'X33_3':0,'X34_3':1}

dest6_vars = LpVariable.dicts("Dest6",Dest6,0)
prob6 += lpSum([costs6[i]*dest6_vars[i] for i in Dest6])
prob6 += lpSum([x6_1[i] * dest6_vars[i] for i in Dest6]) ==1
prob6 += lpSum([x6_2[i] * dest6_vars[i] for i in Dest6]) ==1
prob6 += lpSum([x6_3[i] * dest6_vars[i] for i in Dest6]) ==1

prob6 += lpSum([y6_1[i] * dest6_vars[i] for i in Dest6]) <=1
prob6 += lpSum([y6_2[i] * dest6_vars[i] for i in Dest6]) <=1
prob6 += lpSum([y6_3[i] * dest6_vars[i] for i in Dest6]) <=1
prob6 += lpSum([y6_4[i] * dest6_vars[i] for i in Dest6]) <=1
prob6 += lpSum([y6_5[i] * dest6_vars[i] for i in Dest6]) <=1

prob6 += lpSum([y6_1[i] * dest6_vars[i] for i in Dest6]) >=0
prob6 += lpSum([y6_2[i] * dest6_vars[i] for i in Dest6]) >=0
prob6 += lpSum([y6_3[i] * dest6_vars[i] for i in Dest6]) >=0
prob6 += lpSum([y6_4[i] * dest6_vars[i] for i in Dest6]) >=0
prob6 += lpSum([y6_5[i] * dest6_vars[i] for i in Dest6]) >=0

prob6.solve()
for v in prob6.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print('obj6=',value(prob6.objective))
print("")

#7
prob7 = LpProblem("OR_FINAL", pulp.LpMaximize)
Dest7 = ['X35_1', 'X36_1', 'X37_1','X35_2', 'X36_2', 'X37_2','X35_3', 'X36_3', 'X37_3']
costs7 = {'X35_1':34, 'X36_1':41, 'X37_1':32,'X35_2':44, 'X36_2':31, 'X37_2':42,'X35_3':0, 'X36_3':0, 'X37_3':0}
x7_1 = {'X35_1':1, 'X36_1':1, 'X37_1':1,'X35_2':0, 'X36_2':0, 'X37_2':0,'X35_3':0, 'X36_3':0, 'X37_3':0}
x7_2 = {'X35_1':0, 'X36_1':0, 'X37_1':0,'X35_2':1, 'X36_2':1, 'X37_2':1,'X35_3':0, 'X36_3':0, 'X37_3':0}
x7_3 = {'X35_1':0, 'X36_1':0, 'X37_1':0,'X35_2':0, 'X36_2':0, 'X37_2':0,'X35_3':1, 'X36_3':1, 'X37_3':1}

y7_1 = {'X35_1':1, 'X36_1':0, 'X37_1':0,'X35_2':1, 'X36_2':0, 'X37_2':0,'X35_3':1, 'X36_3':0, 'X37_3':0}
y7_2 = {'X35_1':0, 'X36_1':1, 'X37_1':0,'X35_2':0, 'X36_2':1, 'X37_2':0,'X35_3':0, 'X36_3':1, 'X37_3':0}
y7_3 = {'X35_1':0, 'X36_1':0, 'X37_1':1,'X35_2':0, 'X36_2':0, 'X37_2':1,'X35_3':0, 'X36_3':0, 'X37_3':1}


dest7_vars = LpVariable.dicts("Dest7",Dest7,0)
prob7 += lpSum([costs7[i]*dest7_vars[i] for i in Dest7])

prob7 += lpSum([x7_1[i] * dest7_vars[i] for i in Dest7]) ==1
prob7 += lpSum([x7_2[i] * dest7_vars[i] for i in Dest7]) ==1
prob7 += lpSum([x7_3[i] * dest7_vars[i] for i in Dest7]) ==1

prob7 += lpSum([y7_1[i] * dest7_vars[i] for i in Dest7]) <=1
prob7 += lpSum([y7_2[i] * dest7_vars[i] for i in Dest7]) <=1
prob7 += lpSum([y7_3[i] * dest7_vars[i] for i in Dest7]) <=1

prob7 += lpSum([y7_1[i] * dest7_vars[i] for i in Dest7]) >=0
prob7 += lpSum([y7_2[i] * dest7_vars[i] for i in Dest7]) >=0
prob7 += lpSum([y7_3[i] * dest7_vars[i] for i in Dest7]) >=0

prob7.solve()
for v in prob7.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print('obj7=',value(prob7.objective))
print("")
#8
prob8 = LpProblem("OR_FINAL", pulp.LpMaximize)
Dest8 = ['X38_1', 'X39_1', 'X40_1','X41_1','X38_2', 'X39_2', 'X40_2','X41_2','X38_3', 'X39_3', 'X40_3','X41_3']
costs8 = {'X38_1':31, 'X39_1':21, 'X40_1':26,'X41_1':40,'X38_2':31, 'X39_2':31, 'X40_2':36,'X41_2':30,'X38_3':41, 'X39_3':41, 'X40_3':0,'X41_3':20}
x8_1 = {'X38_1':1, 'X39_1':1, 'X40_1':1,'X41_1':1,'X38_2':0, 'X39_2':0, 'X40_2':0,'X41_2':0,'X38_3':0, 'X39_3':0, 'X40_3':0,'X41_3':0}
x8_2 = {'X38_1':0, 'X39_1':0, 'X40_1':0,'X41_1':0,'X38_2':1, 'X39_2':1, 'X40_2':1,'X41_2':1,'X38_3':0, 'X39_3':0, 'X40_3':0,'X41_3':0}
x8_3 = {'X38_1':0, 'X39_1':0, 'X40_1':0,'X41_1':0,'X38_2':0, 'X39_2':0, 'X40_2':0,'X41_2':0,'X38_3':1, 'X39_3':1, 'X40_3':1,'X41_3':1}

y8_1 = {'X38_1':1, 'X39_1':0, 'X40_1':0,'X41_1':0,'X38_2':1, 'X39_2':0, 'X40_2':0,'X41_2':0,'X38_3':1, 'X39_3':0, 'X40_3':0,'X41_3':0}
y8_2 = {'X38_1':0, 'X39_1':1, 'X40_1':0,'X41_1':0,'X38_2':0, 'X39_2':1, 'X40_2':0,'X41_2':0,'X38_3':0, 'X39_3':1, 'X40_3':0,'X41_3':0}
y8_3 = {'X38_1':0, 'X39_1':0, 'X40_1':1,'X41_1':0,'X38_2':0, 'X39_2':0, 'X40_2':1,'X41_2':0,'X38_3':0, 'X39_3':0, 'X40_3':1,'X41_3':0}
y8_4 = {'X38_1':0, 'X39_1':0, 'X40_1':0,'X41_1':1,'X38_2':0, 'X39_2':0, 'X40_2':0,'X41_2':1,'X38_3':0, 'X39_3':0, 'X40_3':0,'X41_3':1}

dest8_vars = LpVariable.dicts("Dest8",Dest8,0)
prob8 += lpSum([costs8[i]*dest8_vars[i] for i in Dest8])

prob8 += lpSum([x8_1[i] * dest8_vars[i] for i in Dest8]) ==1
prob8 += lpSum([x8_2[i] * dest8_vars[i] for i in Dest8]) ==1
prob8 += lpSum([x8_3[i] * dest8_vars[i] for i in Dest8]) ==1

prob8 += lpSum([y8_1[i] * dest8_vars[i] for i in Dest8]) <=1
prob8 += lpSum([y8_2[i] * dest8_vars[i] for i in Dest8]) <=1
prob8 += lpSum([y8_3[i] * dest8_vars[i] for i in Dest8]) <=1
prob8 += lpSum([y8_4[i] * dest8_vars[i] for i in Dest8]) <=1

prob8 += lpSum([y8_1[i] * dest8_vars[i] for i in Dest8]) >=0
prob8 += lpSum([y8_2[i] * dest8_vars[i] for i in Dest8]) >=0
prob8 += lpSum([y8_3[i] * dest8_vars[i] for i in Dest8]) >=0
prob8 += lpSum([y8_4[i] * dest8_vars[i] for i in Dest8]) >=0

prob8.solve()
for v in prob8.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print('obj8=',value(prob8.objective))
print("")

#9
prob9 = LpProblem("OR_FINAL", pulp.LpMaximize)
Dest9 = ['X42_1', 'X43_1', 'X44_1','X42_2', 'X43_2', 'X44_2','X42_3', 'X43_3', 'X44_3']
costs9 = {'X42_1':33, 'X43_1':43, 'X44_1':0,'X42_2':41, 'X43_2':31, 'X44_2':0,'X42_3':21, 'X43_3':31, 'X44_3':41}
x9_1 = {'X42_1':1, 'X43_1':1, 'X44_1':1,'X42_2':0, 'X43_2':0, 'X44_2':0,'X42_3':0, 'X43_3':0, 'X44_3':0}
x9_2 = {'X42_1':0, 'X43_1':0, 'X44_1':0,'X42_2':1, 'X43_2':1, 'X44_2':1,'X42_3':0, 'X43_3':0, 'X44_3':0}
x9_3 = {'X42_1':0, 'X43_1':0, 'X44_1':0,'X42_2':0, 'X43_2':0, 'X44_2':0,'X42_3':1, 'X43_3':1, 'X44_3':1}

y9_1 = {'X42_1':1, 'X43_1':0, 'X44_1':0,'X42_2':1, 'X43_2':0, 'X44_2':0,'X42_3':1, 'X43_3':0, 'X44_3':0}
y9_2 = {'X42_1':0, 'X43_1':1, 'X44_1':0,'X42_2':0, 'X43_2':1, 'X44_2':0,'X42_3':0, 'X43_3':1, 'X44_3':0}
y9_3 = {'X42_1':0, 'X43_1':0, 'X44_1':1,'X42_2':0, 'X43_2':0, 'X44_2':1,'X42_3':0, 'X43_3':0, 'X44_3':1}


dest9_vars = LpVariable.dicts("Dest9",Dest9,0)
prob9 += lpSum([costs9[i]*dest9_vars[i] for i in Dest9])

prob9 += lpSum([x9_1[i] * dest9_vars[i] for i in Dest9]) ==1
prob9 += lpSum([x9_2[i] * dest9_vars[i] for i in Dest9]) ==1
prob9 += lpSum([x9_3[i] * dest9_vars[i] for i in Dest9]) ==1

prob9 += lpSum([y9_1[i] * dest9_vars[i] for i in Dest9]) <=1
prob9 += lpSum([y9_2[i] * dest9_vars[i] for i in Dest9]) <=1
prob9 += lpSum([y9_3[i] * dest9_vars[i] for i in Dest9]) <=1

prob9 += lpSum([y9_1[i] * dest9_vars[i] for i in Dest9]) >=0
prob9 += lpSum([y9_2[i] * dest9_vars[i] for i in Dest9]) >=0
prob9 += lpSum([y9_3[i] * dest9_vars[i] for i in Dest9]) >=0

prob9.solve()
for v in prob9.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print('obj9=',value(prob9.objective))
print("")
#0
prob0 = LpProblem("OR_FINAL", pulp.LpMaximize)
Dest0 = ['X45_1', 'X46_1', 'X47_1','X48_1','X49_1','X45_2', 'X46_2', 'X47_2','X48_2','X49_2','X45_3', 'X46_3', 'X47_3','X48_3','X49_3']
costs0 = {'X45_1':39, 'X46_1':44, 'X47_1':0,'X48_1':20,'X49_1':42,'X45_2':29, 'X46_2':34, 'X47_2':39,'X48_2':40,'X49_2':32,'X45_3':19, 'X46_3':0, 'X47_3':29,'X48_3':30,'X49_3':0}
x0_1 = {'X45_1':1, 'X46_1':1, 'X47_1':1,'X48_1':1,'X49_1':1,'X45_2':0, 'X46_2':0, 'X47_2':0,'X48_2':0,'X49_2':0,'X45_3':0, 'X46_3':0, 'X47_3':0,'X48_3':0,'X49_3':0}
x0_2 = {'X45_1':0, 'X46_1':0, 'X47_1':0,'X48_1':0,'X49_1':0,'X45_2':1, 'X46_2':1, 'X47_2':1,'X48_2':1,'X49_2':1,'X45_3':0, 'X46_3':0, 'X47_3':0,'X48_3':0,'X49_3':0}
x0_3 = {'X45_1':0, 'X46_1':0, 'X47_1':0,'X48_1':0,'X49_1':0,'X45_2':0, 'X46_2':0, 'X47_2':0,'X48_2':0,'X49_2':0,'X45_3':1, 'X46_3':1, 'X47_3':1,'X48_3':1,'X49_3':1}

y0_1 = {'X45_1':1, 'X46_1':0, 'X47_1':0,'X48_1':0,'X49_1':0,'X45_2':1, 'X46_2':0, 'X47_2':0,'X48_2':0,'X49_2':0,'X45_3':1, 'X46_3':0, 'X47_3':0,'X48_3':0,'X49_3':0}
y0_2 = {'X45_1':0, 'X46_1':1, 'X47_1':0,'X48_1':0,'X49_1':0,'X45_2':0, 'X46_2':1, 'X47_2':0,'X48_2':0,'X49_2':0,'X45_3':0, 'X46_3':1, 'X47_3':0,'X48_3':0,'X49_3':0}
y0_3 = {'X45_1':0, 'X46_1':0, 'X47_1':1,'X48_1':0,'X49_1':0,'X45_2':0, 'X46_2':0, 'X47_2':1,'X48_2':0,'X49_2':0,'X45_3':0, 'X46_3':0, 'X47_3':1,'X48_3':0,'X49_3':0}
y0_4 = {'X45_1':0, 'X46_1':0, 'X47_1':0,'X48_1':1,'X49_1':0,'X45_2':0, 'X46_2':0, 'X47_2':0,'X48_2':1,'X49_2':0,'X45_3':0, 'X46_3':0, 'X47_3':0,'X48_3':1,'X49_3':0}
y0_5 = {'X45_1':0, 'X46_1':0, 'X47_1':0,'X48_1':0,'X49_1':1,'X45_2':0, 'X46_2':0, 'X47_2':0,'X48_2':0,'X49_2':1,'X45_3':0, 'X46_3':0, 'X47_3':0,'X48_3':0,'X49_3':1}

dest0_vars = LpVariable.dicts("Dest0",Dest0,0)
prob0 += lpSum([costs0[i]*dest0_vars[i] for i in Dest0])
prob0 += lpSum([x0_1[i] * dest0_vars[i] for i in Dest0]) ==1
prob0 += lpSum([x0_2[i] * dest0_vars[i] for i in Dest0]) ==1
prob0 += lpSum([x0_3[i] * dest0_vars[i] for i in Dest0]) ==1

prob0 += lpSum([y0_1[i] * dest0_vars[i] for i in Dest0]) <=1
prob0 += lpSum([y0_2[i] * dest0_vars[i] for i in Dest0]) <=1
prob0 += lpSum([y0_3[i] * dest0_vars[i] for i in Dest0]) <=1
prob0 += lpSum([y0_4[i] * dest0_vars[i] for i in Dest0]) <=1
prob0 += lpSum([y0_5[i] * dest0_vars[i] for i in Dest0]) <=1

prob0 += lpSum([y0_1[i] * dest0_vars[i] for i in Dest0]) >=0
prob0 += lpSum([y0_2[i] * dest0_vars[i] for i in Dest0]) >=0
prob0 += lpSum([y0_3[i] * dest0_vars[i] for i in Dest0]) >=0
prob0 += lpSum([y0_4[i] * dest0_vars[i] for i in Dest0]) >=0
prob0 += lpSum([y0_5[i] * dest0_vars[i] for i in Dest0]) >=0

prob0.solve()
for v in prob0.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print('obj10=',value(prob0.objective))
print("")

mx = [value(prob1.objective),value(prob2.objective),value(prob3.objective),value(prob4.objective),value(prob5.objective),value(prob6.objective),
      value(prob7.objective),value(prob8.objective),value(prob9.objective),value(prob0.objective)]

print("Max :",max(mx))
print ("Route :",mx.index(max(mx))+1) # 返回最大值

if mx.index(max(mx))+1 == 1:
    for v in prob1.variables():
        if v.varValue == 1.0:
            print(v.name, "=", v.varValue)
            
elif mx.index(max(mx))+1 == 2:
    for v in prob2.variables():
        if v.varValue == 1.0:
            print(v.name, "=", v.varValue)
            
elif mx.index(max(mx))+1 == 3:
    for v in prob3.variables():
        if v.varValue == 1.0:
            print(v.name, "=", v.varValue)
            
elif mx.index(max(mx))+1 == 4:
    for v in prob4.variables():
        if v.varValue == 1.0:
            print(v.name, "=", v.varValue)
            
elif mx.index(max(mx))+1 == 5:
    for v in prob5.variables():
        if v.varValue == 1.0:
            print(v.name, "=", v.varValue)
            
elif mx.index(max(mx))+1 == 6:
    for v in prob6.variables():
        if v.varValue == 1.0:
            print(v.name, "=", v.varValue)
            
elif mx.index(max(mx))+1 == 7:
    for v in prob7.variables():
        if v.varValue == 1.0:
            print(v.name, "=", v.varValue)
            
elif mx.index(max(mx))+1 == 8:
    for v in prob8.variables():
        if v.varValue == 1.0:
            print(v.name, "=", v.varValue)
            
elif mx.index(max(mx))+1 == 9:
    for v in prob9.variables():
        if v.varValue == 1.0:
            print(v.name, "=", v.varValue)
            
elif mx.index(max(mx))+1 == 10:
    for v in prob0.variables():
        if v.varValue == 1.0:
            print(v.name, "=", v.varValue)