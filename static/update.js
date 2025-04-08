//function updateCity(el) {
//    product_id = el.value
//    fetch('/ready/' + product_id, {
//        method: 'patch',
//        headers: {'Content-Type': 'application/json'},
//        body: JSON.stringify({'ready': el.checked})
//    })
//}


function createCity(event) {
    event.preventDefault(); // Отключает стандартную отправку формы

    let totravel = document.getElementById('totravel').value;
    let date = document.getElementById('datE').value;

    fetch('/city', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            town: totravel || 'Пустое',
            visit_date: date || '15.10.2006'
        })
    })
    .then(response => {
        if (!response.ok) throw new Error('Ошибка при сохранении');
        return response.text();
    })
    .then(() => {
        setTimeout(() => location.reload(), 200); // даём SQLite немного времени
    })
    .catch(error => {
        console.error('Ошибка при добавлении города:', error);
    });
}
function clearCities() {
    fetch('/clear', {
        method: 'DELETE'
    })
    .then(() => {
        location.reload(); // Обновляем страницу после удаления
    })
    .catch(error => {
        console.error('Ошибка при очистке:', error);
    });
}

// Присваиваем окну с датой актуальную дату
window.onload = (() => {
    document.getElementById('datE').valueAsDate = new Date()
})