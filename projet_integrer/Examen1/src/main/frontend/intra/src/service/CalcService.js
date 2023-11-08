
const add = async (one, two, setData) => {
    fetch(`http://localhost:8080/add/${one}/${two}`).then(
        response => response.json()
    ).then(
        data => setData(data['result'])
    ).catch(
        error => console.log(error)
    )
}
const sub = async (one, two, setData) => {
    fetch(`http://localhost:8080/sub/${one}/${two}`).then(
        response => response.json()
    ).then(
        data => setData(data['result'])
    ).catch(
        error => console.log(error)
    )

}

const exportedObject = {
    add, sub
}

export default exportedObject;