

<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount } from 'vue';
import {useRouter} from 'vue-router'
import ProductService from '@/service/ProductService';

const dataviewValue = ref(null);
const layout = ref('grid');
const router = useRouter()
const targetBook = router.currentRoute.value.query.id
const productService = new ProductService();
onBeforeMount(() => {
    
});
onMounted(() => {
    productService.getProductByid(targetBook).then((data) => (dataviewValue.value = data));
});


</script>


<template>
    
    <DataView :value="dataviewValue">
        <template #header>
            
    
        </template>
        <template #list="slotProps">
            <div class="col-60">
                <div class="flex flex-column md:flex-row align-items-center p-3 w-full">
                    <img src='../../../public/demo/images/product/book.jpeg' :alt="slotProps.data.Title"
                        class="my-4 md:my-0 w-9 md:w-10rem shadow-2 mr-5" href="/"/>
                    
                    <div class="flex-10 text-center md:text-left mr-50 ">
                        <div class="font-bold text-2xl">{{ slotProps.data.Title }}</div>
                        <span class="font-semibold">{{ slotProps.data.Genre }}</span>

                        <div class="mb-3">{{ slotProps.data.Description }}</div>
                        <span class="text-2xl font-semibold">${{ slotProps.data.Price }}</span>
                        <div class="flex align-items-center">
                            

                        </div>
                        <Button @click="" icon="pi pi-shopping-cart" label="Add to Cart" :disabled="slotProps.data.inventoryStatus === 'OUTOFSTOCK'" class="mb-2"></Button>

                    </div>
                    <div class="flex flex-row md:flex-column justify-content-between w-full md:w-auto align-items-center md:align-items-end mt-5 md:mt-0">
                                    <!-- <span :class="'product-badge status-' + slotProps.data.inventoryStatus.toLowerCase()">{{ slotProps.data.inventoryStatus }}</span> -->
                                </div>
                </div>
            </div>
        </template>
    </DataView>
</template>
