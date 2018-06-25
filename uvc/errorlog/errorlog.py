# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import os
import datetime
import grokcore.error
import zope.publisher.interfaces.http


_request_iface = zope.publisher.interfaces.http.IHTTPApplicationRequest

def _make_extra(request=None):
    if request is None:
        return None
    if not _request_iface.providedBy(request):
        return None
    host = request.getHeader(
        'HTTP_X_FORWARDED_FOR', request.getHeader('REMOTE_ADDR'))
    principal = request.principal
    auth = principal and principal.id or '',
    extra_data = {
        'url': request.getURL(),
        'method': request.method,
        'host': host,
        'auth': auth,
        'program': 'grok',
        'customer': os.environ.get('CUSTOMER', 'NN'),
        'timestamp': datetime.datetime.now().isoformat() 
    }
    print extra_data
    return extra_data


class GELFLoggingErrorReporting(grokcore.error.LoggingErrorReporting):

    def make_extra(self, request=None):
        return _make_extra(request)
