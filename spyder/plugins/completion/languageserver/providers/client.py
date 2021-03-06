# -*- coding: utf-8 -*-

# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

"""Spyder Language Server Protocol Client client handler routines."""

import logging

from spyder.plugins.completion.manager.api import LSPRequestTypes
from spyder.plugins.completion.languageserver.decorators import (
    handles, send_response)

logger = logging.getLogger(__name__)


class ClientProvider:
    @handles(LSPRequestTypes.CLIENT_REGISTER_CAPABILITY)
    @send_response
    def handle_register_capability(self, params):
        """TODO: Handle the glob patterns of the files to watch."""
        logger.debug('Register Capability: {0}'.format(params))
        return {}
