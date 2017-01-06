importXcosDiagram("/media/data/evo/python_ev3/pendulumX4/x4pendulum_p_.zcos");
xcos_simulate(scs_m, 4);


plot2d(U.time, U.values,6);
//plot2d(d_theta.time, d_theta.values,1);
//plot2d(U.time, d_psi.values,2);
plot2d(psi.time, psi.values,3);

