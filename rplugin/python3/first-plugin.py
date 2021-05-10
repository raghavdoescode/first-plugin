import neovim
from datetime import date

@neovim.plugin
class Main(object):
    def __init__(self, vim):
       self.vim = vim 

    @neovim.function('date')
    def date(self):
        self.vim.cmd(f'echo "{date.today()}"')
