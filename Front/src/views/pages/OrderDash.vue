<script setup>
import { onMounted, reactive, ref, watch } from 'vue';
import ProductService from '@/service/ProductService';
import OrderService from '@/service/OrderService'
import { useLayout } from '@/layout/composables/layout';
import router from '../../router/index';


const { isDarkTheme } = useLayout();

const products = ref(null);

const orders = ref(null);

const items = ref([
    { label: 'Add New', icon: 'pi pi-fw pi-plus' },
    { label: 'Remove', icon: 'pi pi-fw pi-minus' }
]);
let orderTotal;
const productService = new ProductService();
const orderService = new OrderService();
onMounted(() => {
    productService.getProducts().then((data) => (products.value = data));

    orderService.getOrders().then((data) => (orders.value = data));
    


});

// const ;
console.log(orderTotal)

</script>

<template>
    
    
    <div class="col-12 xl:col-6">
        <div class="card" style="width: 100%">
            <h5>Orders</h5>
            <DataTable :value="orders" :rows="5" :paginator="true" style="width: 100%" >

                <Column field="Customer" style="width: 100%">
                    
                    <template #header> Name </template>
                    
                                        
                    <template #body="slotProps">
                        {{ slotProps.data.Name , orderTotal}}
                    </template>
                </Column>
                <!-- <Column field="Title" header="Title" :sortable="true" style="width: 35%"></Column>
                <template #body="slotProps">
                    {{ slotProps.data.Title }}
                </template> -->
                <Column field="Date" header="Date" :sortable="true" style="width: 50%">
                    <template #body="slotProps">

                        {{ slotProps.data.date }}
                    </template>
                </Column>
                <Column field="Address" header="Address" :sortable="true" style="width: 50%">
                    <template #body="slotProps">

                        {{ slotProps.data.Address }}
                    </template>
                </Column>
                <Column field="Status" header="Status" :sortable="true" style="width: 50%">
                    <template #body="slotProps">

                        {{ slotProps.data.orderStatus }}
                    </template>
                </Column>
                <Column style="width: 15%">
                    <template #header> View </template>
                    <template #body="slotProps">
                        <Button @click='router.push({path:"/pages/order",query:{id:slotProps.data.id}})' icon="pi pi-search" type="button" class="p-button-text"></Button>
                    </template>
                </Column>
                <Column headerStyle="min-width:10rem;">
                        <template #body="slotProps">
                            
                        </template>
                    </Column>
                    
            </DataTable>
        </div>
        
    
</div></template>
