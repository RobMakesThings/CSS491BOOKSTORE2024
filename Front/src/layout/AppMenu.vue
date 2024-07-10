<script setup>
import { ref } from 'vue';

import AppMenuItem from './AppMenuItem.vue';

const model = ref([
    {
        label: 'Home',
        items: [{ label: 'Dashboard', icon: 'pi pi-fw pi-home', to: '/' },
        { label: 'Catalog', icon: 'pi pi-fw pi-image', to: '/pages/Catalog' },
        { label: 'Orders', icon: 'pi pi-fw pi-shopping-bag', to: '/pages/OrderDash' },
        { label: 'Manage Books', icon: 'pi pi-fw pi-pencil', to: '/pages/crud' },
        // { label: 'Supplier Dashboard', icon: 'pi pi-fw pi-tablet', to: '/pages/crud' },
        { label: 'ProductView', icon: 'pi pi-fw pi-tablet', to: '/pages/ProductView' },
        {label: 'Login',icon: 'pi pi-fw pi-sign-in',to: '/auth/login'}
    ]
    }

]);
</script>

<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
       
    </ul>
</template>

<style lang="scss" scoped></style>
