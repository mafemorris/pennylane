:orphan:

# Release 0.22.0-dev (development release)

<h3>New features since last release</h3>

* Continued development of the circuit-cutting compiler:

  A method for converting a quantum tape to a directed multigraph that is amenable
  to graph partitioning algorithms for circuit cutting has been added.
  [(#2107)](https://github.com/PennyLaneAI/pennylane/pull/2107)

  A method to replace `WireCut` nodes in a directed multigraph with `MeasureNode`
  and `PrepareNode` placeholders has been added.
  [(#2124)](https://github.com/PennyLaneAI/pennylane/pull/2124)

  A method has been added that takes a directed multigraph with `MeasureNode` and
  `PrepareNode` placeholders and fragments into subgraphs and a communication graph.
  [(#2153)](https://github.com/PennyLaneAI/pennylane/pull/2153)

  A differentiable tensor contraction function `contract_tensors` has been
  added.
  [(#2158)](https://github.com/PennyLaneAI/pennylane/pull/2158)

<h3>Improvements</h3>

<h3>Breaking changes</h3>

* The `MultiControlledX` operation now accepts a single `wires` keyword argument for both `control_wires` and `wires`.
  The single `wires` keyword should be all the control wires followed by a single target wire. 
  [(#2121)](https://github.com/PennyLaneAI/pennylane/pull/2121)

<h3>Deprecations</h3>

<h3>Bug fixes</h3>

<h3>Documentation</h3>

* The ``pennylane.numpy`` subpackage is now included in the PennyLane
  API documentation.
  [(#2179)](https://github.com/PennyLaneAI/pennylane/pull/2179)

* Improves the documentation of `RotosolveOptimizer` regarding the
  usage of the passed `substep_optimizer` and its keyword arguments.
  [(#2160)](https://github.com/PennyLaneAI/pennylane/pull/2160)

<h3>Contributors</h3>

This release contains contributions from (in alphabetical order):

Thomas Bromley, Anthony Hayes, Josh Izaac, Maria Fernanda Morris, David Wierichs
