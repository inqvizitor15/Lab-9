//function updateCity(el) {
//    product_id = el.value
//    fetch('/ready/' + product_id, {
//        method: 'patch',
//        headers: {'Content-Type': 'application/json'},
//        body: JSON.stringify({'ready': el.checked})
//    })
//}

function createCity(){
    console.log('Create')
    let totravel = document.getElementById('totravel').value
    let date = document.getElementById('datE').value

    fetch('/city', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'town': totravel || 'Пустое',
                            'visit_date': date || '15.10.2006'})
    })

    // Новая часть от гпт
    .then(response => {
        if (!response.ok) {
            throw new Error('Ошибка при сохранении города');
        }
        return response.json(); // Ждём JSON-ответ от сервера
    })
    .then(data => {
        if (data.status === 'success') {
            console.log('Город успешно сохранён');
            setTimeout(() => {
                location.reload(); // Немного подождать и обновить страницу
            }, 200); // 200 мс — достаточно для завершения записи в SQLite
        } else {
            console.error('Ответ сервера некорректен:', data);
        }
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