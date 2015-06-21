%t = (0:0.001:1)';
%y = sin(2*pi*1000*t); % sygnał o częstotliwości 1000Hz
% wavplay(y) % odtworzenie dźwięku y

% Generujemy sygnał 1KHz trwający 5 sec
dur = 2.0;
fs = 8000;
tt = 0 : (1/fs) : dur;
xx = sin( 2*pi*1000*tt );
wavwrite(xx','sound.wav')
