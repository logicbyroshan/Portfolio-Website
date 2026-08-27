/**
 * Roshan Portfolio Admin Custom JS
 * Provides interactive auto-detection preview for skill icons across 3 CDN tiers
 * and improves form UI interactions.
 */

document.addEventListener('DOMContentLoaded', function () {
    // ----------------------------------------------------
    // 1. Skill Admin Live Icon Auto-Detection Preview
    // ----------------------------------------------------
    const skillNameInput = document.getElementById('id_name');
    const skillIconInput = document.getElementById('id_icon');

    if (skillNameInput) {
        // Create an icon preview container
        const previewContainer = document.createElement('div');
        previewContainer.id = 'skill-live-icon-preview';
        previewContainer.className = 'admin-live-icon-card';
        previewContainer.innerHTML = `
            <div class="live-icon-badge-row">
                <div class="live-icon-thumb" id="live-icon-img-box">
                    <span id="live-icon-placeholder">⚡</span>
                    <img id="live-icon-img" src="" alt="Icon Preview" style="display:none;" />
                </div>
                <div class="live-icon-info">
                    <div class="live-icon-status" id="live-icon-status">Type a skill name to auto-discover icons...</div>
                    <div class="live-icon-subtext" id="live-icon-subtext">Supports 3-tier fallback (Devicon &bull; SimpleIcons &bull; SkillIcons)</div>
                </div>
            </div>
        `;

        // Insert right after the name row or icon row
        const targetRow = skillIconInput ? skillIconInput.closest('.form-group') || skillIconInput.parentElement : skillNameInput.closest('.form-group');
        if (targetRow) {
            targetRow.parentNode.insertBefore(previewContainer, targetRow);
        }

        let debounceTimer = null;
        function checkSkillIcon(nameVal) {
            const trimmed = nameVal.trim();
            const statusEl = document.getElementById('live-icon-status');
            const subtextEl = document.getElementById('live-icon-subtext');
            const imgEl = document.getElementById('live-icon-img');
            const placeholderEl = document.getElementById('live-icon-placeholder');
            const boxEl = document.getElementById('live-icon-img-box');

            if (!trimmed) {
                statusEl.innerHTML = 'Type a skill name to auto-discover icons...';
                statusEl.className = 'live-icon-status';
                subtextEl.innerHTML = 'Supports 3-tier fallback (Devicon &bull; SimpleIcons &bull; SkillIcons)';
                imgEl.style.display = 'none';
                placeholderEl.style.display = 'inline';
                boxEl.classList.remove('found');
                return;
            }

            statusEl.innerHTML = '🔍 Searching icon libraries...';
            statusEl.className = 'live-icon-status searching';

            fetch(`/api/skill-icon-lookup/?name=${encodeURIComponent(trimmed)}`)
                .then(res => res.json())
                .then(data => {
                    if (data.found && data.url) {
                        imgEl.src = data.url;
                        imgEl.style.display = 'block';
                        placeholderEl.style.display = 'none';
                        boxEl.classList.add('found');
                        statusEl.innerHTML = `✨ <b>Auto-Found in ${data.source}</b> (${data.normalized})`;
                        statusEl.className = 'live-icon-status found';
                        subtextEl.innerHTML = `This icon will be auto-downloaded on save. You can upload a custom file below to override.`;
                    } else {
                        imgEl.style.display = 'none';
                        placeholderEl.style.display = 'inline';
                        boxEl.classList.remove('found');
                        statusEl.innerHTML = `⚠️ No auto-icon found for "<b>${trimmed}</b>"`;
                        statusEl.className = 'live-icon-status not-found';
                        subtextEl.innerHTML = `Please choose and upload an icon file below.`;
                    }
                })
                .catch(err => {
                    console.warn('Icon lookup failed:', err);
                });
        }

        skillNameInput.addEventListener('input', function () {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(() => {
                checkSkillIcon(this.value);
            }, 350);
        });

        // Trigger initial check if name already has value (e.g. edit page)
        if (skillNameInput.value.trim()) {
            checkSkillIcon(skillNameInput.value);
        }
    }
});
