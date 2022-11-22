function logar() {
    const email = document.getElementById("email").value;
    const senha = document.getElementById("password").value;

    const obj = {
        email: email,
        senha: senha
    }

    postData("url", obj)
}
