V = 1;
Tm = 0.0633519;     // aa[2]
Ke = 8 / 14.722618; // aa[1]

data = read("/media/data/evo/python_ev3/local/lctrs/lssn_3/data_sin.txt", -1, 2);

data(:,1) = data(:,1) - data(1,1)/1000;
time = data(:,1)/1000;
angle = data(:,2) * %pi / 180;

importXcosDiagram("/media/data/evo/python_ev3/local/lctrs/lssn_3/model_sin.zcos");
xcos_simulate(scs_m, 4);
plot(time, angle, "r--");
plot(A.time, A.values);

