from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool

class Address(ModelSQL, ModelView):
    "Address"
    _name = 'party.address'
    _description = __doc__
    
    google = fields.Function(fields.Char('map'), 'get_function_google')
    
    def get_function_google(self, ids, names):
        addr_object = Pool().get('party.address')
        result = {}
        res = {}
        for name in names:
            for id in ids:
                addr = addr_object.browse(id)
                str = addr.street
                city = addr.city
                country = addr.country.name
                res[id] = 'https://maps.google.com/maps?f=q&source=s_q&hl=de&geocode=&q=%s,+%s,+%s' % (str, city, country)
            
            result[name] = res
            
        return result

Address()