// Load and render CV data
let cvData = null;

// Load CV data from JSON
async function loadCVData() {
    try {
        const response = await fetch('data/cv-data.json');
        cvData = await response.json();
        renderPage();
    } catch (error) {
        console.error('Error loading CV data:', error);
    }
}

// Render the entire page
function renderPage() {
    if (!cvData) return;

    renderFeatured();
    renderPublications();
    renderResearchExperience();
    renderIndustryExperience();
    renderAwards();
    renderTeaching();
    renderService();
    renderPress();
    renderInvitedTalks();
}

// Render featured projects section (publications only)
function renderFeatured() {
    const container = document.getElementById('featured-container');
    if (!container) return;

    const featured = [];

    // Collect only featured publications
    if (cvData.publications && cvData.publications.conferences) {
        cvData.publications.conferences.filter(p => p.featured).forEach(p => {
            featured.push({
                year: p.year,
                data: p
            });
        });
    }

    // Sort by year (reverse chronological)
    featured.sort((a, b) => b.year - a.year);

    // Render featured papers
    const html = featured.map(f => {
        const p = f.data;
        const authorsStr = p.authors.join(', ');

        return `
        <li class="featured-paper" data-id="featured-${p.id}">
            <div class="paper-main-card">
                <div class="paper-header-row">
                    <h3 class="paper-title">${p.title}</h3>
                    <span class="paper-venue">${p.venue} ${p.year}${p.award ? ' · ' + p.award : ''}</span>
                </div>
                <p class="paper-authors">${authorsStr}</p>
                <p class="paper-description">${p.summary}</p>
                <div class="paper-actions">
                    ${p.abstract ? `<button class="paper-btn secondary-btn" onclick="toggleAbstract('${p.id}')">
                        <span class="abstract-btn-text" id="abstract-btn-${p.id}">Show Abstract</span>
                    </button>` : ''}
                    <a href="${p.link}" target="_blank" class="paper-btn primary-btn">
                        View Paper →
                    </a>
                </div>
                ${p.abstract ? `<div class="paper-abstract" id="abstract-${p.id}" style="display: none;">
                    <p>${p.abstract}</p>
                </div>` : ''}
            </div>
        </li>
        `;
    }).join('');

    container.innerHTML = html;
}

// Toggle abstract visibility
function toggleAbstract(paperId) {
    const abstractDiv = document.getElementById(`abstract-${paperId}`);
    const btnText = document.getElementById(`abstract-btn-${paperId}`);

    if (abstractDiv.style.display === 'none') {
        abstractDiv.style.display = 'block';
        btnText.textContent = 'Hide Abstract';
    } else {
        abstractDiv.style.display = 'none';
        btnText.textContent = 'Show Abstract';
    }
}

// Render publications section
function renderPublications() {
    renderPublicationSubsection('conferences', 'conferences-list');
    renderPublicationSubsection('workshops', 'workshops-list');
}

function renderPublicationSubsection(type, containerId) {
    const container = document.getElementById(containerId);
    if (!container || !cvData.publications || !cvData.publications[type]) return;

    const pubs = cvData.publications[type];
    const html = pubs.map(pub => `
        <li class="expandable-item" data-id="${pub.id}">
            <div class="item-header" onclick="toggleItem('${pub.id}')">
                <div class="item-main">
                    <div class="pub-title-row">
                        <a href="${pub.link}" target="_blank" onclick="event.stopPropagation()">${pub.title}</a>
                        <span class="meta">${pub.venue} ${pub.year}${pub.award ? ' · ' + pub.award : ''}</span>
                    </div>
                    <p class="item-summary">${pub.summary}</p>
                </div>
                <button class="toggle-btn" aria-label="Expand">
                    <i class="fas fa-chevron-down"></i>
                </button>
            </div>
            <div class="item-details" style="display: none;">
                <p class="detail-line"><strong>Authors:</strong> ${pub.authors.join(', ')}</p>
            </div>
        </li>
    `).join('');

    container.innerHTML = html;
}

