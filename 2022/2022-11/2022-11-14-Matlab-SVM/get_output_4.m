if exist('output', 'dir')
    delete('output')
end

if ~exist('output', 'dir')
    mkdir('output')
    mkdir(['output' filesep 'autograde'])
    mkdir(['output' filesep 'images'])
    mkdir(['output' filesep 'report'])
    mkdir(['output' filesep 'code'])
end

test_unit();
test_unit(0.001, 14175332, "_rho_0.001");
test_unit(0.01, 14175332, "_rho_0.01");
test_unit(0.1, 14175332, "_rho_0.1");
test_unit(1, 14175332, "_rho_1");
test_unit(20, 14175332, "_rho_20");
test_unit(50, 14175332, "_rho_50");
test_unit(100, 14175332, "_rho_100");
test_unit(10, 359950539, "_seed_359950539");
test_unit(10, 927112, "_seed_927112");
test_unit(10, 12345678, "_seed_927112");

function test_unit(rho, seed, postfix)
    arguments
        rho = 10
        seed = 14175332
        postfix = ""
    end

    rng(seed);

    v1 = [1 2 3 1 1 3 -1 -3;
        -1 0 -2 -0.5 -4 -3 -3 -3]; 
    u1 = [-1 -1 0 1 -3 -4 0.5 3 0.5;
        0 1 2 3 0 -2 2 2.5 2.5];
    
    u2 = 10.1 * randn(2, 20) + 15; 
    v2 = -10.1 * randn(2, 20) - 15;
    u3 = 10.1 * randn(2, 20) + 10; 
    v3 = -10.1 * randn(2, 20) - 10;
    u4 = 10.1 * randn(2, 50) + 18;
    v4 = -10.1 * randn(2, 50) - 18;
    
%% Autograded part
    vs = {v1, v2, v3, v4};
    
    for i = 1 : 4
        [~, ~, ~, b] = SVMhard2(rho, us{i}, vs{i});
    % For autograder
        T = table(b, 'VariableNames', {'b'});
        fname = "output" + filesep + "autograde" + filesep + "b" + i + postfix + ".txt";
        writetable(T, fname)
        
        if ishandle(1)
            saveas(gcf, "output" + filesep + "images" + filesep + "img" + i + postfix + ".png");
            close all
        end
    end
end

