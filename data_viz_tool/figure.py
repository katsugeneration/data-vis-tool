from typing import List
import matplotlib.pyplot as plt
import matplotlib.figure
from matplotlib.dates import date2num, DateFormatter


def create_bar_and_plot_fig(
        x: List,
        bar_y: List,
        plot_y: List,
        title: str = '',
        bar_label: str = '',
        plot_label: str = '',
        xlabel: str = '',
        bar_ylabel: str = '',
        plot_ylabel: str = '',
        x_type: str = '') -> matplotlib.figure.Figure:
    """Create bar and plot axes figure.

    Args:
        x: x label data.
        bar_y: bar axis y data.
        plot_y: plot axis y data.
        title: figure title.
        bar_label: bar label string for legend.
        plot_label: plot label string for legend.
        xlabel: x label description.
        bar_ylabel: bar x label description.
        plot_ylabel: plot x label description.
        x_type: x label type. case date, x data process as date string.

    Return:
        fig (Figure): matplotlib figure object.

    """
    fig = plt.figure(figsize=(16.0, 9.0))
    ax1 = fig.add_subplot(1, 1, 1)
    ax2 = ax1.twinx()

    _x = x
    if x_type == 'date':
        _x = date2num(x)
    ax1.bar(_x, bar_y, label=bar_label, color='C0', align="center")
    ax2.plot(_x, plot_y, label=plot_label, color='C1', marker='o')


    if x_type == 'date':
        ax1.set_xticks(x)
        ax1.xaxis.set_major_formatter(DateFormatter('%m-%d'))
        ax1.xaxis_date()
        fig.autofmt_xdate(rotation=90)
    ax1.set_title(title)
    ax1.legend(loc="best")
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(bar_ylabel)
    ax2.set_ylabel(plot_ylabel)
    ax2.set_ylim(ymin=0)

    return fig