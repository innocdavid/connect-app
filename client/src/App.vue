
<template>
    <NavBar />
    <main class="px-8 py-6 bg-gray-100">
      <RouterView />
    </main> 

</template>
<script>
    import NavBar from './components/NavBar.vue';
    export default {
        name: 'App',
        components: {
            NavBar,
        },
    }
</script>


