/ @odoo-module /

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.customWidget = publicWidget.Widget.extend({
    selector: '.anubhav',
    start: function () {
        console.log('Custom Web page render using controller');
        this._super.apply(this, arguments);
        this._bindEvents();
    },

    _bindEvents: function () {
        this.$('.o_subtitle').on('click', this.chk_email.bind(this));
        this.$('.o_button').on('click', this.change_form_bg_color.bind(this));
    },

      chk_email: function(){
       let email = document.getElementById('email').value
       console.log(email)
       let flag = 0;
       let ans = true;
       for(let i=0; i<email.length; i++){
          if (email[i] == '@'){
            flag = flag + 1;
            if (i+1 >= email.length){
              ans = false;
            }
          }
       }

       if (flag != 1 || ans==false){
         alert("Please enter valid email")
         return false;
       }
       else if(flag == 1 && ans==false){
         alert("Please enter valid email");
         return false;
       }
      return true

    },
     change_form_bg_color: function () {
     console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
      const randomColor = this.getRandomColor();
        this.$('.o_button').css('background-color', randomColor);
    },

    getRandomColor: function () {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
});
