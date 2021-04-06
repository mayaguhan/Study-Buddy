window.onload=function(){
    const file = document.getElementById("file");
    const url = document.getElementById("url");

    var el = document.getElementById('file');
    if(el){
        file.addEventListener("change", ev => {
            const formData = new FormData();
            formData.append("image", ev.target.files[0]);
            fetch("https://api.imgur.com/3/image", {
                method: "post",
                headers: {
                    Authorization: "Client-ID 2f2e54e289b8051"
                },
                body: formData
            }).then(data => data.json()).then(data => {
                localStorage.newHomeworkImage = data.data.link;
                console.log(localStorage.getItem("newHomeworkImage"))
                if (localStorage.getItem("newHomeworkImage") != null) {
                    alert("Image has been successfully uploaded");
                }

            })
        })
    }
}



