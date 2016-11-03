clear;
g = 9.81;
l = 0.6;
r = 0.0028;
mp = 0.044;
mw = 0.017;
mc = 0.563 - mw * 4;
Jp = mp * l^2 / 12;
Jw = mw * r^2 / 2;
J = 0.0023;
Km = 0.5;
Ke = 0.5;
R = 7.2; // ?? ev3
Umax = 7.6;
size_buffer = 10000;

tnreal = 6.3;
tn = 1.5;
w0 = tnreal/tn;

z0=w0^3;
z1=3*w0^2;
z2=3*w0;


a11 = 0;
a12 = 0;
a13 = 1;


a21 =(g*l^2*mp^2*r)/((4*Jp+l^2*mp)*(-4*Jw-mc*r^2-mp*r^2-4*mw*r^2-2*J)+l^2*mp^2*r^2);
a31 = (2*g*l*mp*(-4*Jw-mc*r^2-mp*r^2-4*mw*r^2-2*J))/((4*Jp+l^2*mp)*(-4*Jw-mc*r^2-mp*r^2-4*mw*r^2-2*J)+l^2*mp^2*r^2);

a22 = -(2*Ke*Km*(-4*Jp-l^2*mp))/(((4*Jp+l^2*mp)*(-4*Jw-mc*r^2-mp*r^2-4*mw*r^2-2*J)+l^2*mp^2*r^2)*R);
a32 = -(4*Ke*Km*l*mp*r)/(((4*Jp+l^2*mp)*(-4*Jw-mc*r^2-mp*r^2-4*mw*r^2-2*J)+l^2*mp^2*r^2)*R);

a23 = 0;
a33 = 0;

b1 = (2*Km*(-4*Jp-l^2*mp))/(((4*Jp+l^2*mp)*(-4*Jw-mc*r^2-mp*r^2-4*mw*r^2-2*J)+l^2*mp^2*r^2)*R);
b2 = (4*Km*l*mp*r)/(((4*Jp+l^2*mp)*(-4*Jw-mc*r^2-mp*r^2-4*mw*r^2-2*J)+l^2*mp^2*r^2)*R);



A=[a11,a12,a13;a21,a22,a23;a31,a32,a33];
B=[0,b1,b2]' * Umax;

Y=[B, A*B, A^2*B];



G=[0,0,-z0;1, 0, -z1; 0, 1, -z2];
H=[0,0,1];

Q=[H; H*G; H*G^2];

S=sylv(-A,G,B*H,'c');

K=-H*S^-1

//importXcosDiagram("/media/data/evo/python_ev3/pendulumX4/x4pendulum_p.zcos");
//xcos_simulate(scs_m, 4);
