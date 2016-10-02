function ydot=f(t, y)
    ydot = A * y;
endfunction

t = 0:0.01:5;
h=ode([5;0], 0, t, f);

plot(t, h);
