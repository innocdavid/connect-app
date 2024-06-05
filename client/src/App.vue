
<template>
    <NavBar />
    <main class="px-8 py-6 bg-gray-100">
      <RouterView />
    </main> 
    <Toast />
</template>
<script>
    import NavBar from '@/components/NavBar.vue';
    import Toast from '@/components/Toast.vue'

    export default {
        name: 'App',
        components: {
            NavBar,
            Toast,
        },
    }
</script>


