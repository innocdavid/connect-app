<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-16">
                <h1 class="mb-6 text-2xl text-purple-500">Register</h1>
                <p class="mb-6 text-gray-500">Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Sed iusto, reprehenderit possimus commodi minima quam vel ab 
                    officiis aliquid id. Rem tenetur fuga delectus reprehenderit enim 
                    consectetur harum molestias quaerat!
                </p>
                <p class="text-gray-500">
                    Already have an account? <RouterLink :to="{'name': 'login'}" class="text-purple-500">Login</RouterLink>
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-10 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="subitForm">
                    <div>
                        <label>Name</label>
                        <input 
                            v-model="form.name"
                            class="w-full mt-2 py-3 px-4 border border-gray-200" 
                            type="text " 
                            placeholder="Please enter your name"
                        >
                    </div>
                    <div>
                        <label>Email</label><br>
                        <input 
                            v-model="form.email"
                            class="w-full mt-2 py-3 px-4 border border-gray-200" 
                            type="email" 
                            placeholder="Please enter your email"
                        >
                    </div>
                    <div>
                        <label>Password</label><br>
                        <input 
                            v-model="form.password1"
                            class="w-full mt-2 py-3 px-4 border border-gray-200" 
                            type="password" 
                            placeholder="Please enter your password"
                        >
                    </div>
                    <div>
                        <label>Confirm Password</label><br>
                        <input 
                            v-model="form.password2"
                            class="w-full mt-2 py-3 px-4 border border-gray-200" 
                            type="password" 
                            placeholder="Please confirm your password"
                        >
                    </div>
                    <template>
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" :key="error">{{ error }}</p>
                        </div>
                    </template>
                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
                            Register
                        </button>
                    </div>
                </form>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

import { useToastStore } from '@/stores/toast';

export default {
    setup() {
        const toastStore = useToastStore();

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: '',

            },
            errors: [],
        }
    },

    methods: {
        subitForm() {
            this.errors = [];

            if (this.form.email === '') {
                this.errors.push('Your email is missing');
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing');
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing');
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('Password does not match');
            }

            if (this.errors.length === 0) {
                axios.post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'Success', 'bg-emerald-500');

                            //reset fields
                            this.form.email = '';
                            this.form.name = '';
                            this.form.password1 = '';
                            this.form.password2 = '';
                        } else {
                            this.toastStore.showToast(5000, 'Error', 'bg-red-300');
                        }
                    })
                    .catch(error => {
                        console.log('error', error);
                    });
            }
        }
    }
}
</script>