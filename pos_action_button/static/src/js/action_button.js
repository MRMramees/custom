odoo.define('pos_action_button.ActionButton', function (require) {
"use strict";

// require pos screens
var pos_screens = require('point_of_sale.screens');

// create a new button by extending the base ActionButtonWidget
var DashboardButton = pos_screens.ActionButtonWidget.extend({
    template: 'DashBoardButton',
    button_click: function(){
        var order = this.pos.get_order();
        order.get_selected_orderline().set_discount(5);
    },
});

// define the dashboard button
pos_screens.define_action_button({
    'name': 'Dashboard',
    'widget': DashboardButton,
    'condition': function(){return this.pos;},
});

});