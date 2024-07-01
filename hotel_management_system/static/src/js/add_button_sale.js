/* @odoo-module */

     //Add button in sale model start here
import { ListController } from "@web/views/list/list_controller";
import { listView } from "@web/views/list/list_view";
import { registry } from "@web/core/registry";


class SalesReport extends ListController {
    setup(){
        super.setup();
        console.log('js is loaded');
    }

    async demo(){
//     alert("DEMO");
     var records = this.model.root.selection;
     console.log(records)
        let sum=0
     for (var key in records){
                 console.log(records[key])
                 console.log(key + "...." + records[key].resIds)
                 sum += records[key].data.total_amount
                 console.log(records[key])
                 let datas = records[key].data
                 console.log(datas)
                 console.log(datas.name)
                // for (var key_1 in records[key]){
                //     console.log(key_1 + "...." + records[key].resId)
                // }
     }
     console.log(sum)
}
}
SalesReport.template = 'library_management.salenewbutton';

export const SalesReportListView = {
    ...listView,
    Controller: SalesReport,
}

registry.category("views").add('sale_list_button',SalesReportListView);

         //Add button in sale model end here

