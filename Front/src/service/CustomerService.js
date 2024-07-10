export default class CustomerService {
    getCustomersSmall() {
        return fetch('api/user/search/all/')
            .then((res) => res.json())
            .then((d) => d.data);
    }

    getCustomersMedium() {
        return fetch('api/user/search/all/')
            .then((res) => res.json())
            .then((d) => d.data);
    }

    getCustomersLarge() {
        return fetch('api/user/search/all/')
            .then((res) => res.json())
            .then((d) => d.data);
    }

    getCustomersXLarge() {
        return fetch('api/user/search/all/')
            .then((res) => res.json())
            .then((d) => d.data);
    }

    getCustomers(params) {
        const queryParams = Object.keys(params)
            .map((k) => encodeURIComponent(k) + '=' + encodeURIComponent(params[k]))
            .join('&');
        return fetch('https://www.primefaces.org//demo/data/customers?' + queryParams).then((res) => res.json());
    }
}
