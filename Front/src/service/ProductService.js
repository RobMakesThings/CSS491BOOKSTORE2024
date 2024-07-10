export default class ProductService {
    getBooksByTitleOrAuthor(search) {
        return fetch(`api/search/${search}`)
            .then((res) => res.json())
            .then((d) => d.data);
    }
    getProductByid(search) {
        return fetch(`api/search/book/${search}`)
            .then((res) => res.json())
            .then((d) => d.data);
    }
    // demo/data/products.json
    getProducts() {
        return fetch('/api/searchAll/')
            .then((res) => res.json())
            .then((d) => d.data);

        // console.log(d.data)

    }

    deleteProduct(id) {
        return fetch(`api/delete/${id}`)
            .then((res) => res.json())
            .then((d) => d.data);
    }
    editProduct(id, Title, Author, Genre,Price) {
        return fetch(`api/update/${id}:${Title}:${Author}:${Genre}:${Price}`)
            .then((res) => res.json())
            .then((d) => d.data);
    }
    addProduct(Title, Author, Genre,Price) {
        return fetch(`api/add/${Title}:${Author}:${Genre}:${Price}`)
            .then((res) => res.json())
            .then((d) => d.data);
            
    }
}