from trytond.model import ModelView, ModelSQL, fields

class LinkList(ModelSQL, ModelView):
    'LinkList'
    _name = 'browser.links'
    
    _description = __doc__
    name = fields.Char('Name')
    url = fields.Char('URL')
    
LinkList()