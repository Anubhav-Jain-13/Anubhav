/** @odoo-module **/
import { PartnerListScreen } from "@point_of_sale/app/screens/partner_list/partner_list";
import { patch } from "@web/core/utils/patch";
patch(PartnerListScreen.prototype, {
  async click(){
       var data = this.pos.partners
        for (let i of data){
            if (i.id == 67){
            console.log(i)
            this.state.selectedPartner = i;
            this.props.resolve({ confirmed: true, payload: this.state.selectedPartner });
            this.pos.closeTempScreen();
}
}
            }
});