//local storage
let currentUser_id = 1;

var homework_url = "http://localhost:5100/homework";

var app = new Vue({
    el: "#app",
    computed: {
        hasHomeworks: function () {
            return this.homeworks.length > 0;
        }
    },
    data: {
        isbn13: "",
        "homeworks": [],
        message: "There is a problem retrieving homeworks data, please try again later.",
        newISBN13: "",
        homeworkAdded: false,
        addHomeworkError: "",
        orderedHomework: "",
        orderPlaced: false,
        orderSuccessful: false,
        homework_id: "",
        newSubject: "",
        newTitle: "",
        newDescription: "",
        newPrice: "",
        newDeadline: ""
    },
    methods: {
        getAllHomeworks: function () {
            const response =
                fetch(homework_url)
                    .then(response => response.json())
                    .then(data => {
                        console.log(response);
                        if (data.code === 404) {
                            this.message = data.message;
                        } else {
                            this.homeworks = data.data.homeworks;
                        }
                    })
                    .catch(error => {
                        console.log(this.message + error);
                    });

        },

        findHomework: function () {
            console.log(this.homework_id);
            const response =
                fetch(`${homework_url}/${this.homework_id}`)
                    .then(response => response.json())
                    .then(data => {
                        console.log(response);
                        if (data.code === 404) {
                            this.message = data.message;
                            this.homeworks = [];
                        } else {
                            this.homeworks = [data.data];
                        }
                    })
                    .catch(error => {
                        console.log(this.message + error);
                    });
        },

        addHomework: function () {
            this.homeworkAdded = false;
            this.addHomeworkError = "";
            let jsonData = JSON.stringify({
                student_id: currentUser_id, 
                subject: this.newSubject,
                title: this.newTitle, 
                description: this.newDescription, 
                price: this.newPrice,
                deadline: this.newDeadline,
                status: "unsolved"
            });
            console.log(this.newDeadline);
            console.log(jsonData);

            fetch(`${homework_url}/addHomework`, {
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
                            this.homeworkAdded = true;
                            this.getAllHomeworks();
                            break;
                        case 400:
                        case 500:
                            this.addHomeworkError = data.message;
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
        },
    },
    created: function () {
        this.getAllHomeworks();
    }
});