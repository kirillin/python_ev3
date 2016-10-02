clear;
a = 4;
b = 2;
t(:,1) = 0:0.01:10;
t(:,2) = a + sin(t(:,1) + b);
deletefile("/media/data/evo/python_ev3/local/lctrs/lssn_2/data.txt");
write("/media/data/evo/python_ev3/local/lctrs/lssn_2/data.txt", t);
data = read("/media/data/evo/python_ev3/local/lctrs/lssn_2/data.txt", -1, 2);
plot(data(:,1), data(:,2));

