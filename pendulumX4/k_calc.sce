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
R = 7.5; // ?? ev3
Umax = 7.6;
size_buffer = 10000;

// 2.3- расходится
// 1.4
// -0.5
tnreal = 1.8;
tn = 6.3;
w0 = tn / tnreal;

z0 = w0^3;
z1 = 3 * w0^2;
z2 = 3 * w0;

E = [
    2*mp*l*r,                               mp*l^2 + 4*Jp;
    mp*r^2 + mc*r^2+ 4*mw*r^2+4*Jw + 2*J,   mp*l*r/2
];



F = [
    0,          0;
    2*Km*Ke/R,  0
];

G = [
    0,  -2*mp*g*l;
    0,  0
];

H = [
    0;
    2*Km/R
];

u = Umax;

detE = det(E);

iE = (1/detE) * [
    mp*l*r/2,                               -mp*l^2 - 4*Jp;
    -(mp*r^2 + mc*r^2+ 4*mw*r^2+4*Jw + 2*J),   2*mp*l*r
];

//iE = E^-1;
dQv = -iE * F;
Qv = -iE * G;
Uv = iE * H * Umax;


A = [
    0,      0,      1;
    Qv(1,2),  dQv(1,1), dQv(1,2);
    Qv(2,2),  dQv(2,1), dQv(2,2)
];

B = [
    0;
    Uv(1);
    Uv(2)
];

C = [];

// матрица управляемости
Y = [
    B, A*B, A^2*B
];

Gg = [
    0, 0, -z0;
    1, 0, -z1;
    0, 1, -z2
];

Hh = [0,0,1];

Qq = [
    Hh;
    Hh*Gg;
    Hh*Gg^2
];

S = sylv(-A, Gg, B*Hh, 'c');

K = -Hh * S^(-1);



