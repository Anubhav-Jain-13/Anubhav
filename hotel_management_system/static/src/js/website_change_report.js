/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";
import PortalSidebar from "@portal/js/portal_sidebar";

PortalSidebar.include({
    selector: ".o_portal_purchase_sidebar",

    init: function (parent, options) {
        this._super.apply(this, arguments);
        console.log("Custom functionality: PurchasePortalSidebar initialized");
    },

    start: function () {
        this.$el.css('background-color', '#34ebcf');
        this.$el.css('border-radius', '15px');

        let element = document.querySelector(".col-lg-3.col-xl-4.d-print-none");
        if (element) {
            element.style.backgroundColor = '#d141bb';
            element.style.borderTopLeftRadius = '15px';
            element.style.borderBottomLeftRadius = '15px';
            element.addEventListener('click', function(){
                alert("It's a Sidebar of Purchase Orders")
            })
           let button = document.createElement('button');
                button.textContent = "Click me";
                element.appendChild(button);

        } else {
            console.warn("Element with class 'col-lg-3 col-xl-4 d-print-none' not found");
        }
    },
});
