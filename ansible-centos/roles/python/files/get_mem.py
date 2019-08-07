#!/usr/bin/env python
# -*- coding:utf-8 -*-

import psutil

result = psutil.virtual_memory().percent
print result
