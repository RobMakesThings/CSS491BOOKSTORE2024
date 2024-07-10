export default class OrderService {
    getOrders() {
        return fetch('api/orders/search/all')
            .then((res) => res.json())
            .then((d) => d.data);
    }
    viewOrder(id) {
        return fetch(`api/order/${id}`)
            .then((res) => res.json())
            .then((d) => d.data);
    }


}