// Render research experience
function renderResearchExperience() {
    const container = document.getElementById('research-exp-list');
    if (!container || !cvData.research_experience) return;

    const exps = cvData.research_experience;
    const html = exps.map(exp => {
        const dateStr = formatDateRange(exp.start_date, exp.end_date);
        const mentorsHtml = exp.mentors && exp.mentors.length > 0
            ? `<p class="detail-line"><strong>Mentors:</strong> ${formatMentors(exp)}</p>`
            : '';

        return `
            <li class="expandable-item" data-id="${exp.id}">
                <div class="item-header" onclick="toggleItem('${exp.id}')">
                    <div class="item-main">
                        <div class="exp-header">
                            <span class="exp-company"><a href="${exp.company_url}" target="_blank" onclick="event.stopPropagation()">${exp.company}</a></span>
                            <span class="meta">${dateStr}</span>
                        </div>
                        <p class="exp-role">${exp.position}</p>
                        <p class="item-summary">${exp.summary}</p>
                    </div>
                    <button class="toggle-btn" aria-label="Expand">
                        <i class="fas fa-chevron-down"></i>
                    </button>
                </div>
                <div class="item-details" style="display: none;">
                    <p class="detail-line">${exp.details}</p>
                    ${mentorsHtml}
                    ${exp.technologies ? `<p class="detail-line"><strong>Technologies:</strong> ${exp.technologies.join(', ')}</p>` : ''}
                </div>
            </li>
        `;
    }).join('');

    container.innerHTML = html;
}

// Render industry experience
function renderIndustryExperience() {
    const container = document.getElementById('industry-exp-list');
    if (!container || !cvData.industry_experience) return;

    const exps = cvData.industry_experience;
    const html = exps.map(exp => {
        const dateStr = formatDateRange(exp.start_date, exp.end_date);

        return `
            <li class="expandable-item" data-id="${exp.id}">
                <div class="item-header" onclick="toggleItem('${exp.id}')">
                    <div class="item-main">
                        <div class="exp-header">
                            <span class="exp-company"><a href="${exp.company_url}" target="_blank" onclick="event.stopPropagation()">${exp.company}</a></span>
                            <span class="meta">${dateStr}</span>
                        </div>
                        <p class="exp-role">${exp.position}</p>
                        <p class="item-summary">${exp.summary}</p>
                    </div>
                    <button class="toggle-btn" aria-label="Expand">
                        <i class="fas fa-chevron-down"></i>
                    </button>
                </div>
                <div class="item-details" style="display: none;">
                    <p class="detail-line">${exp.details}</p>
                    ${exp.technologies ? `<p class="detail-line"><strong>Technologies:</strong> ${exp.technologies.join(', ')}</p>` : ''}
                </div>
            </li>
        `;
    }).join('');

    container.innerHTML = html;
}

// Render awards
function renderAwards() {
    const container = document.getElementById('awards-list');
    if (!container || !cvData.awards) return;

    const html = cvData.awards.map(award => {
        const amountStr = award.amount ? ` - ${award.amount}` : '';
        const descStr = award.description ? ` - ${award.description}` : '';

        return `
            <li class="award-item">
                <div class="award-header">
                    <span class="award-title">${award.link ? `<a href="${award.link}" target="_blank">${award.title}</a>` : award.title}</span>
                    <span class="meta">${award.year}</span>
                </div>
                ${amountStr || descStr ? `<p class="award-details">${amountStr}${descStr}</p>` : ''}
            </li>
        `;
    }).join('');

    container.innerHTML = html;
}

// Render teaching
function renderTeaching() {
    const container = document.getElementById('teaching-list');
    if (!container || !cvData.teaching) return;

    const html = cvData.teaching.map(t => {
        const dateStr = t.year ? t.year : `${t.start_date}–${t.end_date}`;

        return `
            <li class="teaching-item">
                <div class="teaching-header">
                    <span class="teaching-course">${t.role} - ${t.course}</span>
                    <span class="meta">${dateStr}</span>
                </div>
                <p class="teaching-inst">${t.institution_url ? `<a href="${t.institution_url}" target="_blank">${t.institution}</a>` : t.institution}</p>
            </li>
        `;
    }).join('');

    container.innerHTML = html;
}

// Render service & outreach
function renderService() {
    const container = document.getElementById('service-list');
    if (!container || !cvData.service) return;

    const html = cvData.service.map(s => {
        const dateStr = s.year ? s.year : `${s.start_date}${s.end_date ? '–' + s.end_date : ''}`;

        return `
            <li class="service-item">
                <div class="service-header">
                    <span class="service-role">${s.role}</span>
                    <span class="meta">${dateStr}</span>
                </div>
                <p class="service-org">${s.organization_url ? `<a href="${s.organization_url}" target="_blank">${s.organization}</a>` : s.organization}</p>
            </li>
        `;
    }).join('');

    container.innerHTML = html;
}

// Render press
function renderPress() {
    const container = document.getElementById('press-list');
    if (!container || !cvData.press) return;

    const html = cvData.press.map(p => {
        return `
            <li class="press-item">
                <a href="${p.link}" target="_blank" class="press-title">${p.title}</a>
                <p class="press-meta">${p.outlet} - ${p.author} - ${formatDate(p.date)}</p>
                <p class="press-summary">${p.summary}</p>
            </li>
        `;
    }).join('');

    container.innerHTML = html;
}

