<script setup>
import { onMounted, reactive, ref, watch } from 'vue';
import ProductService from '@/service/ProductService';
import OrderService from '@/service/OrderService'
import { useLayout } from '@/layout/composables/layout';
import router from '../router';


const { isDarkTheme } = useLayout();

const products = ref(null);

const orders = ref(null);
let orderLength =0
const items = ref([
    { label: 'Add New', icon: 'pi pi-fw pi-plus' },
    { label: 'Remove', icon: 'pi pi-fw pi-minus' }
]);
const lineOptions = ref(null);
const productService = new ProductService();
const orderService = new OrderService();
onMounted(() => {
    productService.getProducts().then((data) => (products.value = data));

    orderService.getOrders().then((data) => (orders.value = data,orderLength = data.length, orders));
    


});
console.log(orders)

const formatCurrency = (value) => {
    return value.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
};
const applyLightTheme = () => {
    lineOptions.value = {
        plugins: {
            legend: {
                labels: {
                    color: '#495057'
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: '#495057'
                },
                grid: {
                    color: '#ebedef'
                }
            },
            y: {
                ticks: {
                    color: '#495057'
                },
                grid: {
                    color: '#ebedef'
                }
            }
        }
    };
};

const applyDarkTheme = () => {
    lineOptions.value = {
        plugins: {
            legend: {
                labels: {
                    color: '#ebedef'
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: '#ebedef'
                },
                grid: {
                    color: 'rgba(160, 167, 181, .3)'
                }
            },
            y: {
                ticks: {
                    color: '#ebedef'
                },
                grid: {
                    color: 'rgba(160, 167, 181, .3)'
                }
            }
        }
    };
};

watch(
    isDarkTheme,
    (val) => {
        if (val) {
            applyDarkTheme();
        } else {
            applyLightTheme();
        }
    },
    { immediate: true }
);
</script>

<template>
    <div class="col-12 lg:col-6 xl:col-3">
        <div class="card mb-0">
            <div class="flex justify-content-between mb-3">
                <div >
                    <span class="block text-500 font-medium mb-3">Orders</span>
                    <!-- {{ console.log(slotProps.data) }} -->
                    <div class="text-900 font-medium text-xl" >{{ orderLength + "total orders" }}</div>
                </div>
                <div class="flex align-items-center justify-content-center bg-cyan-100 border-round"
                    style="width: 2.5rem; height: 2.5rem">
                    <i class="pi pi-inbox text-cyan-500 text-xl"></i>
                </div>
            </div>
            <span class="text-green-500 font-medium">520 </span>
            <span class="text-500">newly registered</span>
        </div>
    </div>
    
    <div class="col-12 xl:col-6">
        <div class="card">
            <h5>Orders</h5>
            <DataTable :value="orders" :rows="5" :paginator="true" responsiveLayout="scroll">

                <Column field="Customer" style="width: 15%">
                    console.log(slotProps.data)
                    <template #header> Name </template>
                    <template #body="slotProps">
                        {{ slotProps.data.Name}}
                    </template>
                </Column>
                <!-- <Column field="Title" header="Title" :sortable="true" style="width: 35%"></Column>
                <template #body="slotProps">
                    {{ slotProps.data.Title }}
                </template> -->
                <Column field="Date" header="Date" :sortable="true" style="width: 35%">
                    <template #body="slotProps">

                        {{ slotProps.data.date }}
                    </template>
                </Column>
                <Column field="Address" header="Address" :sortable="true" style="width: 35%">
                    <template #body="slotProps">

                        {{ slotProps.data.Address }}
                    </template>
                </Column>
                <Column style="width: 15%">
                    <template #header> View </template>
                    <template #body="slotProps">
                        <Button @click='router.push({path:"/pages/order",query:{id:slotProps.data.id}})' icon="pi pi-search" type="button" class="p-button-text"></Button>
                    </template>
                </Column>
            </DataTable>
        </div>
        <div class="col-12 xl:col-12">
            <div class="card">
                <h5>Books</h5>
                <DataTable :value="products" :rows="5" :paginator="true" responsiveLayout="scroll">
                    <Column field="author" style="width: 15%">

                        <template #header> Author </template>
                        <template #body="slotProps">
                            {{ slotProps.data.Author
                            }}
                        </template>
                    </Column>
                    <Column field="Title" header="Title" :sortable="true" style="width: 35%"></Column>
                    <template #body="slotProps">
                        {{ slotProps.data.Title }}
                    </template>
                    <Column field="Price" header="Price" :sortable="true" style="width: 35%">
                        <template #body="slotProps">
                            {{ slotProps.data.Price }}
                        </template>
                    </Column>
                    
                    <Column style="width: 25%">
                        <template #header> View </template>
                        <template #body="slotProps">
                            <Button @click='router.push({path:"/pages/ProductView",query:{id:slotProps.data.id}})' icon="pi pi-search" type="button" class="p-button-text"></Button>
                        </template>
                    </Column>
                </DataTable>
            </div>
            
        </div>
    
</div></template>
