# This module contains built-in introspector plugins for various common
# Django apps.

# These imports trigger the lower-down files
import south.introspection_plugins.geodjango
# This interferes with our own 'tagging' app
#import south.introspection_plugins.django_tagging
import south.introspection_plugins.django_taggit
import south.introspection_plugins.django_objectpermissions
import south.introspection_plugins.annoying_autoonetoone

