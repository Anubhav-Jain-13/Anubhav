/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ExpenseListController } from "@hr_expense/views/list";

patch(ExpenseListController.prototype, {
    getReport(){
        alert("hiiiiiiiiiiiii");
    }
});

