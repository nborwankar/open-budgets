define([
    'uijet_dir/uijet',
    'resources',
    'project_widgets/ClearableTextInput',
    'project_widgets/Breadcrumbs'
], function (uijet, resources) {

    uijet.Resource('Breadcrumbs', uijet.Collection({
        model   : resources.Node
    }))
    .Resource('NodesListState', uijet.Model());

    uijet.declare([{
        type    : 'Pane',
        config  : {
            element     : '#nodes_picker',
            position    : 'fluid',
            resource    : 'NodesListState',
            data_events : {
                'change:search' : '-search.changed'
            }
        }
    }, {
        type    : 'Pane',
        config  : {
            element     : '#nodes_filters_pane',
            mixins      : ['Layered'],
            position    : 'top:100 fluid',
            app_events  : {
                'nodes_search.entered'  : 'wake',
                'nodes_search.cancelled': 'wake'
            }
        }
    }, {
        type    : 'Button',
        config  : {
            element : '#filters_done'
        }
    }, {
        type    : 'Button',
        config  : {
            element : '#filters_search'
        }
    }, {
        type    : 'Pane',
        config  : {
            element     : '#nodes_search_pane',
            mixins      : ['Layered'],
            dont_wake   : true,
            position    : 'top:100 fluid',
            app_events  : {
                'filters_search.clicked': 'wake'
            }
        }
    }, {
        type    : 'ClearableTextInput',
        config  : {
            element     : '#nodes_search',
            resource    : 'NodesListState',
            dom_events  : {
                keyup   : function (e) {
                    var code = e.keyCode || e.which,
                        value = e.target.value;
                    // enter key
                    if ( code === 13 ) {
                        this.publish('entered')
                    }
                    // esc key
                    else if ( code === 27 ) {
                        this.resource.set({ search : '' });
                        this.$element.val('');
                        this.publish('cancelled');
                    }
                    else {
                        this.resource.set({ search : value });
                    }
                }
            },
            signals     : {
                post_wake   : function () {
                    this.$element.focus();
                }
            },
            app_events  : {
                'nodes_search_clear.clicked': function () {
                    this.resource.set({ search : '' });
                }
            }
        }
    }, {
        type    : 'Breadcrumbs',
        config  : {
            element     : '#nodes_breadcrumbs',
            resource    : 'Breadcrumbs',
            data_events : {
                change  : 'render',
                reset   : 'render'
            },
            app_events  : {
                'nodes_list.selected'   : function (selected) {
                    this.resource.reset(
                        uijet.Resource('LatestTemplate').branch(selected)
                    );
                }
            }
        }
    }, {
        type    : 'Button',
        config  : {
            element     : '#search_crumb',
            app_events  : {
                'search.changed': function (data) {
                    this.$element.text(data.args[1]);
                }
            }
        }
    }]);
    
});