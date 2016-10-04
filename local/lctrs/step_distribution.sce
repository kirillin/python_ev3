clear;

function e = G(a, z)
    e = z(2) - a(1)*z(1) - a(1)*a(2)*exp(-z(1)/a(2)) + a(1)*a(2);
endfunction

function [tm, speed] = plt(data, color_real, color_model)
    time = data(:,1);
    time = time -time(1);
    data(:,2) = data(:,2) * %pi / 180;
    angle = data(:,2);
    a0 = [0; 10];
    [aa, er] = datafit(G, data', a0);
    tm = aa(2);
    speed = aa(1);
    model = aa(1)*time + aa(1)*aa(2)*exp(-time / aa(2)) - aa(1)*aa(2);
    disp(aa);
    plot(time, angle, color_real);
    plot(time, model, color_model);
endfunction

scf(0);
path_black = "/media/data/evo/python_ev3/local/lctrs/lssn_3/data.txt";
for i = 0:20
    data = read(path + "dataLargeMotor_black_" + string(i * 5) +                     + "pwr_1000sec.txt", -1, 2);
    disp("Power = " + string(i * 5));
    [Tm(i+1), w(i+1)] = plt(data, "k", "m--");
end

x = 0:5:100;
scf();
plot(x, Tm);
scf();
plot(x, w);
