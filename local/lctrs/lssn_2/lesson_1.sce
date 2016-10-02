num = 4;

matrix_row = [1 2 3];
matrix_col = [1; 2; 3];
matrix2_2 = [4 3; -3 6];

det(matrix2_2);

inv(matrix2_2);
matrix2_2^-1 

//trans(matrix2x2);

time = 0:0.01:10;


xtitle("blablabla");
plot(time, sin(time));

a = gca();
a.background = 1;
fg = a.children.children;
fg.color = 0;
fg.thickness = 5;
legend(["$\cos\Alpha$"], opt = 3);

A = [0 1; -4 0];
