clear;
angle = 10;
importXcosDiagram("/media/data/evo/python_ev3/local/lctrs/lssn_2/test_to_ws.zcos");
xcos_simulate(scs_m, 4);
plot(A.time, A.values);
a = gca();
a.children.children.thickness = 3;
xs2png(0, "/media/data/evo/python_ev3/local/lctrs/lssn_2/text.png");
