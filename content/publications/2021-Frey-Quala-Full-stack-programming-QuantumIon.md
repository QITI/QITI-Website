---
title: "Programming the full stack of an open-access
quantum computer"
authors: [['Virginia Frey'], ['Richard Rademacher'], ['Elijah Durso-Sabina'], ['Noah Greenberg'],['Nikolay Videnov','nnvideno'],['Matthew L. Day','m9day'], ['Rajibul Islam', 'krislam'],['Crystal Senko']]
link: 
journal:
volume:
issue:
date: 2021-06-11T00:00:00-00:00
DOI: 
draft: false
arXiv: "2106.06549"
tags:
 - "QITI" 
image: "images/publications/2021-Frey-Quala.png"
---

This manuscript describes the full stack programming of QuantumION, an open-access, remote-controlled, trapped-ion quantum information processor for the research community, currently being developed at Waterloo. QuantumION is a joint initiative with Prof. Crystal Senko's research group and funded by Canada First Research Excellence Fund (CFREF).

**Abstract:** We present a new quantum programming language
called ‘Quala’ that enables true full-stack programming of quantum
hardware. Quala allows seamless integration of abstraction
layers such as the digital circuit layer and the analog control pulse
waveform layer. Additionally, the language supports user-issued
low-level hardware instructions like FPGA actions. Mid-circuit
measurements and branching decision logic support real-time,
adaptive programs. This flexibility allows users to write code for
everything from quantum error correction to analog quantum
simulation. The combination of a user-facing calibration database
and a powerful symbolic algebra framework provides users with
an unprecedented level of expressiveness and transparency. We
display the salient characteristics of the language structure and
describe how the accompanying compiler can translate programs
written in any abstraction layer into precisely timed hardware
commands. We intend for this language to bridge the gap
between circuit-level programming and physical operations on
real hardware while maintaining full transparency in each level
of the stack. This eliminates the need for “behind-the-scenes”
compilation and provides users with insights into the day-to-day
calibration routines.