function updateCity(el) {
    product_id = el.value
    fetch('/ready/' + product_id, {
        method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'ready': el.checked})
    })
//    console.log(product_id)

}

//function addProduct() {
//    let prodName = document.getElementById('prod_name').value
//    let price = document.getElementById('price').value
//    fetch('/add', {
//        method: 'post',
//        headers: {'Content-Type': 'application/json'},
//        body: JSON.stringify({'prod_name': prodName,
//                             'price': price,
//                             'in_stock': true})
//    })
////    console.log("Add")
//}

function createCity(){
    console.log('Create')
    let totravel = document.getElementByld('totravel').value
    let date = document.getElementByld('date').value

    fetch('/city', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'totravel': totravel || 'Пустое', \
                            'date': date || '15.10.2006', 'ready': false})
    })
}