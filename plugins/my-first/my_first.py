# This is the class you derive to create a plugin
from airflow.plugins_manager import AirflowPlugin

from flask import Blueprint
from flask_appbuilder import expose, BaseView as AppBuilderBaseView

# Importing base classes that we need to derive
from airflow.hooks.base_hook import BaseHook
from airflow.models import BaseOperator
from airflow.models.baseoperator import BaseOperatorLink
from airflow.sensors.base_sensor_operator import BaseSensorOperator

# Will show up under airflow.hooks.test_plugin.PluginHook
class PluginHook(BaseHook):
    pass

# Will show up under airflow.operators.test_plugin.PluginOperator
class PluginOperator(BaseOperator):
    pass

# Will show up under airflow.sensors.test_plugin.PluginSensorOperator
class PluginSensorOperator(BaseSensorOperator):
    pass

# Will show up under airflow.macros.test_plugin.plugin_macro
# and in templates through {{ macros.test_plugin.plugin_macro }}
def plugin_macro():
    pass

# Creating a flask blueprint to integrate the templates and static folder
bp = Blueprint(
    "test_plugin", 
    __name__,
    template_folder='templates', # registers airflow/plugins/templates as a Jinja template folder
    static_folder='static',
    static_url_path='/static/my-first')

# Creating a flask appbuilder BaseView
class TestAppBuilderBaseView(AppBuilderBaseView):
    default_view = "myview"

    @expose("/")
    def myview(self):
        return self.render_template("test.html", content="I am your plugin inserted in the current layout!")

v_appbuilder_view = TestAppBuilderBaseView()
v_appbuilder_package = {"name": "Test View",
                        "category": "Test Plugin",
                        "view": v_appbuilder_view}

# Creating a flask appbuilder Menu Item
appbuilder_mitem = {"name": "Google",
                    "category": "Search",
                    "category_icon": "fa-th",
                    "href": "https://www.google.com"}

# A global operator extra link that redirect you to google
class GoogleLink(BaseOperatorLink):
    name = "Google"

    def get_link(self, operator, dttm):
        return "https://www.google.com"

# Defining the plugin class
class AirflowTestPlugin(AirflowPlugin):
    name = "my-first"
    operators = [PluginOperator]
    sensors = [PluginSensorOperator]
    hooks = [PluginHook]
    macros = [plugin_macro]
    admin_views = []
    flask_blueprints = [bp]
    appbuilder_views = [v_appbuilder_package]
    appbuilder_menu_items = [appbuilder_mitem]
    global_operator_extra_links = [GoogleLink(),]
    operator_extra_links = []