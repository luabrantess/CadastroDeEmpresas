window.onload = () => {
    const form = document.getElementsByTagName("form")[0]
    const inputs = form.getElementsByTagName("input")


    form.addEventListener(
        "submit",
        () => {
            const data = {}
            for (let i = 0; i < inputs.length; i++) {
                const input = inputs[i]
                if (input.id)
                    data[input.id] = input.value
            }
            /*
                FETCH
             */
            window.open("./empresas.html", "_self")
        }
    )
}