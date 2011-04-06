from django import template

register = template.Library()

class InstallNode(template.Node):
    def render(self, context):
        return """
        navigator.apps.install({
                url: "",
                onsuccess: function(){
                        installed = null;
                        alert("Installed %s.");
                        },
                onerror: function(){
                        alert("Couldn't install %s.);
                        }
        });
        """

@register.tag
def appetizer_install(parser, token):
    return InstallNode()


