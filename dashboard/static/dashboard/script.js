// Chart.js global configurations for styling
if (typeof Chart !== 'undefined') {
    Chart.defaults.color = '#64748b'; // slate 500
    Chart.defaults.font.family = "'Inter', sans-serif";
    Chart.defaults.plugins.tooltip.backgroundColor = '#062e22'; // forest green tooltip
    Chart.defaults.plugins.tooltip.titleColor = '#ffffff';
    Chart.defaults.plugins.tooltip.bodyColor = '#ffffff';
    Chart.defaults.plugins.tooltip.borderColor = '#f1f0eb';
    Chart.defaults.plugins.tooltip.borderWidth = 1;
}

document.addEventListener('DOMContentLoaded', function() {
    // 1. Initialise Charts on Dashboard Overview
    initOverviewCharts();
    
    // 2. Initialise Charts on Revenue Page
    initRevenueCharts();

    // 3. ID Verification Preview Modal Controls
    initVerificationModal();

    // 4. Online Users Real-time Fluctuation
    initOnlineCounter();

    // 5. Sidebar Toggle for Mobile Devices
    initSidebarToggle();
});

function initOverviewCharts() {
    const growthCanvas = document.getElementById('growthChart');
    if (growthCanvas) {
        const ctx = growthCanvas.getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                datasets: [{
                    label: 'Seekers',
                    data: [1200, 1400, 1550, 1720, 1900, 2100, 2250, 2400, 2600, 2800, 2950, 3120],
                    borderColor: '#062e22',
                    backgroundColor: 'rgba(6, 46, 34, 0.05)',
                    tension: 0.35,
                    fill: true,
                    borderWidth: 2.5
                }, {
                    label: 'Walis',
                    data: [400, 520, 600, 680, 780, 890, 940, 1020, 1150, 1250, 1380, 1490],
                    borderColor: '#d97706',
                    backgroundColor: 'transparent',
                    tension: 0.35,
                    borderWidth: 2
                }, {
                    label: 'Imams',
                    data: [35, 42, 48, 55, 62, 70, 78, 85, 90, 96, 102, 110],
                    borderColor: '#3b82f6',
                    backgroundColor: 'transparent',
                    tension: 0.35,
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'top', labels: { boxWidth: 12, usePointStyle: true } }
                },
                scales: {
                    x: { grid: { color: '#f1f0eb' } },
                    y: { grid: { color: '#f1f0eb' } }
                }
            }
        });
    }

    const reachCanvas = document.getElementById('reachChart');
    if (reachCanvas) {
        const niger = parseInt(reachCanvas.getAttribute('data-niger') || '1420');
        const kwara = parseInt(reachCanvas.getAttribute('data-kwara') || '640');
        const fct = parseInt(reachCanvas.getAttribute('data-fct') || '510');
        const kogi = parseInt(reachCanvas.getAttribute('data-kogi') || '310');
        const diaspora = parseInt(reachCanvas.getAttribute('data-diaspora') || '240');

        const ctx = reachCanvas.getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Niger', 'Kwara', 'FCT', 'Kogi', 'Diaspora'],
                datasets: [{
                    data: [niger, kwara, fct, kogi, diaspora],
                    backgroundColor: [
                        '#062e22',
                        '#16a34a',
                        '#3b82f6',
                        '#d97706',
                        '#9333ea'
                    ],
                    borderWidth: 0,
                    hoverOffset: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'right', labels: { boxWidth: 12, usePointStyle: true } }
                },
                cutout: '70%'
            }
        });
    }

    const funnelCanvas = document.getElementById('funnelChart');
    if (funnelCanvas) {
        const ctx = funnelCanvas.getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Registered', 'Wali Linked', 'Verified', 'Matched', 'Active Chat', 'Meeting Planned', 'Nikah'],
                datasets: [{
                    label: 'Users',
                    data: [3120, 2200, 1490, 800, 341, 98, 47],
                    backgroundColor: '#062e22',
                    borderColor: '#062e22',
                    borderWidth: 0,
                    borderRadius: 4,
                    barPercentage: 0.6
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    x: { grid: { color: '#f1f0eb' } },
                    y: { grid: { display: false } }
                }
            }
        });
    }

    const revenueOverviewCanvas = document.getElementById('revenueOverviewChart');
    if (revenueOverviewCanvas) {
        const ctx = revenueOverviewCanvas.getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
                datasets: [{
                    label: 'Monthly Revenue (USD)',
                    data: [4200, 5100, 5800, 6200, 6900, 7500, 8100, 8420],
                    backgroundColor: '#062e22',
                    borderColor: '#062e22',
                    borderWidth: 0,
                    borderRadius: 4,
                    barPercentage: 0.6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    x: { grid: { display: false } },
                    y: { grid: { color: '#f1f0eb' } }
                }
            }
        });
    }
}

