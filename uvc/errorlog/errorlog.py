# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


import grokcore.error
import zope.publisher.interfaces.http


_request_iface = zope.publisher.interfaces.http.IHTTPApplicationRequest


class GELFLoggingErrorReporting(grokcore.error.LoggingErrorReporting):

    def make_extra(self, request=None):
        import pdb; pdb.set_trace()
        if request is None:
            return None
        if not _request_iface.providedBy(request):
            return None
        host = request.getHeader(
            'HTTP_X_FORWARDED_FOR', request.getHeader('REMOTE_ADDR'))
        extra_data = {
            'url': request.getURL(),
            'method': request.method,
            'host': host,
            'auth': request.principal.id,
            'customer': 'BGHW'
        }
        return extra_data
