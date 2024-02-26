<template>
    <nav class="py-5 px-8 border-b border-gray-200">
      <div class="max-w-7xl mx-auto">
        <div class="flex items-center justify-between">
          <div class="menu-left">
            <a href="#" class="text-xl">ConnectApp</a>
          </div>
          <div class="menu-center flex space-x-12 bg-blue">
            <HomeIcon />
            <MessageIcon />
            <NotificationIcon />
            <SearchIcon />
          </div>
          <div class="menu-right">
            <a href="#">
              <img src="https://i.pravatar.cc/40?img=70" class="rounded-full">
            </a>
          </div>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
    import HomeIcon from './_generic/HomeIcon.vue';
    import MessageIcon from './_generic/MessageIcon.vue';
    import NotificationIcon from './_generic/NotificationIcon.vue';
    import SearchIcon from './_generic/SearchIcon.vue';
    // import { RouterView } from 'vue-router'
    export default {
      name: 'NavBar',
      components: {
        HomeIcon,
        MessageIcon,
        NotificationIcon,
        SearchIcon,
      }
    }
  </script>