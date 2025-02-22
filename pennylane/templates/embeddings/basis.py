# Copyright 2018-2021 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""
Contains the BasisEmbedding template.
"""
# pylint: disable-msg=too-many-branches,too-many-arguments,protected-access
import pennylane as qml
from pennylane.operation import Operation, AnyWires
from pennylane.wires import Wires


class BasisEmbedding(Operation):
    r"""Encodes :math:`n` binary features into a basis state of :math:`n` qubits.

    For example, for ``features=np.array([0, 1, 0])``, the quantum system will be
    prepared in state :math:`|010 \rangle`.

    .. warning::

        ``BasisEmbedding`` calls a circuit whose architecture depends on the binary features.
        The ``features`` argument is therefore not differentiable when using the template, and
        gradients with respect to the argument cannot be computed by PennyLane.

    Args:
        features (tensor_like): binary input of shape ``(n, )``
        wires (Iterable): wires that the template acts on

    Example:

        Basis embedding encodes the binary feature vector into a basis state.

        .. code-block:: python

            dev = qml.device('default.qubit', wires=3)

            @qml.qnode(dev)
            def circuit(feature_vector):
                qml.BasisEmbedding(features=feature_vector, wires=range(3))
                return qml.state()

            X = [1,1,1]

        The resulting circuit is:

        >>> print(qml.draw(circuit)(X))
            0: ──X──╭┤ State
            1: ──X──├┤ State
            2: ──X──╰┤ State

        And, the output state is:

        >>> print(circuit(X))
            [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 1.+0.j]

        Thus, ``[1,1,1]`` is mapped to :math:`|111 \rangle`.

    """

    num_wires = AnyWires
    grad_method = None

    def __init__(self, features, wires, do_queue=True, id=None):

        wires = Wires(wires)
        shape = qml.math.shape(features)

        if len(shape) != 1:
            raise ValueError(f"Features must be one-dimensional; got shape {shape}.")

        n_features = shape[0]
        if n_features != len(wires):
            raise ValueError(f"Features must be of length {len(wires)}; got length {n_features}.")

        features = list(qml.math.toarray(features))

        if not set(features).issubset({0, 1}):
            raise ValueError(f"Basis state must only consist of 0s and 1s; got {features}")

        super().__init__(features, wires=wires, do_queue=do_queue, id=id)

    @property
    def num_params(self):
        return 1

    def expand(self):

        features = self.parameters[0]

        with qml.tape.QuantumTape() as tape:

            for wire, bit in zip(self.wires, features):
                if bit == 1:
                    qml.PauliX(wire)

        return tape
