######################################################################
# BioSimSpace: Making biomolecular simulation a breeze!
#
# Copyright 2017-2018
#
# Authors: Lester Hedges

# BioSimSpace is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# BioSimSpace is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BioSimSpace. If not, see <http://www.gnu.org/licenses/>.
#####################################################################

"""
Tools for plotting data.
Author: Lester Hedges
"""

from BioSimSpace import _is_interactive

from Sire import try_import

from warnings import warn

try:
    matplotlib = try_import("matplotlib")
    import matplotlib.pyplot as plt
    _has_matplotlib = True
except ImportError:
    _has_matplotlib = False

__all__ = ["plot"]

if _has_matplotlib:
    # Define font sizes.
    SMALL_SIZE = 14
    MEDIUM_SIZE = 16
    BIGGER_SIZE = 18

    # Set font sizes.
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

def plot(x=None, y=None, xlabel=None, ylabel=None, logx=False, logy=False):
    """A simple function to create x/y plots with matplotlib.

       Keyword arguments:

       x      -- A list of x data values.
       y      -- A list of y data values.
       xlabel -- The x axis label string.
       ylabel -- The y axis label string.
       logx   -- Whether the x axis is logarithmic.
       logy   -- Whether the y axis is logarithmic.
    """

    # Make sure were running interactively.
    if not _is_interactive():
        warn("You can only use BioSimSpace.Notebook.plot when running interactively.")
        return None

    # Matplotlib failed to import.
    if not _has_matplotlib:
        warn("BioSimSpace.Notebook.plot is disabled as matplotlib failed "
            "to load. Please check your matplotlib installation.")
        return None

    if x is None:
        if y is None:
            raise ValueError("'y' data must be defined!")
        else:
            if type(y) is not list:
                raise TypeError("'y' must be of type 'list'")
            # No x data, use array index as value.
            x = [x for x in range(0, len(y))]

    if type(x) is not list:
        raise TypeError("'x' must be of type 'list'")

    if len(x) != len(y):
        raise ValueError("Mismatch in list sizes: len(x) = %d, len(y) = %d"
            % (len(x), len(y)))

    if xlabel is not None:
        if type(xlabel) is not str:
            raise TypeError("'xlabel' must be of type 'str'")

    if ylabel is not None:
        if type(ylabel) is not str:
            raise TypeError("'ylabel' must be of type 'str'")

    # Set the figure size.
    plt.figure(figsize=(8, 6))

    # Create the plot.
    plt.plot(x, y, "-bo")

    # Add axis labels.
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)

    # Scale the axes.
    if logx:
        plt.xscale("log")
    if logy:
        plt.yscale("log")

    # Turn on grid.
    plt.grid()

    return plt.show()
