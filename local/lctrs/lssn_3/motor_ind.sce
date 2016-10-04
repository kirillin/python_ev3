clear;

function e = G(a, z)
    e = z(2) - a(1)*z(1) - a(1)*a(2)*exp(-z(1)/a(2)) + a(1)*a(2);
endfunction


path = "/media/data/evo/python_ev3/local/lctrs/lssn_3/";
data = read(path + "data.txt", -1, 2);

time = data(:,1);
time = time -time(1);
data(:,2) = data(:,2) * %pi / 180;
angle = data(:,2);
a0 = [1; 20];
[aa, er] = datafit(G, data', a0);
model = aa(1)*time + aa(1)*aa(2)*exp(-time / aa(2)) - aa(1)*aa(2);
disp(aa);
plot(time, angle, "b");
plot(time, model, "r--");
