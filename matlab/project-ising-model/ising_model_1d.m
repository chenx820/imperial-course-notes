clear;  % Clear workspace

% Parameters
N = 100;          % Number of lattice points
J = 1;            % Exchange coupling constant
T_list = linspace(0.001, 5, 50);    % Temperature (kT)

mean_magnetization = zeros(1, length(T_list));  % Initialize the magnetization
mean_energy = zeros(1, length(T_list));         % Initialize the energy

magnetization = zeros(10, length(T_list)); % Preallocate array to store magnetization results
energy = zeros(10, length(T_list));        % Preallocate array to store energy results

% Loop over each temperature in the temperature list
for idx = 1:length(T_list)
    T = T_list(idx);
    
    % Perform multiple simulations for statistical averaging
    for i = 1:10
        [spins, energy(i, idx)] = solveIsing(N, T, J);  % Call the function to simulate Ising model
        magnetization(i, idx) = abs(mean(spins(:)));
    end

    % Calculate the mean of the results
    mean_magnetization(idx) = mean(magnetization(:, idx));
    mean_energy(idx) = mean(energy(:, idx));
end

% Plot the mean energy versus temperature
figure(420);
plot(T_list, mean_energy, 'ko--');
xlabel('Temperature $(k_BT)$', 'Interpreter', 'latex');
ylabel('Energy $(E)$', 'Interpreter', 'latex');
savefig('1d_energy_plot.fig'); 

% Plot the mean magnetization versus temperature
figure(421); % Create a new figure for the magnetization plot
plot(T_list, mean_magnetization, 'ko--');
xlabel('Temperature $(k_BT)$', 'Interpreter', 'latex');
ylabel('Magnetization $(m)$', 'Interpreter', 'latex');
savefig('1d_magnetization_plot.fig'); 

% Function to simulate the Ising model using the Metropolis algorithm
function [spins, energy] = solveIsing(N, T, J)
    % Initialize a spin configuration 
    spins = ones(1, N);

    % Number of simulation steps
    num_steps = 200*N;

    % Metropolis algorithm simulation
    for step = 1:num_steps
        % Randomly choose a lattice point
        i = randi([1, N]);

        % Calculate energy change
        delta_E = 2 * J * spins(i) * ( ...
            spins(mod(i - 2, N) + 1) + spins(mod(i, N) + 1));

        % Metropolis acceptance criterion
        if rand() < exp(-delta_E / T)
            spins(i) = -spins(i);
        end
    end

    energy = 0; % Initialize the energy
    for i=1:N-1
        energy = energy - J * spins(i) * spins(i+1);
    end
end

