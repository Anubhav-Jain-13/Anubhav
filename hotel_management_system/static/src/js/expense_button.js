/** @odoo-module **/

          //Add button in hr expense model start here

import { patch } from "@web/core/utils/patch";
import { ExpenseListController } from "@hr_expense/views/list";

patch(ExpenseListController.prototype, {
    getReport(){
        alert("hiiiiiiiiiiiii");
    }
});
       //Add button in hr expense model end here
