window.onload = () => {
    const container = document.getElementById("container-lista")

    updateList(container).catch()
}

async function updateList(container){
    const fetchResponse = await fetch("http://localhost:8000/api/cidades")
    const data = await fetchResponse.json()
    if(data.length > 0)
        container.innerText = ""
    data.forEach((cidade, index) => {
        /*
            TEXTO
         */
        // const element = document.createElement("div")
        // element.innerText = cidade.municipio + " - " + cidade.uf
        // element.classList.add("list-element")
        // container.appendChild(element)

        /*
            HTML INTERNO
         */
        const element = document.createElement("div")
        element.innerHTML = `
                <b> 
                ${cidade.uf}
                </b>
                <i>
                ${cidade.municipio}
                </i>        
        `

        element.classList.add("list-element")
        container.appendChild(element)
    })
}