/* @odoo-module */

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class MyOrderlineDiscount extends Component {
    static template = "point_of_sale.MyOrderlineDiscount";

    setup() {
        this.pos = usePos();
        this.popup = useService("popup");
        this.orm = useService('orm')
    }
//    async onClick() {
//        const selectedOrders = this.pos.get_order().get_orderlines();
//        console.log(selectedOrders)
//        // FIXME POSREF can this happen? Shouldn't the orderline just be a prop?
//        if (!selectedOrders) {
//            return;
//        }
//        const { confirmed, payload: inputNote } = await this.popup.add(TextAreaPopup, {
//            title: _t("Add Customer Note"),
//        });
//
//        if (confirmed) {
//            for (var orderline of selectedOrders){
//                orderline.set_discount(inputNote)
//            }
//        }
//    }
async onClick(){
        const Orderlines = this.pos.get_order().get_orderlines();
        const result = await this.orm.call('pos.order', 'get_discount', ['true']);
         for (let orderLine of Orderlines){
            orderLine.set_discount(result);
           }
    }

}

ProductScreen.addControlButton({
    component: MyOrderlineDiscount,
});