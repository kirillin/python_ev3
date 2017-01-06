plot2d(D.time, D.values(:,2));
plot2d(D.time, D.values(:,3));
plot2d(D.time, D.values(:,4));
plot2d(D.time, D.values(:,5));


scf(0);
plot(D.time, D.values(:,1), 1);
plot(D.time, D.values(:,2), 2);
plot(D.time, D.values(:,3), 3);
plot(D.time, D.values(:,4), 4);
plot(D.time, D.values(:,5), 4);


plot(D.time, D.values(:,5), "b");

a = gca();
a.children.children.thickness = 3;

xtitle("blablabla");

a = gca();
a.background = -2;
fg = a.children.children;
fg.color = 0;
fg.thickness = 5;
legend(["$K = $" + K], opt = 3);


Gg = [
    0, 0, 0, -z0;
    1, 0, 0, -z1;
    0, 1, 0, -z2;
    0, 0, 1, -z3
];

Hh = [0,0,0,1];

Qq = [
    Hh;
    Hh*Gg;
    Hh*Gg^2
    Hh*Gg^3
];

S = sylv(-A, Gg, B*Hh, 'c');

//K = -Hh * S^(-1);
