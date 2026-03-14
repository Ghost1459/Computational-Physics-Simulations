# Computational Physics & Complex Systems Simulations

A curated collection of numerical methods, deterministic simulations, and stochastic models developed during my coursework. 

### 🛠️ Tech Stack & Tools
* **Language:** Python
* **Libraries:** NumPy, SciPy, Matplotlib (Pyplot & FuncAnimation), ImageIO
* **Optimization:** Numba (`@jit` compilation for high-performance Monte Carlo steps)
* **Environment:** Jupyter Notebooks (`.ipynb`)

---

## 📊 Visual Gallery

The following animations illustrate emergent behavior and physical transitions across different modules.

| Sandpile SOC | Wa-Tor Predator-Prey |
| :---: | :---: |
| <img src="./results/gifs/12_sandpile_avalanche_model_center_supercritical.gif" width="400"/> | <img src="./results/gifs/13_wator_ocean.gif" width="400"/> |
| *Avalanches in a critical state.* | *Agent-based population dynamics.* |

| Ising Model: Domain Growth | Ising Model: Periodic Borders |
| :---: | :---: |
| <img src="./results/gifs/09_metropolis.gif" width="400"/> | <img src="./results/gifs/09_metropolis_borders.gif" width="400"/> |
| *Metropolis algorithm domain formation.* | *Phase separation and boundary evolution.* |

| Thermodynamics: Liquid State | Thermodynamics: Solid State |
| :---: | :---: |
| <img src="./results/gifs/06_thermostat_liquid.gif" width="400"/> | <img src="./results/gifs/06_thermostat_solid.gif" width="400"/> |
| *Isokinetic thermostat (Fluid).* | *Lattice stability under temperature control.* |

| Fractal Growth (DLA) | N-Body Orbital Mechanics |
| :---: | :---: |
| <img src="./results/gifs/10_aggregation_growth_p=05_M=10.gif" width="400"/> | <img src="./results/gifs/04_chenciner_figure.gif" width="400"/> |
| *Diffusion-Limited Aggregation.* | *Stable Chenciner 3-body orbit.* |

---

## 🔬 Core Modules & Simulations

### 1. Complex Systems & Emergent Behavior
* **Agent-Based Modeling (`13_wator_predator_prey_model.ipynb`):** Utilized Object-Oriented Programming (OOP) to define interacting classes (Ocean, Animals) and simulate Lotka-Volterra population cycles on a toroidal grid.
* **Self-Organized Criticality (`12_bak_tang_wiesenfeld_sandpile.ipynb`):** Implemented the BTW sandpile model to study avalanche distributions, extracting power-law statistics via logarithmic binning and curve fitting.
* **Partial Differential Equations (`11_gray_scott_reaction_diffusion.ipynb`):** Solved coupled PDEs using numerical integration and Laplacian operators (via optimized array rolling) to simulate Turing pattern formation.
* **Diffusion-Limited Aggregation (`10_dla_growth_simulation.ipynb`):** Modeled fractal growth patterns driven by random walkers adhering to a central seed structure.

### 2. Molecular Dynamics & Thermodynamics
* **Lennard-Jones Gas (`05_lennard_jones_molecular_dynamics.ipynb`):** Simulated interacting particles in a 2D box, implementing periodic boundary conditions and force-calculation algorithms.
* **Isokinetic Thermostat (`06_isokinetic_thermostat_md.ipynb`):** Engineered a thermostat algorithm to regulate kinetic energy, validating the conservation of total system energy over time.

### 3. Stochastic Models & Monte Carlo Methods
* **Ising Model (`08_ising_model_metropolis.ipynb`):** Modeled magnetic dipole alignment via Metropolis kinetics, utilizing `Numba` JIT compilation to heavily optimize nested coordinate loops and probability evaluations.
* **Domain Growth Kinetics (`09_domain_growth_kinetics.ipynb`):** Compared domain growth speeds using Metropolis vs. Kawabata algorithms, plotting power-law scaling across time steps.

### 4. Chaos Theory & Orbital Mechanics
* **Duffing Oscillator (`02_duffing_oscillator_chaos.ipynb`, `02_interactive_duffing_ui.py`):** Solved non-linear differential equations using `scipy.integrate.solve_ivp` to map phase-space trajectories and chaotic attractors. Built an interactive UI with `matplotlib.widgets`.
* **N-Body Problem (`04_nbody_orbital_mechanics.ipynb`):** Solved the equations of motion for planetary bodies, recreating the famous stable Chenciner "figure-eight" orbit.

### 5. Fractals & Network Theory
* **Fractal Dimensions (`03_fractal_dimension_analysis.ipynb`):** Generated Sierpinski triangles and Barnsley ferns; calculated fractal dimensions using the box-counting method and `scipy.optimize.curve_fit`.
* **Percolation Phase Transitions (`07_percolation_phase_transitions.ipynb`):** Analyzed random networks via lattice clustering algorithms (Breadth-First Search queue logic) to identify critical percolation thresholds.

---

## 🚀 How to Run

Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/Ghost1459/Computational-Physics-Simulations.git](https://github.com/Ghost1459/Computational-Physics-Simulations.git)
cd Computational-Physics-Simulations
pip install numpy scipy matplotlib numba imageio jupyter
jupyter notebook
