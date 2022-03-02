<template>
   <div class="page-checkout">
       <div class="columns is-multiline">
           <div class="column is-12">
               <h1 class="title">Checkout</h1>
           </div>
           <div class="column is-12 box"> 
               <h2 class="subtitle">Payment</h2>
               <div class="columns is-multiline">
                   <div class="column is-6">
                       <div class="field">
                           <label> Amount*</label>
                           <div class="control">
                               <input type="amount" class="input" v-model="amount">
                           </div>
                       </div>
                       <div class="field">
                           <label> E-mail*</label>
                           <div class="control">
                               <input type="email" class="input" v-model="email">
                           </div>
                       </div>
                    </div>
                     <hr>
                   
                        <button class="button is-dark" @click="submitForm()" type="submit"> make payment </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import VuePaystack from "vue-paystack2"

export default {
  name: 'Checkout',
   
  data () {
    return {
        paystackKey: {},
        email: '',
        amount: 0,
        reference: ''
        
    }
  },
  methods: {
      submitForm() {
          const data = {
              currency: "NGN",
              plan :"",
              ref:"{{ payment.ref}}",
              key: "{{ paystack_public_key}}",
              email: '{{ payment.email}}',
              amount: '{{ payment.amount_value }}',
              
             } 
            

      }
    
       
    }
}
</script>