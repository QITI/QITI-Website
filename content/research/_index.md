---
title: "Research"
date: 2020-05-10T15:07:47-04:00
draft: false
nav: [ "QSIM", "Assembly", "Resources", "Outreach"]
---
<a id="QSIM"></a>
# Quantum Simulation With Trapped Ions
Many outstanding problems of modern physics involve understanding the origin and properties of strongly interacting quantum systems. Such correlated quantum systems – such as the high-Tc superconductors and quark-gluon plasma in a particle collider –  are present in various energy scales. In an interacting quantum system, entanglement or non-classical correlations between parts often makes theoretical or numerical analysis intractable. An experimental way to solve this problem is to simulate quantum models using well-controlled quantum systems in the laboratory. In these experimental ‘quantum simulators’, it is possible to add complexities and increase the system size in a controlled way. The long quantum coherence in these systems allow their temporal evolution following the quantum laws of nature. The task of the experimentalist is then to initialize the system in a known state, engineer the desired quantum Hamiltonian, let the system evolve in isolation from its environment, and finally measure the outcome. The knowledge gained from studying non-trivial quantum models can potentially lead to the understanding of exotic quantum phases of matter, and give fundamental insights towards realizing quantum computers.

The main research focus of the QITI laboratory is to use laser-cooled trapped Ytterbium ions (Yb+) to simulate non-trivial quantum Hamiltonians. The long range Coulomb interaction between the ions would be exploited to engineer versatile spin Hamiltonians. The spin interactions can be tuned, in principle arbitrarily, and the individual spins can be detected with near perfection. Multi-spin interactions can be created, allowing us to study interacting (spinless) Fermions. Further, the phonons associated with the collective vibrational modes enable us to study interacting bosonic Hamiltonians, such as the Bose-Hubbard model. While trapped ions normally have long quantum coherence, one can introduce dissipation in a controlled way for studying open quantum systems. Interacting Hamiltonians and open quantum systems are often hard to simulate on classical computers, and may become intractable beyond 30-40 spins. The QITI laboratory aims to work in the regime where classical computation is difficult or intractable.

<a id="Assembly"></a>
# Assembling a quantum system atom-by-atom
Laser-cooled trapped ions are among the most pristine quantum systems that can be controlled in a laboratory. In the ultrahigh vacuum of an ion trap apparatus (a Paul trap), we can build a quantum system bottom-up, starting with just one ion, adding a second, a third, … going up to many dozens! The ions are laser-cooled (Doppler cooling, Raman cooling etc) to their electronic and vibrational ground states. Two internal states of an ion can be chosen to represent the qubit or spin-1/2 states. Microwave or optical (Raman) fields can be used to generate an effective magnetic field that rotates the spins. Spin-dependent fluorescence when excited by a laser beam allows us to detect the spin states with near perfection. Quantum coherence of up to fifteen minutes has been demonstrated in a single trapped ion! The long coherence is exploited in building atomic clocks.

Now, let’s add a second ion to the trap. The Coulomb repulsion between the ions separates them by a micron or more for typical ion trapping parameters. So, they (i.e. their fluorescence) can be optically resolved with a moderate resolution microscope objective. The strong Coulomb repulsion and the external trap also generates collective vibrational modes (aka the normal modes). We can couple the spin states of each ion to these normal modes by precisely tuned laser fields, via stimulated Raman transitions. Since the normal modes are shared between various spins, they effectively generate couplings between spins, giving rise to quantum spin models. The interactions can be adiabatically turned on to prepare the (entangled) ground state of the Hamiltonian, an approach known as adiabatic quantum simulation. Or, quantum logic gates can be built by keeping the interactions on (and using single spin manipulation) for some time.

Similarly, we can populate the trap with more spins. When there are more than two spins,  couplings between spin-pairs can compete with each other. Imagine three spins sitting on the corner of a triangle and trying to align anti-parallel to each other! This competition, known as frustration, enriches the many-body spin phases. Also, complicated Hamiltonians such as multi-spin interactions can be broken into quantum logic gates between pairs of spin, an approach known as digital quantum simulation.

In the QITI laboratory, we aim to manipulate individual spins by adaptive optics, and engineer fully connected spin systems to investigate the phases and non-equilibrium dynamics of quantum many-body systems.

<a id="Resources"></a>
# Resources
## Ion Searching for new ion species

There are a fairly well established set of atomic species used in trapped ion experiments. These have primarily been used due to favorable features, and partially used because of momentum (i.e. everyone else is using them). However there does not exist a resource which writes down explictely why the ions we use are the best for the experiments we perform. The introduction of 133Ba+ was due to an enterprising postdoc who pointed out its favourable properties - are there other ions that we are overlooking?

To answer this question we will perform a semi-exhaustive search of the periodic table. The features we will filter by are:

1. '''F=0 and F=1 hyperfine sub-levels in the ground state''' For easy state preparation, minimal state leakage, and a well-defined qubit (examples: 133Ba+, 171Yb+)
2. '''Visible and near-infrared electronic transitions''' For easy optical control. Wavelengths in the UV suffer from harder optical engineering, wavelengths in the far-IR suffer from large diffraction limited spots (and being invisible). (examples: Sr+, Ba+, Ra+)
3. '''A metastable level''' For easy, and long-lived storage of quantum information, allowing for high-fidelity measurements or an alternative qubit transition.
4. '''A closed cycle cooling transition''' For laser cooling of ions into their motional ground state. Repumpers will normally always be required, but there should not be too many of them.
5. '''Non-radioative isotopes''' For easy handling of the atomic source (for example: 171Yb+).

With these criteria in mind we will now explore the periodic table making notes:

* Criterion 1 can only be satisfied by isotopes with spin-1/2 nuclei and an J=1/2 ground state.
* The further right we go in the periodic table the harder the atoms are to ionise.
* Removing electrons from an atom nearly always decreases transition wavelengths, looking at secondary ionisations does not help satisfy criteria 2.
* Increasing in mass down a column of the periodic table nearly always increases the transition wavelengths.

We will begin with an overview of the periodic table, using isotope data from the NIST database to identify favourable isotopes. We will then use NIST database data for atomic transitions to explore the electronic structure to answer the other criteria. The code used to do this is located [here](https://github.com/senkolab/ion-species-explorer).


<a id="Outreach">
# Outreach

## Coop highlight
## Some skills we've taught the student body
## Dust trap

