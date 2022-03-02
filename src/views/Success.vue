<template>
   <div class="page-Success">
       <div class="columns is-multiline">
           <div class="column is-12">
               <h1 class="title">Thank you</h1>

               <p> Your order will be processes within 48 hours </p>
           </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Success | shirts '
    },

    
}
</script>