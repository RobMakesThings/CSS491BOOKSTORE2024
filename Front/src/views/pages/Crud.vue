<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount } from 'vue';
import ProductService from '@/service/ProductService';
import { useToast } from 'primevue/usetoast';

const toast = useToast();

const products = ref(null);
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

onBeforeMount(() => {
    initFilters();
});
onMounted(() => {
    productService.getProducts().then((data) => (products.value = data));
});
const formatCurrency = (value) => {
    return value.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
};

const openNew = () => {
    product.value = {};
    submitted.value = false;
    productDialog.value = true;
};

const hideDialog = () => {
    productDialog.value = false;
    submitted.value = false;
};

const saveProduct = () => {
    submitted.value = true;
    // products.value = products.value.filter((val) => val.id !== product.value.id);
    // change save to match what we need as far as inputs outputs. 

    
        if (product.value.id) {
            
            products.value[findIndexById(product.value.id)] = product.value;
            console.log(product.value)
            productService.editProduct(product.value.id,product.value.Title,product.value.Author,product.value.Genre,product.value.Price)
            toast.add({ severity: 'success', summary: 'Successful', detail: 'Product Updated', life: 3000 });
        } else {
            
            
            productService.addProduct(product.value.Title,product.value.Author,product.value.Genre,product.value.Price)
            toast.add({ severity: 'success', summary: 'Successful', detail: 'Product Created', life: 3000 });
        }
        productDialog.value = false;
        // product.value = {};
    }
    


const editExistProduct = (editProduct) => {
    product.value = { ...editProduct };
    // products.value = products.value.filter((val) => val.id !== product.value.id);
    console.log(" trying to edit");

    productDialog.value = true;
    
};

const confirmDeleteProduct = (editProduct) => {
    product.value = editProduct;
    deleteProductDialog.value = true;
};

const deleteProduct = () => {
    products.value = products.value.filter((val) => val.id !== product.value.id);
    deleteProductDialog.value = false;
    productService.deleteProduct(product.value.id)
    product.value = {};
    
    toast.add({ severity: 'success', summary: 'Successful', detail: 'Product Deleted', life: 3000 });
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
                    <template v-slot:start>
                        <div class="my-2">
                            <Button label="New" icon="pi pi-plus" class="p-button-success mr-2" @click="openNew" />
                            <Button label="Delete" icon="pi pi-trash" class="p-button-danger" @click="confirmDeleteSelected" :disabled="!selectedProducts || !selectedProducts.length" />
                        </div>
                    </template>

                    
                </Toolbar>

                <DataTable
                    ref="dt"
                    :value="products"
                    v-model:selection="selectedProducts"
                    dataKey="id"
                    :paginator="true"
                    :rows="10"
                    :filters="filters"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                    :rowsPerPageOptions="[5, 10, 25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products"
                    responsiveLayout="scroll"
                >
                    <template #header>
                        <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                            <h5 class="m-0">Manage Books</h5>
                            <span class="block mt-2 md:mt-0 p-input-icon-left">
                                <i class="pi pi-search" />
                                <InputText v-model="filters['global'].value" placeholder="Author or Title" />
                            </span>
                        </div>
                    </template>

                    <Column selectionMode="multiple" headerStyle="width: 3rem"></Column>
                  
                    <Column field="Title" header="Title" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Title</span>
                            {{ slotProps.data.Title }}
                        </template>
                    </Column>
                    <Column field="Author" header="Author" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">author</span>
                            <!-- <img :src="'demo/images/product/' + slotProps.data.image" :alt="slotProps.data.image" class="shadow-2" width="100" /> -->
                            {{ slotProps.data.Author }}
                        </template>
                    </Column>
                    <Column field="Genre" header="Genre" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Genre</span>
                            <!-- <img :src="'demo/images/product/' + slotProps.data.image" :alt="slotProps.data.image" class="shadow-2" width="100" /> -->
                            {{ slotProps.data.Genre }}
                        </template>
                    </Column>
                    <Column field="Price" header="Price" :sortable="true" headerStyle="width:14%; min-width:6rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Price</span>
                            {{ slotProps.data.Price }}
                            <!-- <img :src="'demo/images/product/' + slotProps.data.image" :alt="slotProps.data.image" class="shadow-2" width="100" /> -->
                            
                        </template>
                    </Column>
                    <Column field="id" header="id" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">id</span>
                            {{ slotProps.data.id }}
                        </template>
                    </Column>
                    <Column headerStyle="min-width:10rem;">
                        <template #body="slotProps">
                            <Button icon="pi pi-pencil" class="p-button-rounded p-button-success mr-2" @click="editExistProduct(slotProps.data)" />
                            <Button icon="pi pi-trash" class="p-button-rounded p-button-warning mt-2" @click="confirmDeleteProduct(slotProps.data)" />
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