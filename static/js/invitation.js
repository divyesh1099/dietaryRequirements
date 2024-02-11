document.addEventListener('DOMContentLoaded', function() {
    gsap.registerPlugin(ScrollTrigger, MotionPathPlugin);

    // Direct integration of the motion path in the animation call
    gsap.to(".animated-balloon", {
        ease: "none",
        motionPath: {
            path: [
                {x: 100, y: -20},
                {x: 300, y: 10},
                {x: 500, y: 100},
                {x: 750, y: -100},
                {x: 350, y: -50},
                {x: 600, y: 100},
                {x: 800, y: 0},
                {x: window.innerWidth, y: -250}, // End off-screen for a continuous effect
            ],
            curviness: 1.25,
            autoRotate: true
        },
        scrollTrigger: {
            trigger: ".invitation-section",
            start: "top top",
            end: "bottom bottom",
            scrub: true,
        }
    });

    // No changes to the floating animations; they remain as previously defined
    function animateFloating(selector) {
        gsap.to(selector, {
            y: '-20px',
            duration: 2,
            repeat: -1,
            yoyo: true,
            ease: 'sine.inOut',
            scrollTrigger: {
                trigger: selector,
                start: "top bottom",
                end: "bottom top",
                scrub: true,
            },
        });
    }

    // Apply floating animation to other elements as needed
    animateFloating('.animated-confetti');
    animateFloating('.animated-gift');
});
