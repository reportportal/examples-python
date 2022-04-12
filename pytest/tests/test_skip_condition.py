#  Copyright (c) 2022 https://reportportal.io .
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License
"""Example tests with different skip conditions."""
import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 0),
                    reason="requires python3 or higher")
def test_skip_python_2_7(rp_logger):
    rp_logger.info("The test should not run on python 2.7")
    assert True


@pytest.mark.skipif(sys.version_info > (2, 7),
                    reason="requires python3 or higher")
def test_skip_python_3_and_higher(rp_logger):
    rp_logger.info("The test should not run on python3 and higher")
    assert True
