clear;
data = read("/media/data/evo/python_ev3/local/lctrs/lssn_2/data.txt", -1, 2);

function e = G(a, z)
    e = z(2) - (a(1) + sin(z(1) + a(2)));
endfunction

a0 = [3; -2];
[aa, err] = datafit(G, data', a0);


plot(data(:,1), data(:,2));