// Render invited talks
function renderInvitedTalks() {
    const container = document.getElementById('talks-list');
    if (!container || !cvData.invited_talks) return;

    const html = cvData.invited_talks.map(t => {
        return `
            <li class="talk-item">
                <span class="talk-event">${t.link ? `<a href="${t.link}" target="_blank">${t.event}</a>` : t.event}</span>
                <span class="meta">${t.year}</span>
            </li>
        `;
    }).join('');

    container.innerHTML = html;
}

// Toggle expand/collapse for an item
function toggleItem(itemId) {
    const item = document.querySelector(`[data-id="${itemId}"]`);
    if (!item) return;

    const details = item.querySelector('.item-details');
    const icon = item.querySelector('.toggle-btn i');

    if (details.style.display === 'none') {
        details.style.display = 'block';
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-up');
    } else {
        details.style.display = 'none';
        icon.classList.remove('fa-chevron-up');
        icon.classList.add('fa-chevron-down');
    }
}

// Helper functions
function formatDateRange(start, end) {
    if (!start) return '';

    const startDate = new Date(start);
    const startStr = startDate.toLocaleDateString('en-US', { month: 'short', year: 'numeric' });

    if (!end) return startStr;
    if (end === 'Present') return `${startStr}–Present`;

    const endDate = new Date(end);
    const endStr = endDate.toLocaleDateString('en-US', { month: 'short', year: 'numeric' });

    return `${startStr}–${endStr}`;
}

function formatDate(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
}

function formatMentors(exp) {
    if (!exp.mentors || exp.mentors.length === 0) return '';

    return exp.mentors.map(mentor => {
        if (exp.mentor_links && exp.mentor_links[mentor]) {
            return `<a href="${exp.mentor_links[mentor]}" target="_blank"><span class="mentor">${mentor}</span></a>`;
        }
        return `<span class="mentor">${mentor}</span>`;
    }).join(', ');
}

// Toggle section expand/collapse
function toggleSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (!section) return;

    const content = section.querySelector('.section-content');
    const icon = section.querySelector('.section-toggle-btn i');

    if (content.classList.contains('collapsed')) {
        content.classList.remove('collapsed');
        content.style.maxHeight = content.scrollHeight + 'px';
        setTimeout(() => {
            content.style.maxHeight = 'none';
        }, 300);
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-up');
    } else {
        content.style.maxHeight = content.scrollHeight + 'px';
        setTimeout(() => {
            content.classList.add('collapsed');
            content.style.maxHeight = '0';
        }, 10);
        icon.classList.remove('fa-chevron-up');
        icon.classList.add('fa-chevron-down');
    }
}

// Toggle subsection expand/collapse
function toggleSubsection(subsectionId) {
    const content = document.getElementById(`${subsectionId}-content`);
    const subsection = content.closest('.collapsible-subsection');
    if (!subsection) return;

    const icon = subsection.querySelector('.subsection-toggle-btn i');

    if (content.classList.contains('collapsed')) {
        content.classList.remove('collapsed');
        content.style.maxHeight = content.scrollHeight + 'px';
        setTimeout(() => {
            content.style.maxHeight = 'none';
        }, 300);
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-up');
    } else {
        content.style.maxHeight = content.scrollHeight + 'px';
        setTimeout(() => {
            content.classList.add('collapsed');
            content.style.maxHeight = '0';
        }, 10);
        icon.classList.remove('fa-chevron-up');
        icon.classList.add('fa-chevron-down');
    }
}

// Initialize Complete CV sections as collapsed
function initializeCollapsedSections() {
    const cvSections = ['publications', 'research-experience', 'industry-experience', 'awards', 'teaching', 'service', 'press', 'talks'];

    cvSections.forEach(sectionId => {
        const section = document.getElementById(sectionId);
        if (!section) return;

        const content = section.querySelector('.section-content');
        const icon = section.querySelector('.section-toggle-btn i');

        if (content && icon) {
            content.classList.add('collapsed');
            content.style.maxHeight = '0';
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
        }
    });

    // Also collapse subsections
    const subsections = ['conferences', 'workshops'];
    subsections.forEach(subId => {
        const content = document.getElementById(`${subId}-content`);
        if (!content) return;

        const subsection = content.closest('.collapsible-subsection');
        if (!subsection) return;

        const icon = subsection.querySelector('.subsection-toggle-btn i');
        if (icon) {
            content.classList.add('collapsed');
            content.style.maxHeight = '0';
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
        }
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    loadCVData();
    // Wait for content to render before collapsing
    setTimeout(initializeCollapsedSections, 100);
});
