"""
 Module view for home app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render

# internal
# ------------------------------------------------------------------


def index(request):
    """
    main view return to home app
    """
    return render(request, 'home/index.html')
