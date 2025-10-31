// Render About section dynamically from JSON
function renderAboutSection() {
    const cvData = window.cvData;
    if (!cvData || !cvData.about_config) {
        console.log('About rendering skipped - no data', cvData);
        return;
    }
    console.log('Rendering About section', cvData.about_config);

    const config = cvData.about_config;

    // Render current paragraph
    const currentElem = document.querySelector('.about-current');
    if (currentElem) {
        currentElem.innerHTML = config.current_paragraph;
    }

    // Render previous paragraph
    const previousElem = document.querySelector('.about-previous');
    if (previousElem) {
        previousElem.innerHTML = config.previous_paragraph;
    }

    // Render research goal paragraph
    const researchGoalElem = document.querySelector('.about-research-goal');
    if (researchGoalElem && config.research_goal_paragraph) {
        researchGoalElem.innerHTML = config.research_goal_paragraph;
    }

    // Render contact
    const contactElem = document.querySelector('.about-contact');
    if (contactElem) {
        contactElem.innerHTML = `Always happy to chat, collaborate, or mentor → <a href="mailto:${config.email}"><strong>${config.email}</strong></a>`;
    }

    // Render CTA
    const ctaElem = document.querySelector('.hero-cta');
    if (ctaElem) {
        ctaElem.innerHTML = config.cta.replace('featured projects', '<a href="#featured">featured projects</a>').replace('complete CV', '<a href="#complete-cv">complete CV</a>');
    }
}

function renderAboutItems(items) {
    return items.map(item => {
        if (item.type === 'position') {
            return renderPositionItem(item);
        } else if (item.type === 'award') {
            return renderAwardItem(item);
        } else if (item.type === 'education') {
            return renderEducationItem(item);
        } else if (item.type === 'service') {
            return renderServiceItem(item);
        } else if (item.type === 'research_interests') {
            return renderResearchInterests(item);
        } else if (item.type === 'past_work_areas') {
            return renderPastWorkAreas(item);
        }
        return '';
    }).join('');
}

function renderPositionItem(item) {
    const data = findDataById(item.ref_type, item.ref_id);
    if (!data) return '';

    const dateStr = formatDateRange(data.start_date, data.end_date);
    const context = getPositionContext(data);
    const mentorsList = data.mentors && data.mentors.length > 0 ? data.mentors.map(m => {
        if (data.mentor_links && data.mentor_links[m]) {
            return `<a href="${data.mentor_links[m]}" target="_blank">${m}</a>`;
        }
        return m;
    }).join(', ') : '';
    const mentorsHtml = mentorsList ? `<br>Mentored by ${mentorsList}` : '';

    return `
        <li class="expandable-about-item">
            <span class="about-item-title">${data.position} at <a href="${data.company_url}" target="_blank">${data.company}</a>${context ? ` (${context})` : ''}</span>
            <div class="about-item-details" style="display: none;">
                ${dateStr} · ${data.summary}${mentorsHtml}
            </div>
        </li>
    `;
}

function renderAwardItem(item) {
    const data = findDataById(item.ref_type, item.ref_id);
    if (!data) return '';

    let titleText = data.title;
    let contextText = '';

    if (data.id === 'heidelberg-2023') {
        titleText = `Invited to <a href="${data.link}" target="_blank">Heidelberg Laureate Forum</a>`;
        contextText = '(most promising young researchers in math & CS)';
    } else if (data.id === 'project-x-winner-2022') {
        titleText = 'Winner of Project X';
        contextText = '($25k prize)';
    } else if (data.id === 'vanier-2025') {
        titleText = `<a href="${data.link}" target="_blank">Vanier Scholar</a>`;
        contextText = '';
    } else {
        titleText = data.link ? `<a href="${data.link}" target="_blank">${data.title}</a>` : data.title;
    }

    return `
        <li class="expandable-about-item">
            <span class="about-item-title">${titleText}${contextText ? ` ${contextText}` : ''}</span>
            <div class="about-item-details" style="display: none;">
                ${data.year}${data.description ? ` · ${data.description}` : ''}${data.amount ? ` · ${data.amount}` : ''}
            </div>
        </li>
    `;
}

function renderEducationItem(item) {
    const data = findDataById(item.ref_type, item.ref_id);
    if (!data) return '';

    const isPhD = data.degree.includes('PhD');
    const supervisors = data.supervisors ? data.supervisors.map(s => {
        if (data.supervisor_links && data.supervisor_links[s]) {
            return `<a href="${data.supervisor_links[s]}" target="_blank">${s}</a>`;
        }
        return s;
    }).join(' & ') : '';

    if (isPhD) {
        const dateStr = `${data.start_date.split('-')[0]}-${data.end_date.split('-')[0]} (expected)`;
        const awardsHtml = data.awards ? data.awards.map(a => `• ${a}`).join('<br>') : '';
        const papersHtml = data.key_papers ? data.key_papers.map(id => {
            const paper = findPaperById(id);
            return paper ? `• <a href="${paper.link}" target="_blank">${paper.title}</a> (${paper.venue} ${paper.year})` : '';
        }).filter(p => p).join('<br>') : '';

        return `
            <li class="expandable-about-item">
                <span class="about-item-title">PhD at <a href="https://mila.quebec/en/" target="_blank">Mila</a>/<a href="${data.institution_url}" target="_blank">UdeM</a> with ${supervisors}</span>
                <div class="about-item-details" style="display: none;">
                    ${dateStr} · ${data.thesis_topic}<br><br><strong>Funding:</strong><br>${awardsHtml}${papersHtml ? '<br><br><strong>Key papers:</strong><br>' + papersHtml : ''}
                </div>
            </li>
        `;
    } else {
        // BSc
        const dateStr = `${data.start_date.split('-')[0]}-${data.end_date.split('-')[0]}`;
        const clubsHtml = data.clubs ? data.clubs.map(c => `• ${c}`).join('<br>') : '';

        return `
            <li class="expandable-about-item">
                <span class="about-item-title">BSc from <a href="${data.institution_url}" target="_blank">${data.institution}</a></span>
                <div class="about-item-details" style="display: none;">
                    ${dateStr} · ${data.degree} · GPA: ${data.gpa}<br><br>${data.notes}<br><br>${data.undergrad_research}<br><br><strong>Activities:</strong><br>${clubsHtml}
                </div>
            </li>
        `;
    }
}

