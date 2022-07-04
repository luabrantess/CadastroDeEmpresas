let municipioInput, ufInput
window.onload = () => {
    municipioInput = document.querySelector("#municipio")
    ufInput = document.querySelector("#uf")
    document.querySelector("#form_cidade")
        .addEventListener("submit", submit)
}

async function submit(event) {
    try {
        const response = await fetch(
            "http://localhost:8000/api/cidade",
            {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    uf: ufInput.value,
                    municipio: municipioInput.value
                })
            }
        )
        console.log(response)
    } catch (err) {
        console.error(err)
    }
}
