document.addEventListener('DOMContentLoaded', function () {
    const mouseTracker = document.getElementById('mouse_tracker');
    let mouseX = 0;
    let mouseY = 0;
    let circleX = 0;
    let circleY = 0;
    const easingFactor = 0.1; // Facteur d'amortissement pour le flottement
    let isMouseOverPage = true;
    let isFadingOut = false;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    document.addEventListener('mouseenter', () => {
        isMouseOverPage = true;
        if (isFadingOut) {
            isFadingOut = false;
            clearTimeout(fadeOutTimeout);
        }
        // Réinitialisez la position de l'élément au centre de la page
        circleX = mouseX;
        circleY = mouseY;

        // Ajustez l'opacité de manière progressive
        fadeElementIn(mouseTracker, 1000); // 1000 millisecondes (1 seconde)
    });

    document.addEventListener('mouseleave', () => {
        isMouseOverPage = false;
        isFadingOut = true;
        // Ajustez l'opacité de manière progressive et planifiez le réglage de l'opacité à 0
        fadeElementOut(mouseTracker, 1000); // 1000 millisecondes (1 seconde)
    });

    let fadeOutTimeout = null;

    function fadeElementIn(element, duration) {
        element.style.opacity = 0;
        let startTime = null;

        function fadeIn(timestamp) {
            if (!startTime) startTime = timestamp;
            const elapsed = timestamp - startTime;
            element.style.opacity = Math.min(1, elapsed / duration);
            if (elapsed < duration) {
                requestAnimationFrame(fadeIn);
            }
        }

        requestAnimationFrame(fadeIn);
    }

    function fadeElementOut(element, duration) {
        element.style.opacity = 1;
        let startTime = null;

        function fadeOut(timestamp) {
            if (!startTime) startTime = timestamp;
            const elapsed = timestamp - startTime;
            element.style.opacity = 1 - Math.min(1, elapsed / duration);
            if (elapsed < duration) {
                fadeOutTimeout = setTimeout(() => {
                    if (!isMouseOverPage) {
                        element.style.opacity = 0;
                        isFadingOut = false;
                    }
                }, duration);
                requestAnimationFrame(fadeOut);
            }
        }

        requestAnimationFrame(fadeOut);
    }

    function updateCirclePosition() {
        if (isMouseOverPage) {
            const circleWidth = mouseTracker.offsetWidth;
            const circleHeight = mouseTracker.offsetHeight;

            // Calcul de la position du coin supérieur gauche de l'élément pour suivre la souris avec amortissement
            const targetX = mouseX - circleWidth / 2;
            const targetY = mouseY - circleHeight / 2 + window.scrollY; // Ajout du décalage vertical réel lié au scroll

            const dx = targetX - circleX;
            const dy = targetY - circleY;
            circleX += dx * easingFactor;
            circleY += dy * easingFactor;

            mouseTracker.style.transform = `translate(${circleX}px, ${circleY}px)`;
        }

        requestAnimationFrame(updateCirclePosition);
    }

    updateCirclePosition();
});
