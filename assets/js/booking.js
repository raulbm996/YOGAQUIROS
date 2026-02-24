/**
 * Booking process logic for reservations UI
 */

let bookingData = {
    service: null,
    date: '23 de Marzo, 2026',
    time: null
};

// Auto-select based on URL parameters (e.g., came from classes page)
document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const styleParam = urlParams.get('style');

    if (styleParam) {
        // Capitalize first letter to match titles
        const serviceName = styleParam.charAt(0).toUpperCase() + styleParam.slice(1);
        selectService(serviceName, true);
    }
});

// Track current state
let currentStep = 1;

function selectService(serviceName, skipScroll = false) {
    bookingData.service = serviceName;

    // Update UI
    document.querySelectorAll('.service-card').forEach(card => {
        card.classList.remove('selected');
        if (card.querySelector('h4').textContent.includes(serviceName)) {
            card.classList.add('selected');
        }
    });

    // Enable next button
    document.getElementById('btn-next-1').disabled = false;

    // Optionally auto-advance if driven by URL
    if (skipScroll) {
        // We delay slightly to let UI render
        setTimeout(() => nextStep(2), 300);
    }
}

function selectDate(element) {
    if (element.classList.contains('disabled')) return;

    document.querySelectorAll('.day-cell').forEach(cell => {
        cell.classList.remove('selected');
    });

    element.classList.add('selected');
    bookingData.date = `${element.textContent} de Marzo, 2026`;

    // Reset time selection
    bookingData.time = null;
    document.querySelectorAll('.time-slot').forEach(slot => {
        slot.classList.remove('selected');
    });
    document.getElementById('btn-next-2').disabled = true;

    // Update slots header
    document.querySelector('.time-slots h4').textContent = `Disponibilidad para el ${element.textContent} de Mar`;

    // Simple demonstration of different times depending on day
    const container = document.getElementById('slots-container');
    container.innerHTML = ''; // mock clear

    const isTuesdayThursday = ['24', '26', '31'].includes(element.textContent);

    let slots = [];
    if (isTuesdayThursday) {
        slots = ['09:15', '10:30', '18:00', '19:15'];
    } else {
        slots = ['11:45', '18:00', '19:15', '20:30'];
    }

    slots.forEach(time => {
        const div = document.createElement('div');
        div.className = 'time-slot';
        div.textContent = time;
        div.onclick = function () { selectTime(this); };
        container.appendChild(div);
    });
}

function selectTime(element) {
    document.querySelectorAll('.time-slot').forEach(slot => {
        slot.classList.remove('selected');
    });

    element.classList.add('selected');
    bookingData.time = element.textContent;

    // Enable next button
    document.getElementById('btn-next-2').disabled = false;
}

function updateSummaryPreview() {
    const preview = document.getElementById('summary-preview');
    if (preview) {
        preview.innerHTML = `<strong>${bookingData.service} Yoga</strong> el <strong>${bookingData.date}</strong> a las <strong>${bookingData.time}h</strong>.`;
    }
}

function populateFinalSummary() {
    const s = document.getElementById('final-service');
    if (s) s.textContent = `${bookingData.service} Yoga`;
    const d = document.getElementById('final-date');
    if (d) d.textContent = bookingData.date;
    const t = document.getElementById('final-time');
    if (t) t.textContent = `${bookingData.time}h`;
}

/**
 * Universal step renderer
 */
function renderStep(stepNumber) {
    currentStep = stepNumber;

    if (currentStep === 3) updateSummaryPreview();
    if (currentStep === 4) populateFinalSummary();

    // Hide all contents
    document.querySelectorAll('.booking-step-content').forEach(content => {
        content.classList.remove('active');
    });

    // Show target content
    const target = document.getElementById(`step-${currentStep}`);
    if (target) target.classList.add('active');

    // Update indicators
    document.querySelectorAll('.step').forEach((indicator, index) => {
        const stepIdx = index + 1;
        indicator.classList.remove('active', 'completed');

        if (stepIdx === currentStep) {
            indicator.classList.add('active');
        } else if (stepIdx < currentStep) {
            indicator.classList.add('completed');
        }
    });

    // Update progress bar fill
    const progressFill = document.getElementById('progress-fill');
    if (progressFill) {
        // Calculate percentage: (currentStep - 1) / (totalSteps - 1) * 100
        // We have 4 steps total.
        const percentage = ((currentStep - 1) / 3) * 100;
        progressFill.style.width = `${percentage}%`;
    }

    // Scroll to top of booking section
    document.querySelector('.booking-section').scrollIntoView({ behavior: 'smooth' });
}

function nextStep(stepNumber) {
    renderStep(stepNumber);
}

function prevStep(stepNumber) {
    renderStep(stepNumber);
}

/**
 * Click handler for step indicators
 * Restricts jumping forward but allows going back
 */
function goToStep(stepNumber) {
    if (stepNumber < currentStep) {
        renderStep(stepNumber);
    }
}
