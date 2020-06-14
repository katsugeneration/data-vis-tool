from nose.tools import ok_, eq_
import os
import datetime
import data_viz_tool.figure


class TestFigure:
    def test_create_bar_and_plot_fig(self):
        fig = data_viz_tool.figure.create_bar_and_plot_fig(
            x = [1., 2.],
            bar_y = [1.0, 2.0],
            plot_y = [0.8, 0.6])
        fig.savefig('test.png')
        ok_(os.path.exists('test.png'))
        os.remove('test.png')

    def test_create_bar_and_plot_fig_case_date(self):
        fig = data_viz_tool.figure.create_bar_and_plot_fig(
            x = [datetime.date.fromisoformat('2020-05-10'), datetime.date.fromisoformat('2020-05-17')],
            bar_y = [1.0, 2.0],
            plot_y = [0.8, 0.6],
            x_type = 'date')
        fig.savefig('test.png')
        ok_(os.path.exists('test.png'))
        os.remove('test.png')
