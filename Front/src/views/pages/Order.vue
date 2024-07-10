<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount, computed } from 'vue';
import {useRouter} from 'vue-router'
import ProductService from '@/service/ProductService';
import OrderService from '@/service/OrderService';
import { useToast } from 'primevue/usetoast';

const toast = useToast();
const router = useRouter()
const targetOrder = router.currentRoute.value.query.id
console.log(router.currentRoute.value.query.id)




const products = ref(null);
const order = ref(null)
const productDialog = ref(false);
const deleteProductDialog = ref(false);
const deleteProductsDialog = ref(false);
const product = ref({});
const selectedProducts = ref(null);
const dt = ref(null);
const filters = ref({});
const submitted = ref(false);
const statuses = ref([
    { label: 'INSTOCK', value: 'instock' },
    { label: 'LOWSTOCK', value: 'lowstock' },
    { label: 'OUTOFSTOCK', value: 'outofstock' }
]);

const productService = new ProductService();
const orderService = new OrderService();
onBeforeMount(() => {
    initFilters();
});
let orderTotal = ref(null);
let customerName;
let Address;

onMounted(() => {
    
    productService.getProducts().then((data) => (products.value = data));

    orderService.viewOrder(targetOrder).then((data)=>(order.value = data , customerName= data[0]['Name'], Address= data[0]['Address']))
});
const formatCurrency = (value) => {
    return value.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
};

// orderTotal= order.reduce((sum,item)=>sum +item.Price*item.quantity,0)
for (let index = 0; index < 3; index++) {
    console.log(order)
    
}

// const totalPrice = computed(() =>
//   products.value.reduce((sum, item) => sum + item.price, 0)
// )

// console.log(totalPrice)
const openNew = () => {
    product.value = {};
    submitted.value = false;
    productDialog.value = true;
};

const hideDialog = () => {
    productDialog.value = false;
    submitted.value = false;
};


const findIndexById = (id) => {
    let index = -1;
    for (let i = 0; i < products.value.length; i++) {
        if (products.value[i].id === id) {
            index = i;
            break;
        }
    }
    return index;
};



const exportCSV = () => {
    dt.value.exportCSV();
};

const confirmDeleteSelected = () => {
    deleteProductsDialog.value = true;
};
const deleteSelectedProducts = () => {
    products.value = products.value.filter((val) => !selectedProducts.value.includes(val));
    deleteProductsDialog.value = false;
    selectedProducts.value = null;
    toast.add({ severity: 'success', summary: 'Successful', detail: 'Products Deleted', life: 3000 });
};

const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};

</script>


<template>
    
    <div class="grid">
        <div class="col-12">
            <div class="card">
                <Toast />
                <Toolbar class="mb-4">
                
                </Toolbar>

                <DataTable
                    ref="dt"
                    :value="order"
                    v-model:selection="selectedProducts"
                    dataKey="id"
                    :paginator="true"
                    :rows="10"
                    :filters="filters"
                    paginatorTemplate=" PrevPageLink NextPageLink LastPageLink CurrentPageReport "
                    :rowsPerPageOptions="[5, 10, 25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products"
                    responsiveLayout="scroll"
                >
                    <template #header>
                        <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                            <h5 class="card">Items in order for {{ customerName }}<br><h4 class="card">Deliver to {{Address}}</h4>
                            Order total 
                            </h5>
                        
                            
                            <span class="block mt-2 md:mt-0 p-input-icon-left">
                                <i class="pi pi-search" />
                                <InputText v-model="filters['global'].value" placeholder="Filters" />
                            </span>
                        </div>
                    </template>

                    <Column field="Title" header="Title" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Title</span>
                            {{ slotProps.data.Title }}
                        </template>
                    </Column>
                    <!-- <Column field="Author" header="Author" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">author</span>
                            {{ slotProps.data.Name }}
                        </template>
                    </Column> -->
                    <Column field="Genre" header="Quantity" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Genre</span>
                            <!-- <img :src="'demo/images/product/' + slotProps.data.image" :alt="slotProps.data.image" class="shadow-2" width="100" /> -->
                            {{ slotProps.data.quantity }}
                        </template>
                    </Column>
                    <Column field="Price" header="Price" :sortable="true" headerStyle="width:14%; min-width:6rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Price</span>
                            {{ slotProps.data.Price }}
                            <!-- <img :src="'demo/images/product/' + slotProps.data.image" :alt="slotProps.data.image" class="shadow-2" width="100" /> -->
                            
                        </template>
                    </Column>
                    
                    
                </DataTable>

                <Dialog v-model:visible="productDialog" :style="{ width: '450px' }" header="Product Details" :modal="true" class="p-fluid">
                    
                    <div class="field">
                        <label for="Title">Title</label>
                        <InputText id="Title" v-model.trim="product.Title" required="true" autofocus :class="{ 'p-invalid': submitted && !product.Title }" />
                        <small class="p-invalid" v-if="submitted && !product.Title">Name is required.</small>
                    </div>
                    <div class="field">
                        <label for="Author">Author</label>
                        <InputText id="Author" v-model.trim="product.Author" required="true" autofocus :class="{ 'p-invalid': submitted && !product.Author }" />
                        <small class="p-invalid" v-if="submitted && !product.Author">Author Name is required.</small>
                    </div>
                    <div class="field">
                        <label for="Genre">Genre</label>
                        <InputText id="Genre" v-model.trim="product.Genre" required="true" autofocus :class="{ 'p-invalid': submitted && !product.Genre }" />
                        <small class="p-invalid" v-if="submitted && !product.Genre">Genre is required, Unknown is okay</small>
                    </div>
                   
                   

                    <div class="formgrid grid">
                        <div class="field col">
                            <label for="Price">Price</label>
                            <InputNumber id="price" v-model="product.Price" mode="currency" currency="USD" locale="en-US" :class="{ 'p-invalid': submitted && !product.Price }" :required="true" />
                            <small class="p-invalid" v-if="submitted && !product.Price">Price is required.</small>
                        </div>
                       
                    </div>
                    <template #footer>
                        <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialog" />
                        <Button label="Save" icon="pi pi-check" class="p-button-text" @click="saveProduct" />
                    </template>
                </Dialog>

                <Dialog v-model:visible="deleteProductDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
                    <div class="flex align-items-center justify-content-center">
                        <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
                        <span v-if="product"
                            >Are you sure you want to delete <b>{{ product.name }}</b
                            >?</span
                        >
                    </div>
                    <template #footer>
                        <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteProductDialog = false" />
                        <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteProduct" />
                    </template>
                </Dialog>

                <Dialog v-model:visible="deleteProductsDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
                    <div class="flex align-items-center justify-content-center">
                        <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
                        <span v-if="product">Are you sure you want to delete the selected products?</span>
                    </div>
                    <template #footer>
                        <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteProductsDialog = false" />
                        <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteSelectedProducts" />
                    </template>
                </Dialog>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss"></style>