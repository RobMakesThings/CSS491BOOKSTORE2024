
<!-- this page could be used as a search results page.  -->
<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount } from 'vue';
import {useRouter} from 'vue-router'
import { useProductStore } from '../../store/products'
const productStore = useProductStore()

import ProductService from '@/service/ProductService';
const router = useRouter()

const display = ref(false);
const displayConfirmation = ref(false);
const visibleLeft = ref(false);
const visibleRight = ref(false);
const visibleTop = ref(false);
const visibleBottom = ref(false);
const visibleFull = ref(false);
const dataviewValue = ref(null);
const layout = ref('grid');
const sortKey = ref(null);
const sortOrder = ref(null);
const sortField = ref(null);
const filters = ref({});
const sortOptions = ref([
    { label: 'Price High to Low', value: '!Price' },
    { label: 'Price Low to High', value: 'Price' }
]);

const productService = new ProductService();
onBeforeMount(() => {
    initFilters();
});
onMounted(() => {
    productService.getProducts().then((data) => (dataviewValue.value = data));
});
const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};
const onSortChange = (event) => {
    const value = event.value.value;
    const sortValue = event.value;

    if (value.indexOf('!') === 0) {
        sortOrder.value = -1;
        sortField.value = value.substring(1, value.length);
        sortKey.value = sortValue;
    } else {
        sortOrder.value = 1;
        sortField.value = value;
        sortKey.value = sortValue;
    }
};
console.log("store",productStore)
</script>


<template>
    
    
    <DataView :value="dataviewValue" :filters="filters" :layout="layout" :paginator="true" :rows="9" :sortOrder="sortOrder"
        :sortField="sortField">
        <template #header>
            <span class="block mt-2 md:mt-0 p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global'].value" placeholder="a" />
            </span>
            <div class="grid grid-nogutter">
                <div class="col-6 text-left">
                    <Dropdown v-model="sortKey" :options="sortOptions" optionLabel="label" placeholder="Sort By Price"
                        @change="onSortChange($event)" />
                </div>
                <div class="col-6 text-right">
                    <DataViewLayoutOptions v-model="layout" />
                </div>
            </div>
        </template>
        <template #list="slotProps">
            <div @click="alert(1)" class="col-12">
                <div  class="flex flex-column md:flex-row align-items-center p-3 w-full">
                    <img src='../../../public/demo/images/product/book.jpeg' :alt="slotProps.data.Title"
                        class="my-4 md:my-0 w-9 md:w-10rem shadow-2 mr-5" />
                    <div class="flex-1 text-center md:text-left">
                        <div class="font-bold text-2xl">{{ slotProps.data.Title }}</div>
                        <div class="mb-3">{{ slotProps.data.Description }}</div>
                        <span class="text-2xl font-semibold">${{ slotProps.data.Price }}</span>
                        <div class="flex align-items-center">
                            <i class="pi pi-tag mr-2"></i>
                            <span class="font-semibold margin:5px">{{ slotProps.data.Genre }}</span>
                            <Button @click='router.push({path:"/pages/ProductView",query:{id:slotProps.data.id}})' icon="pi pi-search" type="button" class="p-button-text"></Button>
                        
                        </div>
                    </div>
                    <div class="flex flex-row md:flex-column justify-content-between w-full md:w-auto align-items-center md:align-items-end mt-5 md:mt-0">
                                    <Button icon="pi pi-shopping-cart" label="Add to Cart" :disabled="slotProps.data.inventoryStatus === 'OUTOFSTOCK'" class="mb-2"></Button>
                                </div>
                </div>
            </div>
        </template>

        <template #grid="slotProps">
            <div class="col-12 md:col-4">
                <div class="card m-3 border-1 surface-border">
                    <div class="flex align-items-center justify-content-between">
                        <div class="flex align-items-center">
                            <i class="pi pi-tag mr-2"></i>
                            <span class="font-semibold">{{ slotProps.data.Genre }}</span>
                        </div>
                    </div>
                    <div class="text-center">
                        <img src='../../../public/demo/images/product/book.jpeg' :alt="slotProps.data.Title"
                            class="w-9 shadow-2 my-3 mx-0" />
                        <div class="text-2xl font-bold">{{ slotProps.data.Title }}</div>
                        <div class="mb-3">{{ "by: " + slotProps.data.Author }}</div>
                        <span class="text-2xl font-semibold">${{ slotProps.data.Price }}</span>
                        <div class="mb-2">{{ slotProps.data.Description }}</div>
                        <Button @click='router.push({path:"/pages/ProductView",query:{id:slotProps.data.id}})' icon="pi pi-search" type="button" class="p-button-text"></Button>
                        <Button icon="pi pi-shopping-cart" :disabled="slotProps.data.inventoryStatus === 'OUTOFSTOCK'"></Button>

                    </div>
                 
                    
                </div>
            </div>
        </template>
    </DataView>
</template>
