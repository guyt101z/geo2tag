var Plugin = Backbone.Model.extend({});

var plugin = new Plugin({
    title: "Plugin"
});

var PluginList = Backbone.Collection.extend({
    model: Plugin,
    url: function(){
        return '/instance/plugins;
    }
});

var PluginView = Backbone.View.extend({
    tagName: "div",
    id: "container_plugin_list",
    render: function(json) {
        $('#' + this.id).append(get_plugin_display(json));
        return this;
    },
    clear: function(){
        $('#' + this.id).empty();
    }
});

plugin_view = new PluginView({'model' : plugin});

var PluginPageModel = Backbone.Model.extend({
    initialize: function() {
        this.plugins = new PluginList();       
    }
});

plugin_list_page = new PluginPageModel;

var PluginPageView = Backbone.View.extend({
    initialize:function(){
        this.refresh();
    },

    refresh: function() {
        this_ = this;
        this.model.fetch({
            success: function(){
                this_.render();
            }
        });
    },
    render: function() {
        plugin_view.clear();
        for(var i = 0; i < this.model.length; i++)
            plugin_view.render(this.model.at(i).attributes);
    }
});

var plugin_page = new PluginPageView({model: plugin_list_page.plugins});

function get_plugin_display(json){

}
