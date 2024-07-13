clear;  % Clear workspace

% Parameters
N = 50;          % Number of lattice points (N*N)
J = 1;           % Exchange coupling constant
T_list = linspace(0.001, 5, 16);    % Temperature

mean_magnetization = zeros(1, length(T_list));  % Initialize the magnetization
mean_energy = zeros(1, length(T_list));         % Initialize the energy

magnetization = zeros(10, length(T_list)); % Preallocate array to store magnetization results
energy = zeros(10, length(T_list));        % Preallocate array to store energy results

figure(820); % Create a new figure outside the loop
custom_colormap = [177 217 229; 52 73 100]/255;

% Loop over each temperature in the temperature list
for idx = 1:length(T_list)
    T = T_list(idx);

    % Perform multiple simulations for statistical averaging
    for i = 1:10
        [spins, energy(i, idx)] = solveIsing(N, T, J);  % Call the function
        magnetization(i, idx) = abs(mean(spins(:))); % Compute mean magnetization directly
    end

    % Calculate the mean of the results
    mean_magnetization(idx) = mean(magnetization(:, idx));
    mean_energy(idx) = mean(energy(:, idx));
    
    % Plot the spins directly
    subplot(4, 4, idx); % 4 rows, 4 columns
    imagesc(spins);
    colormap(custom_colormap);
    axis equal
    title(['$k_BT=$', num2str(round(T,2)), ...
        ', $|m|=$', num2str(round(mean_magnetization(idx),2))], ...
        'Interpreter', 'latex'); 
    set(gca,'XTick',[], 'YTick', []);
    axis tight
end

savefig('2d_spins.fig'); 

% Plot mean magnetization
figure(821); % Create a new figure for the magnetization plot
plot(T_list, mean_magnetization, 'ko--');
xlabel('Temperature $(k_BT)$', 'Interpreter', 'latex');
ylabel('Magnetization $(m)$', 'Interpreter', 'latex');
savefig('2d_magnetization_plot.fig'); 

% Plot mean energy
figure(822); % Create a new figure for the energy plot
plot(T_list, mean_energy, 'ko--');
xlabel('Temperature $(k_BT)$', 'Interpreter', 'latex');
ylabel('Energy $(E)$', 'Interpreter', 'latex');
savefig('2d_energy_plot.fig'); 

function [spins, energy] = solveIsing(N, T, J)
    % Initialize a spin configuration
    spins = ones(N);

    % Number of simulation steps
    num_steps = 200*N^2;

    % Metropolis algorithm simulation
    for step = 1:num_steps
        % Randomly choose a lattice point
        i = randi([1, N]);
        j = randi([1, N]);

        % Calculate energy change
        delta_E = 2 * J * spins(i, j) * ( ...
            spins(mod(i - 2, N) + 1, j) + spins(mod(i, N) + 1, j) + ...
            spins(i, mod(j - 2, N) + 1) + spins(i, mod(j, N) + 1));

        % Metropolis acceptance criterion
        if rand() < exp(-delta_E / T)
            spins(i, j) = -spins(i, j);
        end
    end

    energy = 0; % Initialize the energy
    for i=1:N-1
        for j=1:N-1
            energy = energy - J * spins(i,j) * ( ...
                spins(i,j+1) + spins(i+1,j));
        end
    end
end
