/** @odoo-module **/


//add location task start here

import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { CustomButtonPopup } from "@hotel_management_system/js/custom_button_popup";
import { onMounted, useRef, useState } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import {Order} from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

class LocationButton extends Component {
static template = 'point_of_sale.locationBtn';
    setup() {
        this.orm = useService("orm");
        this.pos = usePos();
         this.popup = useService("popup");
                 this.state = useState({ locationText: _t("Location") });

    }
    async OnClick() {
       const order = this.pos.get_order();
     const res = await this.orm.call('pos.config', 'get_locations',['true']);
     console.log(res)

     const { confirmed, payload: selectedLocation } = await this.popup.add(CustomButtonPopup, {
            // startingValue: selectedOrderline.get_customer_note(),
            title: _t("Add Location"),
            locations: res,
        });
         this.state.locationText = selectedLocation || _t("Location");
         let selection = this.state.locationText

          order.set_location(selection);

    }
}
ProductScreen.addControlButton({
    component: LocationButton,
    condition: () => true
})


patch(Order.prototype,{

     export_as_JSON(){
       const res = super.export_as_JSON(...arguments);
       res.location_pos = this.get_location();
       return res;
     },

     get_location(){
       return this.inputNote
     },

     set_location(inputNote){
       this.inputNote = inputNote
     },


     export_for_printing(){
       const rec = super.export_for_printing(...arguments);
       rec.location_recept = this.inputNote
       return rec;
     }

});

//add location task end here