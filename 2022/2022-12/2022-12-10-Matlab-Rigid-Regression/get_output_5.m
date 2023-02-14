function get_output_5
% Project 4
if ~exist('output', 'dir')
    mkdir('output')
    mkdir(['output' filesep 'part1'])
    mkdir(['output' filesep 'part2'])
    mkdir(['output' filesep 'part3'])
    mkdir(['output' filesep 'part4'])
    mkdir(['output' filesep 'images'])
    mkdir(['output' filesep 'code'])
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This part is vital for the autograder so everyone gets the same results
% Comment out this part below if using this for the report
rng(97922758)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

X3 = [-10; -8; -6; -4; -2; 2; 4; 6; 8; 10; -9; -7; -5; -3; -1; 1; 3; 5; 7; 9];
y3 = [-3; 1; 0; 0; 1.5; 4; 6; 5; 1; 8; -2.5; 0.5; 1.5; -1; -0.5; 3.5; 5.5; 2.5; 4.5; 5];

X13 = 15*randn(50,1);
ww13 = 1;
y13 = X13*ww13 + 10*randn(50,1) + 20;

X = [-10, 11; -6, 5; -2, 4; 0, 0; 1, 2; 2, -5; 6, -4; 10, -6];
y = [0; -2.5; 0.5; -2; 2.5; -4.2; 1; 4];

X8 = 10*randn(50,2);
ww = [1; 2];
y8 = X8*ww + 10*randn(50,1) + 10;

X10 = 10*randn(100,2);
ww2 = [1; 2];
y10 = X10*ww2 + 10*randn(100,1) + 15;

X20 = randn(50,30);
ww20 = [0; 2; 0; -3; 0; -4; 1; 0; 2; 0; 2; 3; 0; -5; 6; 0; 1; 2; 0; 10; 0; 0; 3; 4; 5; 0; 0; -6; -8; 0];
y20 = X20*ww20 + randn(50,1)*0.1 + 5;

Xs = cell(6,1);
ys = cell(6,1);
Xs{1} = X3;
ys{1} = y3;
Xs{2} = X13;
ys{2} = y13;
Xs{3} = X;
ys{3} = y;
Xs{4} = X8;
ys{4} = y8;
Xs{5} = X10;
ys{5} = y10;
Xs{6} = X20;
ys{6} = y20;


%% Autograded part
rho = 10;
for k = [ -2, -1, 0, 1, 2, 3 ]
    K = 10^k;
    for i = 1:length(Xs)
        [w1,b1,xi1,w2,b2,xi2,alpha2,w3,b3,xi3,w4,b4,xi4] = reg3(Xs{i},ys{i},K);
        
        % For autograder
        % Part 1
        T = table([w1(:);b1(:);xi1(:)], 'VariableNames', {'vars'});
        fname = ['output' filesep 'part1' filesep sprintf('ridgeregv1_%d_%d.txt',k+2, i)];
        writetable(T, fname)

        % Part 2
        T = table([w2(:);b2(:);xi2(:);alpha2(:)], 'VariableNames', {'vars'});
        fname = ['output' filesep 'part2' filesep sprintf('ridgeregb1_%d_%d.txt',k+2, i)];
        writetable(T, fname)

        % Part 3
        T = table([w3(:);b3(:);xi3(:)], 'VariableNames', {'vars'});
        fname = ['output' filesep 'part3' filesep sprintf('ridgeregv2_%d_%d.txt',k+2, i)];
        writetable(T, fname)

        % Part 4
        if k == 0 % No regularizaiton by K in part 4
            T = table([w4(:);b4(:);xi4(:)], 'VariableNames', {'vars'});
            fname = ['output' filesep 'part4' filesep sprintf('reglq_%d.txt', i)];
            writetable(T, fname)
        end

        % Write data to text file
        if ishandle(1)
            imname = ['output' filesep 'images' filesep sprintf('img_%d_%d.png',k+2,i)];
            saveas(gcf, imname);
            close all
        end
    end
end


end % function



