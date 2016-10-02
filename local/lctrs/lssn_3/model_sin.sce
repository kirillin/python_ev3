V = 1;
Tm = 0.0647448;
Ke = 8 / 16.343242;

data = read("/media/data/evo/python_ev3/local/lctrs/lssn_3/data.txt", -1, 2);

data(:,1) = data(:,1) - data(1,1)/1000;
time = data(:,1)/1000;
angle = data(:,2) * %pi/180;

importXcosDiagram("/media/data/evo/python_ev3/local/lctrs/lssn_3/model_sin.zcos");
xcos_simulate(scs_m, 4);
plot(time, angle-8.9360858, "r--");
plot(A.time, A.values);


