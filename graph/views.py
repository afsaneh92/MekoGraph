from django.http import HttpResponse
from django.shortcuts import render
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import StringIO
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def index(request):
    return render(request, 'index.html')


def showimage(request):
    # Construct the graph
    t = arange(0.0, 2.0, 0.01)
    s = sin(2 * pi * t)
    plot(t, s, linewidth=1.0)

    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)

    # Store image in a string buffer
    buffer = StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")


def dashboard(request):
    np.random.seed(2000000)

    x = np.arange(0.0, 50.0, 2.0)
    y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
    s = np.random.rand(*x.shape) * 800 + 500

    plt.scatter(x, y, s, c="g", alpha=0.5, marker=r'$\clubsuit$', label='luck')
    plt.xlabel("leprechauns")
    plt.ylabel("gold")
    plt.legend(loc='upper left')
    plt.show()
    return render(
        request,
        'singleplot.html',
        {
            'plotDisp': plt
        }
    )

