document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("contactForm");
    if (!contactForm) {
        return;
    }

    contactForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const formData = new FormData(this);
        const responseMessage = document.getElementById("formMessage");
        const submitButton = this.querySelector('button[type="submit"]');
        const originalButtonHtml = submitButton.innerHTML;
        
        // Get CSRF token from the form
        const csrfTokenEl = document.querySelector('[name=csrfmiddlewaretoken]');
        const csrfToken = csrfTokenEl ? csrfTokenEl.value : '';
        
        // Show loading state
        submitButton.innerHTML = `<span>Sending...</span>`;
        submitButton.disabled = true;
        if (responseMessage) {
            responseMessage.innerHTML = `<div class="loading-message">?? Sending your message...</div>`;
        }

        try {
            const response = await fetch("/", {
                method: "POST",
                body: formData,
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": csrfToken
                }
            });

            const result = await response.json();

            if (result.success) {
                if (responseMessage) {
                    responseMessage.innerHTML = `<div class="success-message">? ${result.message || 'Message sent successfully!'}</div>`;
                }
                contactForm.reset();
                
                setTimeout(() => {
                    if (responseMessage) {
                        responseMessage.innerHTML = "";
                    }
                }, 6000);
            } else {
                if (responseMessage) {
                    responseMessage.innerHTML = `<div class="error-message">? ${result.error || 'Failed to send message.'}</div>`;
                }
            }
        } catch (error) {
            console.error("Contact form fetch error:", error);
            if (responseMessage) {
                responseMessage.innerHTML = `<div class="error-message">? Network error. Please check your connection and try again.</div>`;
            }
        } finally {
            submitButton.innerHTML = originalButtonHtml;
            submitButton.disabled = false;
        }
    });
});
