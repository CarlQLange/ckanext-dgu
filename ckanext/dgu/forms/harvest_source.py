import formalchemy
from formalchemy import helpers as fa_h
from sqlalchemy.util import OrderedDict

from ckan.forms.builder import FormBuilder
import ckan.model as model
from ckan.forms import common
import ckan.lib.helpers as h
from ckan.lib.helpers import literal

__all__ = ['get_harvest_source_fieldset']

def harvest_source_url_validator(val, field=None):
    if not val.strip().startswith('http://'):
        raise formalchemy.ValidationError('Harvest source URL is invalid (must start with "http://").')

def build_harvest_source_form():
    builder = FormBuilder(model.HarvestSource)
    builder.set_field_text('url', 'Location (required)', literal("<br/><strong>URL</strong> for source of metadata.<br/>"))
    builder.set_field_option('url', 'validate', harvest_source_url_validator)
    builder.set_field_option('description', 'textarea', {'size':'60x15'})
    displayed_fields = ['url', 'description']
    builder.set_displayed_fields(OrderedDict([('Details', displayed_fields)]))
    builder.set_label_prettifier(common.prettify)
    return builder  

fieldsets = {}
def get_harvest_source_fieldset(name='harvest_source_fs'):
    if not fieldsets:
        fieldsets['harvest_source_fs'] = build_harvest_source_form().get_fieldset()
    return fieldsets[name]