function renderServiceItem(item) {
    const data = findDataById(item.ref_type, item.ref_id);
    if (!data) return '';

    const dateStr = data.year ? data.year : `${data.start_date}${data.end_date ? ' – ' + data.end_date : ''}`;
    const orgLink = data.organization_url ? `<a href="${data.organization_url}" target="_blank">${data.organization}</a>` : data.organization;

    return `
        <li class="expandable-about-item">
            <span class="about-item-title">${data.role} at ${orgLink}</span>
            <div class="about-item-details" style="display: none;">
                ${dateStr}
            </div>
        </li>
    `;
}

function renderResearchInterests(item) {
    const interestsHtml = item.interests.map(interest => {
        const papersHtml = interest.papers.map(paperId => {
            const paper = findPaperById(paperId);
            return paper ? `• <a href="${paper.link}" target="_blank">${paper.title}</a> (${paper.venue} ${paper.year})` : '';
        }).filter(p => p).join('<br>');

        return `
            <li class="expandable-about-item">
                <span class="about-item-title">Research: ${interest.name}</span>
                <div class="about-item-details" style="display: none;">
                    ${papersHtml}
                </div>
            </li>
        `;
    }).join('');

    return interestsHtml;
}

function renderPastWorkAreas(item) {
    const areasHtml = item.areas.map(area => {
        const papersHtml = area.papers.map(paperId => {
            const paper = findPaperById(paperId);
            return paper ? `• <a href="${paper.link}" target="_blank">${paper.title}</a> (${paper.venue} ${paper.year})` : '';
        }).filter(p => p).join('<br>');

        return `
            <li class="expandable-about-item">
                <span class="about-item-title">Past work: ${area.name}</span>
                <div class="about-item-details" style="display: none;">
                    ${papersHtml}
                </div>
            </li>
        `;
    }).join('');

    return areasHtml;
}

// Helper functions
function findDataById(refType, refId) {
    const cvData = window.cvData;
    if (!cvData) return null;

    if (refType === 'research_experience') {
        return cvData.research_experience.find(e => e.id === refId);
    } else if (refType === 'awards') {
        return cvData.awards.find(a => a.id === refId);
    } else if (refType === 'education') {
        return cvData.education.find(e => e.id === refId);
    } else if (refType === 'service') {
        return cvData.service.find(s => s.id === refId);
    }
    return null;
}

function findPaperById(paperId) {
    const cvData = window.cvData;
    if (!cvData) return null;

    if (cvData.publications && cvData.publications.conferences) {
        const conf = cvData.publications.conferences.find(p => p.id === paperId);
        if (conf) return conf;
    }
    if (cvData.publications && cvData.publications.workshops) {
        const workshop = cvData.publications.workshops.find(p => p.id === paperId);
        if (workshop) return workshop;
    }
    return null;
}

function getPositionContext(data) {
    // Extract the context from summary (text in parentheses)
    if (data.company === 'Anthropic') return 'mechanistic interpretability';
    if (data.company === 'Occam AI') return 'LLM agents';
    if (data.company === 'Waabi') return 'autonomous driving simulation';
    if (data.company.includes('Blake Richards')) return 'neuroscience RL';
    if (data.company.includes('Doina Precup')) return 'model-based RL';
    return '';
}

// Attach event listeners to expandable About items
function attachAboutListeners() {
    document.querySelectorAll('.expandable-about-item').forEach(item => {
        item.addEventListener('click', function(e) {
            // Don't trigger if clicking on a link
            if (e.target.tagName === 'A') return;

            const details = this.querySelector('.about-item-details');
            if (details) {
                if (details.style.display === 'none' || details.style.display === '') {
                    details.style.display = 'block';
                    this.classList.add('expanded');
                } else {
                    details.style.display = 'none';
                    this.classList.remove('expanded');
                }
            }
        });
    });
}

// Helper to format date ranges (also used by cv-renderer.js)
function formatDateRange(start, end) {
    if (!start) return '';

    const startDate = new Date(start);
    const startStr = startDate.toLocaleDateString('en-US', { month: 'short', year: 'numeric' });

    if (!end) return startStr;
    if (end === 'Present' || end === 'present') return `${startStr}–Present`;

    const endDate = new Date(end);
    const endStr = endDate.toLocaleDateString('en-US', { month: 'short', year: 'numeric' });

    return `${startStr}–${endStr}`;
}
