import pynvim
from datetime import date

@pynvim.plugin
class Plugin(object):
    def __init__(self, vim):
        self.vim = vim
    
    @pynvim.command('Date')
    def date(self):
        self.vim.command(f'echo "{date.today()}"')
