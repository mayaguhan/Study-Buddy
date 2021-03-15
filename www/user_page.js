var get_all_URL = "http://localhost:5000/user";

var app = new Vue({
    el: "#app",
    computed: {
        hasUsers: function () {
            return this.users.length > 0;
        }
    },
    data: {
        isbn13: "",
        "users": [],
        message: "There is a problem retrieving users data, please try again later.",
        newISBN13: "",
        userAdded: false,
        addUserError: "",
        orderedUser: "",
        orderPlaced: false,
        orderSuccessful: false,
    },
    methods: {
        getAllUsers: function () {
            const response =
                fetch(get_all_URL)
                    .then(response => response.json())
                    .then(data => {
                        console.log(response);
                        if (data.code === 404) {
                            this.message = data.message;
                        } else {
                            this.users = data.data.users;
                        }
                    })
                    .catch(error => {
                        console.log(this.message + error);
                    });
        },

        findUser: function () {
            console.log(this.user_id);
            const response =
                fetch(`${get_all_URL}/${this.user_id}`)
                    .then(response => response.json())
                    .then(data => {
                        console.log(response);
                        if (data.code === 404) {
                            this.message = data.message;
                            this.users = [];
                        } else {
                            this.users = [data.data];
                        }
                    })
                    .catch(error => {
                        console.log(this.message + error);
                    });
        },

        addUser: function () {
            this.userAdded = false;
            this.addUserError = "";

            let jsonData = JSON.stringify({
                username: this.newUsername,
                contact: this.newContact,
                email: this.newEmail,
                photo: "none.png"
            });
            console.log(jsonData);

            fetch(`${get_all_URL}/${this.   name}`,
                {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json"
                    },
                    body: jsonData
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    result = data.data;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 201:
                            this.userAdded = true;
                            // refresh user list
                            this.getAllUsers();
                            // an alternate way is to add this one element into this.users
                            break;
                        case 400:
                        case 500:
                            this.addUserError = data.message;
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
        },
    },
    created: function () {
        // on Vue instance created, load the user list
        this.getAllUsers();
    }
});