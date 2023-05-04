"""
 Module view for root app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party
from django.shortcuts import render

# internal
# ------------------------------------------------------------------


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    print("======handler404=========")
    return render(request, "errors/404.html", status=404)