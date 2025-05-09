from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('Qualquer coisa')
lp.log_success('Deu bom')    
lf = LogFileMixin()
lf.log_error('Qualquer coisa')
lf.log_success('Deu bom')        
