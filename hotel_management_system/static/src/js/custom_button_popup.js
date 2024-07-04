/** @odoo-module **/

//add location task start here
import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { _t } from "@web/core/l10n/translation";
import { onMounted, useRef, useState } from "@odoo/owl";

export class CustomButtonPopup extends AbstractAwaitablePopup {
    static template = "point_of_sale.CustomButtonPopup";
    static defaultProps = {
        closeText: _t("Cancel"),
        confirmText: _t("Save"),
        title: _t("Select Location"),
        locations: [],
    };
    setup(){
        super.setup();
        this.state = useState({ inputValue: this.props.startingValue });
    }
    getPayload(){
        return this.state.inputValue;
    }
};

//add location task end here