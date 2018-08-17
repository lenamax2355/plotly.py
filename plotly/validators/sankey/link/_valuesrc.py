import _plotly_utils.basevalidators


class ValuesrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(
        self, plotly_name='valuesrc', parent_name='sankey.link', **kwargs
    ):
        super(ValuesrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )