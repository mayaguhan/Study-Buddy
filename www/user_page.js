var user_url = "http://localhost:5000/user";

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
        userAdded: false, 
        user_id: "",
        newUsername: "",
        newTelegramId: "",
        newContact: "",
        newEmail: "",
        addUserError: "",
        orderedUser: "",
        orderPlaced: false,
        orderSuccessful: false,
    },
    methods: {
        getAllUsers: function () {
            const response =
                fetch(user_url)
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
            const response =
                fetch(`${user_url}/${this.user_id}`)
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
                telegram_id: this.newTelegramId,
                contact: this.newContact,
                email: this.newEmail,
                photo: "none.png"
            });
            console.log(jsonData);

            fetch(`${user_url}/${this.newUsername}`,
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
                    switch (data.code) {
                        case 201:
                            this.userAdded = true;
                            this.getAllUsers();
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
        this.getAllUsers();
    }
});