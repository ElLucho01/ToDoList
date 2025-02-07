document.addEventListener('DOMContentLoaded', function () {
    const checks = document.querySelectorAll('.check');
    checks.forEach(check => {
        check.addEventListener('click', function () {
            id = check.getAttribute('name').slice(1);
            window.location.href = window.location.href + '/togItem/' + id;
        })
})
})
