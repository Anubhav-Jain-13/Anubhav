/** @odoo-module **/


//Make a JavaScript Class "A", along with this, inherit this into a new class called Class "B".

import { A } from "./A_class"
class B extends A{
     hello_B(){
      console.log("helloB")
    }
}
const obj = new B()
obj.hello_B()