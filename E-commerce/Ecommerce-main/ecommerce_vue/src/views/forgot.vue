<template>
    
    <form @submit.prevent="handleSubmit">

        <h3>forget password</h3>
        <div>
            <label>Email</label>
            <input type="email" class="form-control" v-model="email" placeholder="Email"/>
        </div>
        <button class="Button">submit</button>

    </form> 



</template>
<script>

import axios from 'axios'

export default {
    
    name: 'forgot',

    data() {
        return{
            email: ''
        }
    },

    methods: {
        async handleSubmit(){
            const response = await axios.post('forgot' , {
                email : this.email
            });
            console.log(response);
        }
    }
    
}
</script>