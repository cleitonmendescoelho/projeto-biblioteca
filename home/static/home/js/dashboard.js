(function () {
    const canvas = document.querySelector('[data-reading-chart]');

    if (!canvas || typeof Chart === 'undefined') {
        return;
    }

    const labelsElement = document.getElementById(canvas.dataset.labelsId);
    const valuesElement = document.getElementById(canvas.dataset.valuesId);

    if (!labelsElement || !valuesElement) {
        return;
    }

    const labels = JSON.parse(labelsElement.textContent);
    const values = JSON.parse(valuesElement.textContent);

    new Chart(canvas, {
        type: 'bar',
        data: {
            labels,
            datasets: [{
                label: 'Livros lidos',
                data: values,
                backgroundColor: 'rgba(59, 130, 246, 0.75)',
                borderColor: '#1d4ed8',
                borderWidth: 1,
                borderRadius: 6,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: { displayColors: false },
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { precision: 0 },
                    title: { display: true, text: 'Livros lidos' },
                },
                x: { title: { display: true, text: 'Data' } },
            },
        },
    });
}());
