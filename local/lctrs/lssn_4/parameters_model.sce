m = 17e-3;                                      //масса ротора
r = 23.5e-3 / 2;                             //радиус ротора
L = 4.7e-3 ;                                  //индуктивность обмотки ротора
R_rotor = 4.4;                           //сопротивление обмотки ротора
I_st = 0.98;                              //пусковой ток
U_ctrl = 8.02;                        //управляющее напряжение
i = 48;                                  //коэффициент редукции
J = m * r^2 / 2;                             //момент инерции ротора
T_m = 0.08;                                //электромеханическая постоянная времени
omega = 14.4 * i;                     //угловая скорость вращения ротора
dot_omega = omega / T_m;    //угловое ускорение ротора
M_st = J * dot_omega;        //пусковой момент двигателя
k_t = M_st / I_st;               //конструктивная постоянная
k_e = U_ctrl / omega;      //конструктивная постоянная
K_p = 20;