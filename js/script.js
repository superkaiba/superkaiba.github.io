let pubsBatch = 0;
let expBatch = 0;
let pubsExpanded = false;
let expExpanded = false;

function showMorePublications() {
    if (!pubsExpanded) {
        // Show more
        pubsBatch++;
        const itemsToShow = document.querySelectorAll(`.hidden-pub[data-batch="${pubsBatch}"]`);
        const btn = document.getElementById('pubs-btn');

        itemsToShow.forEach(item => {
            item.style.display = 'flex';
        });

        // Check if there are more items to show
        const remainingItems = document.querySelectorAll('.hidden-pub[style="display: none;"]');
        if (remainingItems.length === 0) {
            btn.textContent = 'Show Less';
            pubsExpanded = true;
        }
    } else {
        // Show less - hide everything except first 3
        const allItems = document.querySelectorAll('[data-batch]');
        const pubItems = Array.from(allItems).filter(item => item.classList.contains('hidden-pub') || item.hasAttribute('data-batch'));

        document.querySelectorAll('.hidden-pub').forEach(item => {
            item.style.display = 'none';
        });

        pubsBatch = 0;
        pubsExpanded = false;
        document.getElementById('pubs-btn').textContent = 'Show More';
    }
}

function showMoreExperience() {
    if (!expExpanded) {
        // Show more
        expBatch++;
        const itemsToShow = document.querySelectorAll(`.hidden-exp[data-batch="${expBatch}"]`);
        const btn = document.getElementById('exp-btn');

        itemsToShow.forEach(item => {
            item.style.display = 'flex';
        });

        // Check if there are more items to show
        const remainingItems = document.querySelectorAll('.hidden-exp[style="display: none;"]');
        if (remainingItems.length === 0) {
            btn.textContent = 'Show Less';
            expExpanded = true;
        }
    } else {
        // Show less - hide everything except first 3
        document.querySelectorAll('.hidden-exp').forEach(item => {
            item.style.display = 'none';
        });

        expBatch = 0;
        expExpanded = false;
        document.getElementById('exp-btn').textContent = 'Show More';
    }
}

// Initialize hidden items on page load
document.addEventListener('DOMContentLoaded', function() {
    // Hide all publications with hidden-pub class
    document.querySelectorAll('.hidden-pub').forEach(pub => {
        pub.style.display = 'none';
    });

    // Hide all experience with hidden-exp class
    document.querySelectorAll('.hidden-exp').forEach(exp => {
        exp.style.display = 'none';
    });
});
