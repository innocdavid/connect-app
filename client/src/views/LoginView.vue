<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-16">
                <h1 class="mb-6 text-2xl text-purple-500">Login</h1>
                <p class="mb-6 text-gray-500">Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Sed iusto, reprehenderit possimus commodi minima quam vel ab 
                    officiis aliquid id. Rem tenetur fuga delectus reprehenderit enim 
                    consectetur harum molestias quaerat!
                </p>
                <p class="text-gray-500">
                    Don't have an account? <RouterLink :to="{'name': 'signup'}" class="text-purple-500">Register</RouterLink>
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-10 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6">
                    <div>
                        <label>Email</label><br>
                        <input class="w-full mt-2 py-3 px-4 border border-gray-200" type="email" placeholder="Please enter your email">
                    </div>
                    <div>
                        <label>Password</label><br>
                        <input class="w-full mt-2 py-3 px-4 border border-gray-200" type="password" placeholder="Please enter your password">
                    </div>
                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
                            Login
                        </button>
                    </div>
                </form>

            </div>
        </div>
    </div>
</template>