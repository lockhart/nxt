# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, View
from django.http import StreamingHttpResponse, Http404
from django.contrib import messages
from django.conf import settings
from django.utils.timezone import now
import logging


logger = logging.getLogger(__name__)


class ProfileView(TemplateView):
    template_name='membership/detail.html'
    pass
