# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Utilities for mocking the IBMQ provider, including job responses and backends.

The module includes dummy provider, backends, and jobs.
The purpose of these classes is to fake backends for testing purposes:
testing local timeouts, arbitrary responses or behavior, etc.

The mock devices are mainly for testing the compiler.
"""

from .fake_provider import FakeProvider
from .fake_backend import FakeBackend
from .fake_job import FakeJob
from .fake_qobj import FakeQobj

from .fake_qasm_simulator import FakeQasmSimulator

from .fake_yorktown import FakeYorktown
from .fake_tenerife import FakeTenerife
from .fake_ourense import FakeOurense
from .fake_vigo import FakeVigo
from .fake_melbourne import FakeMelbourne
from .fake_rueschlikon import FakeRueschlikon
from .fake_tokyo import FakeTokyo
from .fake_poughkeepsie import FakePoughkeepsie
from .fake_almaden import FakeAlmaden
from .fake_singapore import FakeSingapore
from .fake_johannesburg import FakeJohannesburg
from .fake_boeblingen import FakeBoeblingen


from .fake_openpulse_2q import FakeOpenPulse2Q
