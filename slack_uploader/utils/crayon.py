from colorful import Colorful


class ColorfulWrapper(Colorful):
    """
    Description
    -----------
        A wrapper class for our Colorful module

    Arguments
    ---------
        style_type : str
            The color style we want to make use
    """
    
    def __init__(self, style_type="monokai"):
        self.use_style(style_type)
    
    