function initRevenueCharts() {
    const subCanvas = document.getElementById('subscriptionChart');
    if (subCanvas) {
        const subVal = parseInt(subCanvas.getAttribute('data-sub') || '50');
        const matchVal = parseInt(subCanvas.getAttribute('data-match') || '40');
        const donVal = parseInt(subCanvas.getAttribute('data-don') || '10');

        const ctx = subCanvas.getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Premium Subscriptions', 'Matchmaking Fees', 'Donations'],
                datasets: [{
                    data: [subVal, matchVal, donVal],
                    backgroundColor: ['#062e22', '#d97706', '#3b82f6'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'bottom', labels: { boxWidth: 12, usePointStyle: true } }
                },
                cutout: '70%'
            }
        });
    }
}

function initVerificationModal() {
    const modal = document.getElementById('idModal');
    if (!modal) return;

    const closeBtn = modal.querySelector('.modal-close-btn');
    const modalImg = modal.querySelector('.id-preview-img');
    const modalUser = modal.querySelector('#modalUserName');
    const modalDoc = modal.querySelector('#modalDocType');
    const approveForm = modal.querySelector('#modalApproveForm');
    const rejectForm = modal.querySelector('#modalRejectForm');

    // Attach click events to all "Review" buttons
    document.querySelectorAll('.btn-review-id').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const id = this.getAttribute('data-id');
            const user = this.getAttribute('data-user');
            const doc = this.getAttribute('data-doc');
            const previewUrl = this.getAttribute('data-url');

            modalUser.textContent = user;
            modalDoc.textContent = doc;
            modalImg.src = previewUrl;

            // Set hidden inputs inside forms
            approveForm.querySelector('input[name="request_id"]').value = id;
            rejectForm.querySelector('input[name="request_id"]').value = id;

            modal.style.display = 'flex';
        });
    });

    // Close Modal actions
    const closeModal = () => { modal.style.display = 'none'; };
    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });
}

function initOnlineCounter() {
    const counterEl = document.getElementById('onlineCounter');
    if (!counterEl) return;

    let baseCount = 141;
    setInterval(() => {
        const fluctuation = Math.floor(Math.random() * 5) - 2;
        baseCount = Math.max(120, Math.min(180, baseCount + fluctuation));
        counterEl.textContent = `${baseCount} online`;
    }, 4000);
}

function initSidebarToggle() {
    const toggleBtn    = document.getElementById('sidebarToggle');
    const closeBtn     = document.getElementById('sidebarClose');
    const overlay      = document.getElementById('sidebarOverlay');
    const appContainer = document.getElementById('appContainer');

    function openSidebar()  { appContainer.classList.add('sidebar-open'); }
    function closeSidebar() { appContainer.classList.remove('sidebar-open'); }

    if (toggleBtn)  toggleBtn.addEventListener('click', openSidebar);
    if (closeBtn)   closeBtn.addEventListener('click', closeSidebar);
    if (overlay)    overlay.addEventListener('click', closeSidebar);

    // Close on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeSidebar();
    });
}
